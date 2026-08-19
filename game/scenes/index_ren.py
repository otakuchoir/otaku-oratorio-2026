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
    # S('gen_scene01', 'Preshow'),
    S('scene02',  'Memorial Monster Commercial; SONG: Fumetsu no Hero'),
    S('scene03',  'Initial Training Battle'),
    S('scene03a', 'IRL: Opening Transition; SONG: Butter-Fly'),
    S('scene04',  'Academy Classroom'),
    S('scene05',  'School Grounds, Meet Barthandelus'),
    S('scene05a', 'SONG: Ragnarok'),
    S('scene06',  'Train Station'),
    S('scene06a', 'SONG: Hana Ni Natte'),
    S('scene07',  'Classroom scene 1'),
    S('scene08',  'Classroom scene 2'),
    S('scene09',  'IRL: Usagi and Linda'),
    S('scene09a', 'SONG: Moonlight Densetsu'),
    S('scene10',  'Shuttle to Earth, Takeoff'),
    S('scene11',  "Kelisha's Shuttle Office"),
    S('scene12',  'Arriving on Earth'),
    S('scene13',  'New Jersey Negotiations. SONG: Lilium; MANGA: Destruction of New Jersey'),
    S('scene14',  'Graduation Day'),
    S('scene15',  'Mission Briefing'),
    S('scene15a', 'SONG: Weight of the World'),
    S('scene16',  'IRL?: Dark Side of the Moon; SONG: Ragnarok'),
    S('scene16a', 'MANGA: Discovering the Child'),
    S('scene16b', 'End Act 1'),

    ### Act 2
    S('scene17', 'Start Act 2; Flashback: Eden vs. PD 1'),
    S('scene18', 'Flashback: Eden vs. PD 2, News Report'),
    S('scene18a', 'SONG: The Final Day'),
    # Manga panels
    S('scene19', 'Flashback: Eden vs. PD 2; MANGA: Ultima Cannon Hits the PD'),
    S('scene20', 'Sanders Reassigns Usagi'),
    S('scene21', 'Sanders Chauffeurs Usagi'),
    S('scene22', 'Sanders Leaves Usagi; Research Lab'),
    S('scene23', 'The Child Speaks'),
    S('scene23a', 'SONG: Silhouette'),
    S('scene24', 'Flashback: Jojo Discovers Fast Travel'),
    S('scene25', 'Flashback: Training Battle'),
    S('scene26', 'Usagi and Linda, Takeshi and Elizabeth'),
    S('gen_scene27'),
    S('gen_scene28', "Christmas Party/What's The Tea?"),
    S('gen_scene29', "MANGA: PD's Monologue"),
    S('gen_scene30'),
    S('gen_scene31'),
    S('gen_scene32'),
    S('gen_scene33'),
    S('gen_scene34', "MANGA: Kagu's Memories"),
    S('gen_scene35'),
    S('gen_scene36'),
    S('gen_scene37'),
    S('gen_scene38'),
    S('gen_scene39'),
    S('gen_scene40', "MANGA: Kagu's Final Evolution"),
    S('gen_scene41', 'IRL: Road Trip'),
]
len_scenes = len(scenes)
