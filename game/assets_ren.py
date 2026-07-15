# Load all asset files.
#
# Renpy has built-in image autoloading. However, it requires particular file
# layouts and file names, and I don't want to dictate how our artists structure
# their files. I also don't want the git assets mirror to move their around -
# that makes syncing too hard. So, we'll write our own loading script.
#
# Missing images throw an error when starting the game, instead of showing a
# "couldn't find filename" replacement image. No missing images will sneak into
# our project this way.

import renpy # type: ignore

"""renpy
# dims characters that aren't speaking.
# dimmed images are defined while loading sprites, so these have to be defined in this file too
transform dim:
    matrixcolor BrightnessMatrix(-0.25)
    zoom 0.95
transform nodim:
    matrixcolor BrightnessMatrix(0)
    zoom 1

init python:
"""

import re

def load_image(name: str, path: str):
    """Load an image if possible, or throw an error.
    
    Ren'py's normal image loading behavior, if an image can't be found, is to
    show "couldn't load filename.png" and keep going. But we might not notice!
    Instead, throw an error so it can't possibly be missed.
    Prefer this instead of `renpy.image(...)` or `image ...`
    """
    if not renpy.loadable(path):
        raise RuntimeError("couldn't load file: "+path)
    return renpy.image(name, path)

# Load all sprites.
#
# For example, the file `usagi-happy-1.png` is loaded in renpy as `usagi happy1`.
# Use it like `show usagi happy1`.
#
# The image tag `usagi` is very important. In the following example:
#     show usagi happy1
#     show usagi happy2
#     show takeshi happy1
# Renpy knows the second `show` replaces the first, instead of showing a new
# image, because they have the same tag. It knows the third `show` is for a
# different character because its tag is different.
#
# The image attribute `happy1` is less important, but I chose to remove dashes
# because the renpy vscode extension can't autocomplete them.
#
# Also adds a dimmed version of each sprite, for when that character isn't speaking.
# For example, `show usagi happy1 dim`
fs: list[str] = renpy.list_files()
for f in fs:
    m = re.match(r"^assets\/Character Sprites\/(?P<basename>.*).(png|jpg|gif)$", f)
    if m:
        basename = m.group('basename')
        (tag, attr) = basename.split('-', 1)
        attr = attr.replace('-', '')
        name = ' '.join([tag, attr])
        load_image(name, f)
        print('image:', name, '-', f)
        renpy.image(name+' dim', dim(renpy.get_registered_image(name))) # type: ignore

# Load a list of other assets with less predictible naming patterns.
load_image('logo', 'assets/Logo/OO2 Logo V3.png')
load_image('scene16a', 'assets/Scene 16/Scene16A.png')
load_image('scene16b', 'assets/Scene 16/Scene16B.png')
load_image('scene16c', 'assets/Scene 16/Scene16C.png')

# Uncomment to prove that missing images throw an error, and can't sneak into our project
# load_image('missing_image', 'assets/missing-image-uroiepwreowpqrueopiqwueriowq.png')