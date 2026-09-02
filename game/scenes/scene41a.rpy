define credits_size = 5.5
define credits_dur = 30
label scene41a:
    scene bg black
    window hide
    window auto
    # show text "{color=#fff}{size=160}CREDITS{/size}{/color}" at truecenter with dissolve
    show bg beige as bglogo:
        anchor (0.5, 0.0)
        pos (0.5, 0.0)
    show logo:
        zoom 0.5
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with dissolve
    pause 2
    show bg beige as bglogo:
        linear credits_dur ypos (0.0-credits_size)
    show logo:
        linear credits_dur ypos (0.5-credits_size)
    show expression scene41.credits:
        anchor (0.5, 0.0)
        # pos (0.5, -2.0)
        pos (0.5, 1.0)
        linear credits_dur ypos (1.0-credits_size)
    # "PLACEHOLDER song: welcome to the new world\nmanga panels/postcards: epilogue\nCREDITS"
    pause
    return

init python:
    import re
    def credits_text(c: str) -> Text:
        # skip the first few lines describing the file to humans
        c ='\n'.join(c.splitlines()[5:])
        c = markdown_to_renpy(c)
        c = 'TODO: credits work in progress\n\n'+c
        # NOPE renpy's default font does not support japanese, gotta find and use one that does for this
        # c = c+'\n\nおわり'
        return Text(c, text_align=0.5)

    def markdown_to_renpy(t) -> str:
        t = re.sub(r'\*\*\*(?P<body>[^\*]*)\*\*\*', r'{b}{i}\g<body>{/i}{/b}', t)
        t = re.sub(r'\*\*(?P<body>[^\*]*)\*\*', r'{b}\g<body>{/b}', t)
        t = re.sub(r'\*(?P<body>[^\*]*)\*', r'{i}\g<body>{/i}', t)
        t = re.sub(r'~~(?P<body>[^\~]*)~~', r'{s}\g<body>{/s}', t)
        t = re.sub(r'\\-', r'-', t)
        t = re.sub(r'\\#', r'#', t)
        t = re.sub(r'\\<[Yy]our [Nn]ame [Hh]ere\\>\n', r'', t)
        return t

define scene41.credits = credits_text(renpy.open_file('images/credits-20260902.md').read().decode('utf-8'))
