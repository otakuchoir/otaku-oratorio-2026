"""List all scenes, in the order the VN shows them."""
import renpy # type: ignore

"""renpy
init python:
"""

import dataclasses
@dataclasses.dataclass(frozen=True)
class S:
    label: str
    """`label ___`, at the top of each scene.rpy file"""

    desc: str = ''
    """A short description used in the "jump to scene" menu"""

    def __str__(self):
        return f"{self.label}: {self.desc}"

scenes = [
    ### Act 1
    S('gen_scene01', 'Preshow'),
    S('gen_scene02', 'Memorial Monster Commercial'),
    S('scene02a', 'SONG: Fumetsu no Hero'),
    S('scene03', 'Initial Training Battle'),
    S('scene03a', 'Opening Transition; SONG: Butter-Fly'),
    S('scene04', 'Academy Classroom'),
    S('scene05', 'School Grounds, Meet Barthandelus'),
    S('scene05a', 'SONG: Ragnarok'),
    S('scene06', 'Train Station'),
    S('scene06a', 'SONG: Hana Ni Natte'),
    S('scene07', '(IRL) Classroom scene 1'),
    S('scene08', '(IRL) Classroom scene 2'),
    S('scene09', '(IRL) Usagi and Linda'),
    S('scene09a', 'SONG: Moonlight Densetsu'),
    S('scene10', 'Shuttle to Earth, Takeoff'),
    S('scene11', "(IRL) Kelisha's Shuttle Office"),
    S('scene12', 'Arriving on Earth'),
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
