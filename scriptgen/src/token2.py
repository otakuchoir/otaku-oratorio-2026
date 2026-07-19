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

# each line happens to be exactly one token
def tokenize_line(line: str) -> Token:
    song_prefix = 'SONG: '
    character_suffix = "(CONT’D)"
    nline = line.strip()  # removes whitespace including newlines
    cline = nline.replace(character_suffix, '').strip()
    mscene = re.match(r'^(?P<a>\d+) +.+ +(?P<b>\d+)$', nline)
    pscene = re.match(r'^(?P<p>\d+)\.$', nline)
    if nline == '':
        return Blank(line=line)
    elif nline == '(MORE)':
        return More(line=line)
    elif nline.startswith(song_prefix):
        return Song(line=line, song=line[len(song_prefix):])
    elif cline in data.characters:
        return Speaker(line=line, speaker=data.characters[cline])
    elif mscene:
        a = int(mscene.group('a'))
        b = int(mscene.group('b'))
        if a == b:
            return Scene(line=line, scene=a)
        else:
            return Unknown(line=line)
    elif pscene:
        p = int(pscene.group('p'))
        return PageNumber(line=line, page=p)
    else:
        return Unknown(line=line)

# what kind of line are we talking about? no context/state allowed
def tokenize(pages: io.Reader[str]) -> Generator[Token]:
    for page in pages:
        for line in page.split('\n'):
            yield tokenize_line(line)
        yield PageBreak()
