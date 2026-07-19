# Transform the pdf script into a VERY imperfect renpy file.
#
# This quick generated file will be our starting point for writing the final
# version. We avoid lots of manual copy-pasting from the script pdf this way.
# It's not perfect because the pdf format isn't consistent, but it's not bad!

from src import parser

# To populate this source file: 
#
# - open the script pdf in chrome
# - select and copy all the text. start from the bottom of the document, not the top - much faster scrolling
# - open a new, empty file in vscode
# - paste the text
#
# (I also tried the `pdftotext` tool in ubuntu, but its formatting is not as good)
#
txt_path = "./script.txt"
# rpy_path = "./oo2_script.rpy"
# rpy_path = "../game/oo2_scriptgen.rpy"
rpy_path = "../game/generated_scenes/"
debug_path = "./oo2_debug.txt"

def main():
    with open(txt_path, 'r') as txt:
        with open(rpy_path, 'w') as rpy:
            with open(debug_path, 'w') as debug:
                nodes = list(parser.parse_lines(txt))
                parser.write_debug(nodes, debug)
                parser.write_rpy(nodes, rpy)

if __name__=='__main__':
    main()