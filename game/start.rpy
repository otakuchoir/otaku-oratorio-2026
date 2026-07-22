init python:
    scenes = [
        'gen_scene01',
        'scene02',
        'scene02a',
        'gen_scene03',
        'gen_scene04',
        'gen_scene05',
        'gen_scene06',
        # no scene 7
        'gen_scene08',
        'gen_scene09',
        'gen_scene10',
        'gen_scene11',
        'gen_scene12',
        'gen_scene13',
        'gen_scene14',
        'gen_scene15',
        'gen_scene16',
        'gen_scene17',
        # no scene 18
        'gen_scene19',
        'gen_scene20',
        'gen_scene21',
        'gen_scene22',
        'gen_scene23',
        'gen_scene24',
        'gen_scene25',
        'gen_scene26',
        'gen_scene27',
        'gen_scene28',
        'gen_scene29',
    ]
    len_scenes = len(scenes)

label start(i=0):
    while i < len_scenes:
        call expression scenes[i]
        $ i += 1