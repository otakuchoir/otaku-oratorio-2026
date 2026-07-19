import dataclasses
import io
from typing import Generator

from . import ast, token, data

@dataclasses.dataclass(frozen=True)
class Parser:
    dialogue_speaker: token.Speaker | None = None
    dialogue_quote: list[token.Unknown] = dataclasses.field(default_factory=list)
    last_speaker: token.Speaker | None = None
    scene: int | None = None
    page: int | None = None
    version: str | None = None

    def replace(self, **kwargs) -> Parser:
        return dataclasses.replace(self, **kwargs)

    def is_speaking(self):
        """true if a speaker is present."""
        return self.dialogue_speaker is not None

    def is_dialogue_buffered(self):
        """true if a speaker plus one line of dialogue are present."""
        return self.is_speaking() and len(self.dialogue_quote) > 0

    def flush_dialogue(self, next_speaker: token.Speaker | None=None) -> tuple[Parser, list[ast.Node]]:
        if self.is_dialogue_buffered():
            nodes = [ast.Dialogue(
                [self.dialogue_speaker] + self.dialogue_quote,
                self.dialogue_speaker.speaker,
                [q.line.replace('\n', '') for q in self.dialogue_quote],
            )]
        else:
            nodes = []
        self = self.replace(dialogue_speaker=next_speaker, last_speaker=self.dialogue_speaker, dialogue_quote=[])
        return (self, nodes)

    def parse(self, t: token.Token) -> tuple[Parser, list[ast.Node]]:
        if self.version == None and t.type_ != 'version':
            raise Exception('source text must start with "version: <source-file.pdf>"')
        call = f'_parse_{t.type_}'
        return getattr(self, call)(t)

    def _parse_version(self, t: token.Version) -> tuple[Parser, list[ast.Node]]:
        if self.version is not None:
            raise Exception(f"can't have two versions: {self.version}, {t.version}")
        return (self.replace(version=t.version), [])

    def _parse_blank(self, _: token.Blank) -> tuple[Parser, list[ast.Node]]:
        if self.is_dialogue_buffered():
            # blank line means the speaker is done speaking, but only if they've already said something
            # not a perfect heuristic but it's pretty good
            return self.flush_dialogue()
        else:
            return (self, [])

    def _parse_song(self, t: token.Song) -> tuple[Parser, list[ast.Node]]:
        nodes = [ast.ScriptComment([], '\n'), ast.ScriptComment([t], t.line), ast.ScriptComment([], '\n')]
        if self.is_speaking():
            # the speaker is done speaking
            self, dia = self.flush_dialogue()
            return (self, dia + nodes)
        else:
            return (self, nodes)

    def _parse_speaker(self, t: token.Speaker) -> tuple[Parser, list[ast.Node]]:
        # if there was a speaker, they're done speaking
        return self.flush_dialogue(next_speaker=t)

    def _parse_scene(self, t: token.Scene) -> tuple[Parser, list[ast.Node]]:
        nodes = []
        if self.is_speaking():
            (self, ns) = self.flush_dialogue()
            nodes += ns
        # special case the pre-show section, which looks like a scene for some reason
        if 'THE DIMENNA CENTER FOR CLASSICAL MUSIC' in t.line and self.scene is None:
            nodes += [ast.Label([], 'gen_preshow', self.version)]
        else:
            label = f'gen_scene{t.scene:02d}'
            nodes += [ast.Jump([], label), ast.Label([t], label, self.version)]
        nodes += [ast.ScriptComment([], t.line)]
        return (self.replace(scene=t.scene), nodes)

    def _parse_page(self, t: token.Page) -> tuple[Parser, list[ast.Node]]:
        return (self, [ast.PageComment([t], t.page)])

    def _parse_more(self, t: token.More) -> tuple[Parser, list[ast.Node]]:
        # a page break happened while someone is speaking!
        # output the quote so far, but keep the same speaker.
        if self.is_speaking():
            # dialogue's not yet output, output it and make a new one
            self, nodes = self.flush_dialogue(next_speaker=self.dialogue_speaker)
        else:
            if self.last_speaker is None:
                raise Exception('"more" token but no previous speaker', t, self)
            # dialogue's already been output, make a new one
            nodes = []
            self, _ = self.flush_dialogue(next_speaker=self.last_speaker)
        # return (self, nodes + [ast.ScriptComment([t], t.line)])
        return (self, nodes + [ast.ScriptComment([], '(MORE)\n')])

    def _parse_unknown(self, t: token.Unknown) -> tuple[Parser, list[ast.Node]]:
        if self.is_speaking():
            # the speaker is still talking, this token is part of their dialogue
            return (self.replace(dialogue_quote=self.dialogue_quote + [t]), [])
        else:
            # no one's speaking, this is a comment
            return (self, [ast.ScriptComment([t], t.line)])

@dataclasses.dataclass(frozen=True)
class SceneBufferParser:
    """Buffer all ast nodes for a scene to build a list of its characters"""
    buffer: list[ast.Node] = dataclasses.field(default_factory=list)

    def flush(self) -> tuple[SceneBufferParser, list[ast.Node]]:
        return (SceneBufferParser(), self.buffer)

    def parse(self, node: ast.Node) -> tuple[SceneBufferParser, list[ast.Node]]:
        if isinstance(node, ast.Label):
            speakers = [n.speaker for n in self.buffer if isinstance(n, ast.Dialogue)]
            # unique list, preserving order
            speakers = list(dict.fromkeys(speakers))
            speakers_ast = self.build_speakers_ast(speakers)
            return (SceneBufferParser(), speakers_ast + self.buffer + [node])
        else:
            return (SceneBufferParser(buffer = self.buffer + [node]), [])
    
    def build_speakers_ast(self, speakers: list[str]) -> list[ast.Node]:
        images = [data.character_images[s] for s in speakers if s in data.character_images]
        ats = ['center', 'left2', 'right2', 'left', 'right', 'top', 'topleft', 'topright', 'truecenter']
        if len(images) > len(ats):
            raise Exception('too many speakers in one scene', images)
        images_at = zip(images, ats)
        return [ast.Show(img=img, at=at) for (img, at) in images_at]

def parse_lines(lines: io.Reader[str]) -> Generator[ast.Node]:
    return parse_tokens(token.tokenize(lines))

def parse_tokens(tokens: Generator[token.Token]) -> Generator[ast.Node]:
    yield ast.GeneratedAt()
    yield ast.Characters()
    p = Parser()
    p2 = SceneBufferParser()
    for t in tokens:
        p, nodes = p.parse(t)
        for n in nodes:
            p2, nodes2 = p2.parse(n)
            for n2 in nodes2:
                yield n2

def write_debug(ast: Generator[ast.Node], out: io.Writer[str]) -> None:
    for node in ast:
        for line in node.to_debug():
            out.write(line)

def write_rpy(ast: Generator[ast.Node], out: io.Writer[str]) -> None:
    for node in ast:
        out.write(node.to_rpy())
