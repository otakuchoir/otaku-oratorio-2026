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
import dataclasses

config.speaking_attribute = 'focus' # type: ignore

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
        name_unfocus = name
        name_focus = name+' focus'
        load_image(name_focus, f)
        renpy.image(name_unfocus, dim(renpy.get_registered_image(name_focus))) # type: ignore
        # print('image:', name, '-', f)

# Load a list of other assets with less predictible naming patterns.
load_image('logo', 'assets/Logo/OO2 Logo V3.png')
load_image('bg scene16a', 'assets/Scene 16/Scene16A.png')
load_image('bg scene16b', 'assets/Scene 16/Scene16B.png')
load_image('bg scene16c', 'assets/Scene 16/Scene16C.png')
load_image('bg scene13a', 'assets/Storyboards/storyboard-13-1.png')
load_image('bg scene13b', 'assets/Storyboards/storyboard-13-2.png')
load_image('bg scene13c', 'assets/Storyboards/storyboard-13-3.png')
load_image('bg scene13d', 'assets/Storyboards/storyboard-13-4.png')
load_image('bg scene19a', 'assets/Storyboards/storyboard-19-1.png')
load_image('bg scene19b', 'assets/Storyboards/storyboard-19-2.png')
load_image('bg scene19c', 'assets/Storyboards/storyboard-19-3.png')
load_image('bg scene19d', 'assets/Storyboards/storyboard-19-4.png')

# Uncomment to prove that missing images throw an error, and can't sneak into our project
# load_image('missing_image', 'assets/missing-image-uroiepwreowpqrueopiqwueriowq.png')

changelog = renpy.file('CHANGELOG').read().decode('utf-8')
last_updated = re.match(r'^## (?P<u>.*)$', changelog.split('\n')[0]).group('u')
if not last_updated: raise Exception("couldn't find latest version number from changelog")

import dataclasses
@dataclasses.dataclass(frozen=True)
class S:
    label: str
    desc: str = ''

    def __str__(self):
        return f"{self.label}: {self.desc}"

scenes = [
    ### Act 1
    S('gen_scene01', 'Preshow'),
    S('gen_scene02', 'Memorial Monster Commercial'),
    S('scene03', 'Initial Training Battle'),
    S('scene03a', 'Opening Transition; SONG: Butter-Fly'),
    S('gen_scene04', 'Academy Classroom'),
    S('gen_scene05', 'School Grounds, Meet Barthandelus'),
    S('scene05a', 'SONG: Ragnarok'),
    S('gen_scene06', 'Train Station'),
    S('scene06a', 'SONG: Hana Ni Natte'),
    S('scene07_08', '(IRL) Classroom scenes 1 and 2'),
    S('scene09', '(IRL) Usagi and Linda'),
    S('scene09a', 'SONG: Moonlight Densetsu'),
    S('gen_scene10', 'Shuttle to Earth, Takeoff'),
    S('scene11', "(IRL) Kelisha's Shuttle Office"),
    S('gen_scene12', 'Arriving on Earth'),
    S('scene13', '(IRL) New Jersey Negotiations; SONG: Lillium'),
    S('scene14', '(IRL) Graduation Day'),
    S('scene15', '(IRL) Mission Briefing'),
    S('scene15a', 'SONG: Weight of the World'),
    S('scene16', '(partial IRL) Dark Side of the Moon; SONG: Ragnarok'),
    S('scene16a', 'End Act 1'),

    ### Act 2
    S('gen_scene17', 'Start Act 2'),
    S('gen_scene18'),
    S('scene18a', 'SONG: The Final Day'),
    S('scene19', '(IRL)'),
    S('gen_scene20'),
    S('gen_scene21'),
    S('gen_scene22'),
    S('gen_scene23'),
    S('gen_scene24'),
    S('scene25', '(IRL)'),
    S('gen_scene26'),
    S('gen_scene27'),
    S('gen_scene28'),
    S('gen_scene29'),
    S('gen_scene30'),
    S('gen_scene31'),
    S('gen_scene32'),
    S('gen_scene33'),
    S('gen_scene34'),
    S('gen_scene35'),
    S('gen_scene36'),
    S('gen_scene37'),
    S('gen_scene38'),
    S('gen_scene39'),
    S('gen_scene40'),
    S('gen_scene41'),
]
len_scenes = len(scenes)
