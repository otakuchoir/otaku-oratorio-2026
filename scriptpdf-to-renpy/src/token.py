import re
import dataclasses
import io
from typing import Generator
from . import data

def format(t: Token) -> str:
    return f'{t.type_:>10}: {t.line}\n'

@dataclasses.dataclass(frozen=True)
class PageBreak:
    type_ = 'pagebreak'
    line: str = '<page-break>'

@dataclasses.dataclass(frozen=True)
class Speaker:
    type_ = 'speaker'
    line: str
    speaker: str

@dataclasses.dataclass(frozen=True)
class Unknown:
    """Either a line of dialogue, or a stage direction/other comment
    
    We tell the two apart by comparing indentation elsewhere on the page.
    That's too much context for tokenizing, we'll figure out which it is during parsing
    """
    type_ = 'unknown'
    line: str

    def indent(self) -> int:
        """To tell if this is dialogue or not, compare its indentation to other unknown tokens on this page"""
        return len(self.line) - len(self.line.lstrip())

@dataclasses.dataclass(frozen=True)
class Blank:
    type_ = 'blank'
    line: str

@dataclasses.dataclass(frozen=True)
class Song:
    type_ = 'song'
    line: str
    song: str

@dataclasses.dataclass(frozen=True)
class Scene:
    type_ = 'scene'
    line: str
    scene: int

@dataclasses.dataclass(frozen=True)
class PageNumber:
    type_ = 'pagenum'
    line: str
    page: int

@dataclasses.dataclass(frozen=True)
class More:
    type_ = 'more'
    line: str

Token = PageBreak | Speaker | Unknown | Blank | Song | Scene | PageNumber | More

# characters with longest names first, so "Linda Kitadani" is not recognized as "Kitadani" after page breaks with "(MORE)".
characters_by_len = sorted(data.characters.items(), key=lambda c: len(c[0]), reverse=True)

def tokenize_line(line: str) -> list[Token]:
    song_prefix = 'SONG: '
    character_suffix = "(CONT’D)"
    nline = line.strip()  # removes whitespace including newlines
    cline = nline.replace(character_suffix, '').strip()
    mscene = re.match(r'^(?P<a>\d+) +.+ +(?P<b>\d+)$', nline)
    pscene = re.match(r'^(?P<p>\d+)\.$', nline)
    if nline == '':
        return [Blank(line=line)]
    elif nline == '(MORE)':
        return [More(line=line)]
    elif nline.startswith(song_prefix):
        return [Song(line=line, song=line[len(song_prefix):])]
    elif cline in data.characters:
        return [Speaker(line=line, speaker=data.characters[cline])]
    elif mscene:
        a = int(mscene.group('a'))
        b = int(mscene.group('b'))
        if a == b:
            return [Scene(line=line, scene=a)]
        else:
            return [Unknown(line=line)]
    elif pscene:
        p = int(pscene.group('p'))
        return [PageNumber(line=line, page=p)]
    elif nline.endswith(character_suffix):
        # our pdf parser seems to choke on page breaks with '(MORE)' and '(CONT'D)'.
        # it keeps putting the speaker in the same line as their dialogue.
        # easy enough to detect and fix though, since this only happens with (CONT'D)
        #
        # expected: 
        #     (MORE)
        #     <page-break>
        #            SPEAKING CHARACTER (CONT'D)
        #     dialogue dialogue dialogue dialogue
        #     dialogue dialogue dialogue dialogue
        # observed:
        #     (MORE)
        #     <page-break>
        #     dialogue dialogue dialogue dialogue SPEAKING CHARACTER (CONT'D)
        #     dialogue dialogue dialogue dialogue
        for (scriptchar, renpychar) in characters_by_len:
            speaker_line = f'{scriptchar} {character_suffix}'
            if nline.endswith(speaker_line):
                # found our speaker!
                return [Speaker(speaker_line+'\\', renpychar), Unknown(line=line[:-len(speaker_line)])]
        raise Exception(f"looks like this like has the pypdf (CONT'D) speaker bug, but I couldn't find the speaker", line)
    else:
        return [Unknown(line=line)]

# what kind of line are we talking about? no context/state allowed
def tokenize(pages: io.Reader[str]) -> Generator[Token]:
    for page in pages:
        # quick hack for scene 18 because it is formatted differently
        page = page.replace(
            'VARIOUS SCREENS SHOWING THE NEWS OF THE SPACESHIP EDEN AS IT',
            'VARIOUS SCREENS SHOWING THE NEWS OF THE SPACESHIP EDEN AS IT 18',
        )
        for line in page.split('\n'):
            for t in tokenize_line(line):
                yield t
        yield PageBreak()
