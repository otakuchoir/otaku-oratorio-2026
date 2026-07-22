"""Generate ren'py dialogue from the Otaku Oratorio 2 script.

The generated code is just a starting point! It generates talking heads with neutral expressions.
A human must give them expressions, move the sprites around the screen, fix any mistakes in the
generated dialogue, etc.

This code relies on an up-to-date list of every character who speaks in the show, in `src/data.py`.
Keep it up to date when the script changes.
"""
import os
import shutil
import pypdf
from src import token, page_parser, ast_parser
from typing import Generator
import pathlib
import itertools

# Our input file, the OO2 script.
pdf_path = './Otaku Oratorio 2 Script 7-20-2026.pdf'
# Name of the input file without directories. Used in some renpy output.
# Answers the question "which version of the script generated this code? Is it up to date?"
version = pathlib.Path(pdf_path).name
# Intermediate text version of the script, for the developer
debug_path = './oo2_debug.txt'
# Fill this directoy with the generated code.
# Careful, anything already there will be deleted!
rpy_path = "../game/generated/"

def main():
    with pypdf.PdfReader(pdf_path) as pdf:
        # Everything here uses generators. We're not parsing the whole script pdf into memory.
        # (I think it's small enough that we could, but that's bad style.)
        #
        # First, transform the pdf into plain text pages.
        # I don't know how to parse a pdf, but pypdf does, and I do know how to parse plain text.
        # Each string from the generator is one page of plain text.
        ps = pdf_pages(pdf)

        # We parse the script's text in several steps. Each step needs a different set of *context*
        # for its parsing. Grouping our parsing steps by context keeps things much simpler than they
        # would be, if we had one big parser with all of the context instead.
        #
        # First, split each plain text pages into a flat list of `token` objects, defined in src/token.py.
        # These tokens have no context - that is, to parse a token we're only looking at that token.
        # Just like in my compilers class.
        ts = token.tokenize(ps)

        # We need more context to parse some things. For example, indentation: lines that are indented
        # less are stage directions/comments; lines that are indented more are dialogue.
        # (An earlier version of this script didn't have indentation data, and couldn't always tell them apart!)
        #
        # Parse tokens with one page of context at a time, turning "unknown" tokens into "comment"
        # or "dialogue". Indents are consistent in a single page, but different in different pages,
        # so only look at one page at a time.
        # (Tokens with context isn't quite kosher according to my compilers class, but it works well here.
        # Try to keep `page_parser` as small as possible though.)
        pts = page_parser.parse(ts)

        # This is a good place to output a debugging file - the plain text script, each line annotated
        # with the type of token it was parsed as.
        pts, pts2 = itertools.tee(pts)
        with open(debug_path, 'w') as txt:
            for t in pts2:
                txt.write(token.format(t))
                # print(token.format(t), end='')

        # Next step, turn our list of tokens (resembling the script file) into renpy AST nodes (abstract
        # syntax tree, resembling renpy code). This groups dialogue with who's speaking, among other
        # things. It looks at a little nearby context - it keeps some state as it goes, but it doesn't
        # handle things where you have to examine an entire section.
        nodes = ast_parser.parse_pagetokens_to_ast(version, pts)

        # Finally, group our renpy AST by scene. We use this to output one scene at a time of course, but
        # we also use it to figure out what characters are speaking in a scene, so we can show their sprites.
        scenes = ast_parser.parse_ast_to_scenes(nodes)

        # All done parsing! Now we write the generated renpy files to disk.
        # Files are named by scene number.
        try:
            shutil.rmtree(rpy_path)
        except FileNotFoundError:
            pass
        os.mkdir(rpy_path)
        for scene in scenes:
            rpy_file = pathlib.Path(rpy_path) / scene.filename()
            with open(rpy_file, 'w') as rpy:
                ast_parser.write_rpy(scene.nodes, rpy)

def pdf_pages(pdf: pypdf.PdfReader) -> Generator[str]:
    """Output one plaintext page of the script at a time, parsed from a pdf using `pypdf`."""
    pages = len(pdf.pages)
    for pnum in range(pages):
        page = pdf.pages[pnum]
        yield page.extract_text(extraction_mode='layout')

if __name__=='__main__':
    main()