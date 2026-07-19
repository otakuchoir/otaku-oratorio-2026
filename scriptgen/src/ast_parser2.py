import dataclasses
import io
from typing import Generator
from . import ast, token2, page_parser2, data

@dataclasses.dataclass(frozen=False)
class ASTParser:
    version: str
    speaker: token2.Speaker | None = None
    quote: list[page_parser2.Quote] = dataclasses.field(default_factory=list)
    last_speaker: token2.Speaker | None = None
    scene: int | None = None

    def is_speaking(self):
        """true if a speaker is present."""
        return self.speaker is not None

    def is_dialogue_buffered(self):
        """true if a speaker plus one line of dialogue are present."""
        return self.is_speaking() and len(self.quote) > 0

    def flush_dialogue(self, next_speaker: token2.Speaker | None=None) -> ast.Dialogue | None:
        if self.is_dialogue_buffered():
            node = ast.Dialogue(
                [self.speaker] + self.quote,
                self.speaker.speaker,
                [q.line.replace('\n', '').strip() for q in self.quote],
            )
        else:
            node = None
        self.last_speaker = self.speaker
        self.speaker = next_speaker
        self.quote = []
        return node

    def flush_dialogue_list(self, next_speaker: token2.Speaker | None=None) -> ast.Dialogue | None:
        node = self.flush_dialogue(next_speaker)
        return [node] if node is not None else []

    def parse(self, t: page_parser2.PageToken) -> list[ast.Node]:
        call = f'_parse_{t.type_}'
        return getattr(self, call)(t)

    def _parse_blank(self, _: token2.Blank) -> list[ast.Node]:
        # ignored. now that we have indentation info, we no longer rely on blank lines for parsing
        return []

    def _parse_song(self, t: token2.Song) -> list[ast.Node]:
        comment = [ast.ScriptComment([], '\n'), ast.ScriptComment([t], t.line), ast.ScriptComment([], '\n')]
        return self.flush_dialogue_list() + comment

    def _parse_speaker(self, t: token2.Speaker) -> list[ast.Node]:
        # if there was another speaker, they're done speaking now
        return self.flush_dialogue_list(next_speaker=t)

    def _parse_scene(self, t: token2.Scene) -> list[ast.Node]:
        nodes = self.flush_dialogue_list()
        # special case the pre-show section, which looks like a scene for some reason
        if 'THE DIMENNA CENTER FOR CLASSICAL MUSIC' in t.line and self.scene is None:
            nodes += [ast.Label([], 'gen_preshow', self.version)]
        else:
            label = f'gen_scene{t.scene:02d}'
            nodes += [ast.Jump([], label), ast.Label([t], label, self.version)]
        nodes += [ast.ScriptComment([], t.line+'\n')]
        self.scene = t.scene
        return nodes

    def _parse_pagenum(self, t: token2.PageNumber) -> list[ast.Node]:
        return [ast.PageComment([t], t.page)]
    def _parse_pagebreak(self, _: token2.PageBreak) -> list[ast.Node]:
        return []

    def _parse_more(self, t: token2.More) -> list[ast.Node]:
        # a page break happened while someone is speaking!
        # output the quote so far, but keep the same speaker.
        if self.is_speaking():
            # dialogue's not yet output, output it and make a new one
            nodes = self.flush_dialogue_list(next_speaker=self.speaker)
        else:
            if self.last_speaker is None:
                raise Exception('"more" token but no previous speaker', t, self)
            # dialogue's already been output, make a new one
            nodes = self.flush_dialogue(next_speaker=self.last_speaker)
        # return (self, nodes + [ast.ScriptComment([t], t.line)])
        return nodes + [ast.ScriptComment([], '(MORE)\n')]

    def _parse_unknown(self, _: token2.Unknown) -> list[ast.Node]:
        raise Exception('ast_parser cannot handle token.Unknown, use page_parser first')

    def _parse_quote(self, t: page_parser2.Quote) -> list[ast.Node]:
        self.quote += [t]
        return []

    def _parse_comment(self, t: page_parser2.Comment) -> list[ast.Node]:
        return [ast.ScriptComment([t], t.comment+'\n')]

@dataclasses.dataclass(frozen=False)
class SceneBufferParser:
    """Buffer all ast nodes for a scene to build a list of its characters"""
    buffer: list[ast.Node] = dataclasses.field(default_factory=list)

    def flush(self) -> list[ast.Node]:
        buf = self.buffer
        self.buffer = []
        return buf

    def parse(self, node: ast.Node) -> list[ast.Node]:
        if isinstance(node, ast.Label):
            # a new scene has started. build and output the buffered scene's speakers, and the buffered scene itself
            speakers = [n.speaker for n in self.buffer if isinstance(n, ast.Dialogue)]
            # unique list, preserving order
            speakers = list(dict.fromkeys(speakers))
            speakers_ast = self.build_speakers_ast(speakers)
            buf = self.flush()
            return speakers_ast + buf + [node]
        else:
            self.buffer += [node]
            return []
    
    def build_speakers_ast(self, speakers: list[str]) -> list[ast.Node]:
        images = [data.character_images[s] for s in speakers if s in data.character_images]
        ats = ['center', 'left2', 'right2', 'left', 'right', 'top', 'topleft', 'topright', 'truecenter']
        if len(images) > len(ats):
            raise Exception('too many speakers in one scene', images)
        images_at = zip(images, ats)
        return [ast.Show(img=img, at=at) for (img, at) in images_at]

def parse_pagetokens(version: str, tokens: Generator[page_parser2.PageToken]) -> Generator[ast.Node]:
    yield ast.GeneratedAt()
    yield ast.Characters()
    p = ASTParser(version=version)
    p2 = SceneBufferParser()
    for t in tokens:
        nodes = p.parse(t)
        for n in nodes:
            nodes2 = p2.parse(n)
            for n2 in nodes2:
                yield n2

def write_debug(ast: Generator[ast.Node], out: io.Writer[str]) -> None:
    for node in ast:
        for line in node.to_debug():
            out.write(line)

def write_rpy(ast: Generator[ast.Node], out: io.Writer[str]) -> None:
    for node in ast:
        out.write(node.to_rpy())
