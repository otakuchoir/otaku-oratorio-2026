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
transform anchor_sprite:
    anchor (0.5, 1.0)

init python:
"""

import re
import dataclasses

config.speaking_attribute = 'focus' # type: ignore
config.side_image_only_not_showing = True  # type: ignore

def load_image(name: str, path: str, transform=lambda x: x):
    """Load an image if possible, or throw an error.
    
    Ren'py's normal image loading behavior, if an image can't be found, is to
    show "couldn't load filename.png" and keep going. But we might not notice!
    Instead, throw an error so it can't possibly be missed.
    Prefer this instead of `renpy.image(...)` or `image ...`
    """
    if not renpy.loadable(path):
        raise RuntimeError("couldn't load file: "+path)
    return renpy.image(name, transform(path))

# Load all sprites.
#
# For example, the file `usagi-happy-1.png` is loaded in renpy as `usagi happy 1`.
# Use it like `show usagi happy 1`.
#
# The image tag `usagi` is very important. In the following example:
#     show usagi happy 1
#     show usagi happy 2
#     show takeshi happy 1
# Renpy knows the second `show` replaces the first, instead of showing a new
# image, because they have the same tag. It knows the third `show` is for a
# different character because its tag is different.
#
# The image attribute `happy 1` is less important, but I chose to remove dashes
# because the renpy vscode extension can't autocomplete them.
#
# Also adds a dimmed version of each sprite, for when that character isn't speaking.
# For example, `show usagi happy 1 dim`
fs: list[str] = renpy.list_files()
for f in fs:
    m = re.match(r"^assets\/Character Sprites\/(?P<basename>.*).(png|jpg|gif)$", f)
    if m:
        basename = m.group('basename')
        (tag, attr) = basename.split('-', 1) if '-' in basename else (basename, '')
        if tag == 'reporter':
            # exception for the reporters, which have only one image each with no attributes.
            # dashes in the tag break it for some reason, so remove them.
            tag = basename.replace('-', '')
            attr = ''
        if basename == 'train-security':
            tag = 'train_security'
            attr = ''
        attr = attr.replace('-', ' ')
        name = ' '.join([tag, attr])
        name_unfocus = name
        name_focus = name+' focus'
        load_image(name_focus, f, transform=anchor_sprite) # type: ignore
        renpy.image(name_unfocus, Transform(dim(renpy.get_registered_image(name_focus)))) # type: ignore
        # print('image:', name, '-', f)

    m = re.match(r"^assets\/backgrounds\/(?P<basename>.*).(png|jpg|gif)$", f)
    if m:
        basename = m.group('basename')
        attrs = basename.split('-')
        name = ' '.join(['bg'] + attrs)
        load_image(name, f)

# Load a list of other assets with less predictible naming patterns.
load_image('logo', 'assets/Logo/OO2 Logo V3.png')
load_image('bg scene16a nofg', 'assets/Scene 16/Scene 16 - no foreground/Scene16A-noforeground.png')
load_image('bg scene16b nofg', 'assets/Scene 16/Scene 16 - no foreground/Scene16B-noforeground.png')
load_image('bg scene16c nofg', 'assets/Scene 16/Scene 16 - no foreground/Scene16C-noforeground.png')
load_image('bg scene16a', 'assets/Scene 16/Scene16A.png')
load_image('bg scene16b', 'assets/Scene 16/Scene16B.png')
load_image('bg scene16c', 'assets/Scene 16/Scene16C.png')
load_image('bg scene13a', 'assets/Storyboards/storyboard-13-1.png')
load_image('bg scene13b', 'assets/Scene 13 - NJ blows up/scene13-2.png')
load_image('bg scene13c', 'assets/Scene 13 - NJ blows up/scene13-3.png')
load_image('bg scene13d', 'assets/Scene 13 - NJ blows up/scene13-4.png')
load_image('bg scene19a', 'assets/Storyboards/storyboard-19-1.png')
load_image('bg scene19b', 'assets/Storyboards/storyboard-19-2.png')
load_image('bg scene19c', 'assets/Storyboards/storyboard-19-3.png')
load_image('bg scene19d', 'assets/Storyboards/storyboard-19-4.png')

# Uncomment to prove that missing images throw an error, and can't sneak into our project
# load_image('missing_image', 'assets/missing-image-uroiepwreowpqrueopiqwueriowq.png')

changelog = renpy.file('CHANGELOG').read().decode('utf-8')
last_updated = re.match(r'^## (?P<u>.*)$', changelog.split('\n')[0]).group('u')
if not last_updated: raise Exception("couldn't find latest version number from changelog")

# create the title page from the logo (transparent png) + a solid color background.
# be careful not to mangle the logo's aspect ratio!
# 
# we do this in three steps:
# 1. create a large solid-color image, with exactly the same aspect ratio as our screen.
#    put the logo in roughly the center-right of it.
# 2. scale that image down to match our theater's screen size.
# 3. flatten the image down to one layer. usually renpy happily uses multilayer images,
#    but they break if used for the main screen background for whatever reason
logo_dim = (2804, 1558)
screen_dim = (1440, 1080)
renpy.image('bg mainmenu', Flatten(Transform(Composite( # type: ignore
    (int(screen_dim[0]*2.5), int(screen_dim[1]*2.5)),
    (0,0), Solid('#e7dbc7'), # type: ignore
    (800, 550), renpy.get_registered_image('logo'),
), size=screen_dim)))