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
    S('scene06',  'Train Station'),
    S('scene06a', 'SONG: Hana Ni Natte'),
    S('scene07',  'Classroom scene 1'),
    S('scene08',  'Classroom scene 2'),
    S('scene09',  'Usagi and Linda'),
    S('scene09a', 'SONG: Moonlight Densetsu'),
    S('scene10',  'Shuttle to Earth, Takeoff'),
    S('scene11',  "Kelisha's Shuttle Office"),
    S('scene12',  'Arriving on Earth'),
    S('scene12a',  'SONG: Shanghai Tan'),
    S('scene12b',  'New Jersey News Report'),
    S('scene13',  'New Jersey Negotiations. SONG: Lilium; MANGA: Destruction of New Jersey'),
    S('eyecatch06', 'Eyecatch: Ultima Cannon'),
    S('scene14',  'Graduation Day'),
    S('scene15',  'Mission Briefing'),
    S('scene15a', 'SONG: Weight of the World'),
    S('scene16',  'Dark Side of the Moon; SONG: Ragnarok'),
    S('scene16a', 'MANGA: Discovering the Child'),
    S('scene16b', 'End Act 1'),

    ### Act 2
    S('scene17', 'Start Act 2; Flashback: Eden vs. PD 1'),
    S('scene18', 'Flashback: Eden vs. PD 2, News Report'),
    S('scene19', 'Flashback: Eden vs. PD 3; MANGA: Ultima Cannon Hits the PD'),
    S('scene20', 'Sanders Reassigns Usagi'),
    S('scene21', 'Sanders Chauffeurs Usagi'),
    S('scene22', 'Sanders Leaves Usagi; Research Lab'),
    S('scene23', 'The Child Speaks'),
    S('scene23a', 'SONG: Silhouette'),
    S('scene24', 'Flashback: Jojo Discovers Fast Travel'),
    S('scene25', 'Flashback: Training Battle'),
    S('scene25a',  'SONG: Baka Mitai'),
    S('scene26', 'Usagi and Linda, Takeshi and Elizabeth'),
    S('scene27', 'The Story of Princess Kaguya'),
    S('scene28', "Flashback: Christmas Party/What's The Tea?"),
    S('scene29', "MANGA/Flashback: PD's Monologue"),
    S('scene29a', "SONG: Floating Moon on the Water"),
    S('scene30', "Takeshi's Message"),
    S('scene31', "Spying on Usagi; Kagu's Hopes and Dreams"),
    S('scene31a', "SONG: Soto"),
    S('scene31b', "\"If you don't do it...\""),
    S('scene32', 'Flashback: Kohei on the Eden'),
    S('scene33', 'Kagu Remembers'),
    S('scene34', "MANGA: Kagu's Memories"),
    S('scene34a', "SONG: Destati"),
    S('scene35', "Confronting Barthandelus"),
    S('scene36', "Flashback: The Eden's Escorts"),
    S('scene37', "Flashback: The Eden vs. The Plant Destroyer"),
    S('scene38', "Barthandelus's Answer"),
    S('scene39', "The Last News Report"),
    S('scene40', "The Final Battle; SONG: Smash Opening; MANGA: Kagu's Final Evolution"),
    S('scene41', 'MANGA: Road Trip'),
    S('scene41a', 'SONG: welcome to the new world; CREDITS'),
]
len_scenes = len(scenes)
