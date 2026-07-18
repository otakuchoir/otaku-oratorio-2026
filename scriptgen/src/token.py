import re
import dataclasses
import io
from typing import Generator
from . import data

class Base:
    type_: str
    line: str

    def __str__(self):
        return format(self.type_, self.line)

def format(t: str, line: str) -> str:
    return f'{t:>10}: {line}'

@dataclasses.dataclass(frozen=True)
class Speaker(Base):
    type_ = 'speaker'
    line: str
    speaker: str

@dataclasses.dataclass(frozen=True)
class Unknown(Base):
    type_ = 'unknown'
    line: str

@dataclasses.dataclass(frozen=True)
class Blank(Base):
    type_ = 'blank'
    line: str

@dataclasses.dataclass(frozen=True)
class Song(Base):
    type_ = 'song'
    line: str
    song: str

@dataclasses.dataclass(frozen=True)
class Scene(Base):
    type_ = 'scene'
    line: str
    scene: int

@dataclasses.dataclass(frozen=True)
class Page(Base):
    type_ = 'page'
    line: str
    page: int

@dataclasses.dataclass(frozen=True)
class More(Base):
    type_ = 'more'
    line: str

@dataclasses.dataclass(frozen=True)
class Version(Base):
    type_ = 'version'
    line: str
    version: str

Token = Speaker | Unknown | Blank | Song | Scene | Page | More | Version

# what kind of line are we talking about? no context/state allowed
def tokenize(lines: io.Reader[str]) -> Generator[Token]:
    for line in lines:
        yield tokenize_line(line)

# each line happens to be exactly one token
def tokenize_line(line: str) -> Token:
    song_prefix = 'SONG: '
    version_prefix = 'version:'
    character_suffix = " (CONT’D)"
    nline = line.replace('\n', '')
    cline = nline.replace(character_suffix, '')
    mscene = re.match(r'^(?P<a>\d+) .+ (?P<b>\d+)$', nline)
    pscene = re.match(r'^(?P<p>\d+)\.$', nline)
    if nline == '':
        return Blank(line=line)
    elif nline == '(MORE)':
        return More(line=line)
    elif nline.startswith(song_prefix):
        return Song(line=line, song=line[len(song_prefix):])
    elif nline.startswith(version_prefix):
        return Version(line=line, version=line[len(version_prefix):].strip())
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
        return Page(line=line, page=p)
    else:
        return Unknown(line=line)
