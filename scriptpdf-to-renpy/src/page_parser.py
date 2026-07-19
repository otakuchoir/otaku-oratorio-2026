from . import ast, token
import dataclasses
from typing import Generator

@dataclasses.dataclass(frozen=True)
class Quote:
    type_ = 'quote'
    line: str
    
    @property
    def quote(self):
        return self.line.strip()

@dataclasses.dataclass(frozen=True)
class Comment:
    type_ = 'comment'
    line: str
    
    @property
    def comment(self):
        return self.line.strip()

PageToken = token.Token | Quote | Comment
"""A token, parsed with additional page-wide context

This doesn't quite fit the parser model I learned in my compilers class, but it works well here
"""

format = token.format

@dataclasses.dataclass(frozen=False)
class PageParser:
    num: int = 0
    buf: list[token.Token] = dataclasses.field(default_factory=list)

    def parse_token(self, t: token.Token) -> list[PageToken]:
        self.buf.append(t)
        if t.type_ == 'pagebreak':
            return self.flush()
        elif t.type_ == 'pagenum' and t.page != self.num+1:
            raise Exception(f'parsed page ({t.page}) does not match computed page ({self.num+1})')
        else:
            return []
    
    def flush(self) -> list[PageToken]:
        self.num += 1
        buf = self.buf
        self.buf = []
        candidates: list[token.Unknown] = [t for t in buf if t.type_ == 'unknown']
        num_speakers = len([t for t in buf if t.type_ == 'speaker'])
        indents = sorted(list(set(t.indent() for t in candidates)))
        if num_speakers == 0:
            # if noone's speaking on this page, they're all comments, easy
            return [process_unknown(t, None) for t in buf]
        if len(indents) == 0:
            # there's nothing that needs processing, easy
            return [t for t in buf]
        elif len(indents) == 1:
            # either they're all quotes, or all comments. which one?
            # there must be a speaker somewhere on the page, we checked for that earlier. therefore, they're all quotes
            return [process_unknown(t, indents[0]) for t in buf]
        else:
            # the *second-smallest* indent is the quotes.
            # the smallest indent is stage direction, and any larger indents are big section markers like "act 1", etc.
            q = indents[1]
            return [process_unknown(t, q) for t in buf]

def process_unknown(t: token.Token, quote_indent: int | None) -> PageToken:
    if t.type_ != 'unknown':
        return t
    if t.indent() == quote_indent:
        return Quote(t.line)
    return Comment(t.line)

def parse(tokens: Generator[token.Token]) -> Generator[ast.Node]:
    p = PageParser()
    for t in tokens:
        for node in p.parse_token(t):
            yield node