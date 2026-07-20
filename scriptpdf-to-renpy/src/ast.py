import dataclasses
import datetime

from . import data, token

def format_debug(t: str, line: str) -> str:
    return f'{t:>10}: {line}'

@dataclasses.dataclass(frozen=True)
class Dialogue:
    tokens: list[token.Token]
    speaker: str
    quotes: list[str] = dataclasses.field(default_factory=list)

    def quote(self) -> str:
        return ' '.join(self.quotes)

    def to_rpy(self) -> str:
        quote = self.quote().replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%')
        return f'    {self.speaker} "{quote}"\n'

    def to_debug(self) -> list[str]:
        return [format_debug('quote' if t.type_ == 'unknown' else t.type_, t.line) for t in self.tokens]
    
@dataclasses.dataclass(frozen=True)
class Label:
    tokens: list[token.Token]
    name: str
    version: str

    def to_rpy(self) -> str:
        return f"""
label {self.name}:
    scene black
    show text "{{color=#fff}}Scene \\"{self.name}\\" automatically generated from \\"{self.version}\\"\\nat \\"{datetime.datetime.now()}\\" by scriptpdf-to-renpy.py (AI-free)\\nThis scene still needs human editing. It is not done. Expect mistakes.{{/color}}" at top 
"""

    def to_debug(self) -> list[str]:
        return [format_debug(t.type_, t.line) for t in self.tokens]

@dataclasses.dataclass(frozen=True)
class Jump:
    tokens: list[token.Token]
    name: str

    def to_rpy(self) -> str:
        return f'    jump {self.name}\n'

    def to_debug(self) -> list[str]:
        return [format_debug(t.type_, t.line) for t in self.tokens]

@dataclasses.dataclass(frozen=True)
class ScriptComment:
    tokens: list[token.Token]
    line: str

    def to_rpy(self) -> str:
        return f'    # > {self.line}'

    def to_debug(self) -> list[str]:
        return [format_debug(t.type_, t.line) for t in self.tokens]

@dataclasses.dataclass(frozen=True)
class PageComment:
    tokens: list[token.Token]
    page: int

    def to_rpy(self) -> str:
        return f'    ### page {self.page} ###\n'

    def to_debug(self) -> list[str]:
        return [format_debug(t.type_, t.line) for t in self.tokens]

@dataclasses.dataclass(frozen=True)
class Characters:
    tokens: list[token.Token] = dataclasses.field(default_factory=list)
    characters: list[str] = dataclasses.field(default_factory=lambda: data.characters_without_images)

    def to_rpy(self) -> str:
        return ''.join(f'define {c} = Character("{c.upper()}")\n' for c in self.characters)

    def to_debug(self) -> list[str]:
        return [format_debug(t.type_, t.line) for t in self.tokens]

@dataclasses.dataclass(frozen=True)
class GeneratedAt:
    tokens: list[token.Token] = dataclasses.field(default_factory=list)
    datetime: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.now)

    def to_rpy(self) -> str:
        return f'#\n# automatically generated on {self.datetime}\n#\n'

    def to_debug(self) -> list[str]:
        return [format_debug(t.type_, t.line) for t in self.tokens]

@dataclasses.dataclass(frozen=True)
class Show:
    img: str
    at: str | None = None
    behind: str | None = None

    def to_rpy(self) -> str:
        at = f" at {self.at}" if self.at else ""
        behind = f" behind {self.behind}" if self.behind else ""
        return f"    show {self.img}{at}{behind}\n"

    @property
    def tokens(self):
        return []

    def to_debug(self) -> list[str]:
        return []

# Not really a tree, more of a list, but that's fine here.
# AST is still the technical parser term
Node = Dialogue | Label | Jump | ScriptComment | PageComment | Characters | GeneratedAt | Show

@dataclasses.dataclass(frozen=True)
class Scene:
    label: str
    nodes: list[Node]
    def filename(self):
        return f"{self.label}.rpy"
