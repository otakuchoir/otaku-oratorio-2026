# hardcoded list of every character who speaks throughout the show.
# this is how we recognize the speaker when parsing!
# add to this list as the script changes.
# format: `('name in the script', 'name in renpy')`
# or if they're the same, just `'name'``
#
# easiest way to populate this list: generate the rpy file, read and
# look for dialogue in its comments. They're easy to spot. Add each name
# to this list, rebuild, repeat.
_characters = [
    ('announcer (voiceover)', 'announcer'),
    ('kitadani (red)', 'kitadani'),
    'kitadani',
    'monster',
    ('computer voice', 'computer'),
    # scene 2
    'sanders',
    'takeshi',
    ("takeshi's console", 'console'),
    'usagi',
    # scene 3
    ('professor kelisha', 'kelisha'),
    ('takeshi, usagi & sanders', 'trio'),
    ('classmate', 'classmate'),
    ('news reporter 1', 'reporter1'),
    ('news reporter 2', 'reporter2'),
    ('news reporter 3', 'reporter3'),
    ('the king', 'king'),
    # scene 4
    ('barthandelus', 'bart'),
    # scene 5
    ('train security guard', 'guard'),
    # scene 6
    ('professor jojo', 'jojo'),
    # scene 9
    ('linda kitadani', 'linda'),
    # scene 13
    ('elite general', 'general'),
    ('queen elizabeth newark', 'queen'),
    # scene 17
    ('gunner chief', 'gunner'),
    ('first officer', 'officer'),
    # scene 19
    ('navigation chief', 'navigator'),
    'navigator',
    ('planet destroyer adult', 'destroyer'),
    # scene 20
    ('office worker', 'worker'),
    # scene 23
    ('the child', 'child'),
    # scene 24
    ('gossiping student 1', 'student1'),
    ('gossiping student 2', 'student2'),
    ('gossiping student 3', 'student3'),
    ('kohei kitadani', 'kohei'),
    # scene 25
    ('professor wellington', 'wellington'),
    ('linda hudson', 'linda'),
    ('robert huxtable', 'huxtable'),
    # wait, she also has a few lines in this scene as queen?
    ('princess elizabeth newark', 'princess'),
    # scene 27
    # hm, how should we handle the same character with multiple names
    # in the script? 'noname' and 'kagu' and 'the child' are all the same.
    # renpy supports characters with dynamic names, but that might not be
    # worth the trouble vs. treating them as separate characters.
    # I'll treat them as separate for now, but reassess this later.
    ('noname', 'noname'), 
    ('kagu', 'kagu'), 
]
_characters: list[tuple[str, str]] = [(c, c) if isinstance(c, str) else c for c in _characters]
# format script names a bit. character names in the script are always uppercase, but I don't wanna type them that way
characters = dict([(s.upper().replace("'", "’"), r) for s, r in _characters])
# unique list values, preserving order
character_list = list(dict.fromkeys(r for _,r in _characters))

# Default images for each speaker
_character_images = [
    'bart neutral',
    'child neutral',
    'jojo neutral',
    'kelisha neutral',
    'sanders neutral',
    'takeshi neutral',
    'usagi happy1',
    'queen neutral',
    'linda neutral',
    'huxtable neutral',
    ('general', 'huxtable neutral'),
]
character_images = dict((i.split(' ')[0], i) if isinstance(i, str) else i
                        for i in _character_images)

# If we don't have sprites for a character, they probably don't have a character definition yet
# - that is, an entry in `characters.rpy`.
characters_without_images = [c for c in character_list if c not in character_images]