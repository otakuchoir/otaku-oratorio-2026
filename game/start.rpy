init python:
    scenes = [
        ### Act 1
        'gen_scene01',
        'scene02',
        'scene02a',
        'gen_scene03',
        'gen_scene04',
        'scene04a',
        'gen_scene05',
        'scene05a',
        'scene06', # IRL
        # no scene 7
        # scene 8 IRL, same file as scene 6
        'scene09', # IRL
        'scene09a',
        'gen_scene10',
        'scene11', # IRL
        'gen_scene12',
        'scene13', # IRL
        'scene14', # IRL
        'scene15', # IRL
        'scene15a',
        'scene16', # partial IRL

        ### Act 2
        'gen_scene17',
        'gen_scene18',
        'scene18a',
        'scene19', # IRL
        'gen_scene20',
        'gen_scene21',
        'gen_scene22',
        'gen_scene23',
        'gen_scene24',
        'scene25', # IRL
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