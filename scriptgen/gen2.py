import os
import shutil
import pypdf
from src import token2, page_parser2, ast_parser2
from typing import Generator
import pathlib
import itertools

pdf_path = './Otaku Oratorio 2 Script 7-15-2026.pdf'
txt_path = './oo2_debug.txt'
rpy_path = "../game/scenegen/"
version = pathlib.Path(pdf_path).name

skipped_scenes = set(['scene02'])

def main():
    with pypdf.PdfReader(pdf_path) as pdf:
        ps = pdf_pages(pdf)
        #ts, ts2 = itertools.tee(token2.tokenize(ps))
        #for t in ts2:
        #    txt.write(token2.format(t))
        #    print(token2.format(t), end='')
        ts = token2.tokenize(ps)
        pts, pts2 = itertools.tee(page_parser2.parse(ts))
        with open(txt_path, 'w') as txt:
            for t in pts2:
                txt.write(token2.format(t))
                # print(token2.format(t), end='')
        scenes = ast_parser2.parse_pagetokens(version, pts)
        try:
            shutil.rmtree(rpy_path)
        except FileNotFoundError:
            pass
        os.mkdir(rpy_path)
        for scene in scenes:
            if scene.label not in skipped_scenes:
                rpy_file = pathlib.Path(rpy_path) / scene.filename()
                with open(rpy_file, 'w') as rpy:
                    ast_parser2.write_rpy(scene.nodes, rpy)

def pdf_pages(pdf: pypdf.PdfReader) -> Generator[str]:
    pages = len(pdf.pages)
    for pnum in range(pages):
        page = pdf.pages[pnum]
        yield page.extract_text(extraction_mode='layout')

if __name__=='__main__':
    main()