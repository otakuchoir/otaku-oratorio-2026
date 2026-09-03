define credits_size = 11.5
# TODO: we're singing "welcome to the new world" here, so duration should be a bit longer than that.
# but... that's so slow during dev.
# define credits_dur = credits_size * 8.0
define credits_dur = credits_size * 8.0
define driving_scrolls_at = 5.5
define driving_dur = (driving_scrolls_at / credits_size) * credits_dur
define roxbury_scrolls_at = 8.5

label scene41a:
    scene bg black
    window hide
    window auto

    show bg beige as bglogo:
        anchor (0.5, 0.0)
        pos (0.5, 0.0)
    show logo:
        zoom 0.5
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with dissolve
    pause

    call ed.driving(delay=0)
    # hide/reshow logo so it's on top of the driving animation. easier to do this than to specify 'behind' for all the driving images
    hide bglogo
    hide logo
    show bg beige as bglogo:
        anchor (0.5, 0.0)
        pos (0.5, 0.0)
    show logo:
        zoom 0.5
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    # pause 2.0

    show bg beige as bglogo:
        linear credits_dur ypos (0.0-credits_size)
    show logo:
        linear credits_dur ypos (0.5-credits_size)
    show expression scene41.credits behind bgloop_x_0, bgloop_x_1:
        anchor (0.5, 0.0)
        # pos (0.5, -2.0)
        pos (0.5, 1.0)
        linear credits_dur ypos (1.0-credits_size)
    # "PLACEHOLDER song: welcome to the new world\nmanga panels/postcards: epilogue\nCREDITS"
    
    call roxbury
    show layer roxbury:
        anchor (0.5, 0.5)
        zoom 0.5
        pos (0.5, 6.5)
        linear credits_dur ypos (roxbury_scrolls_at-credits_size)

    pause
    return

image ed_bg_driving = Transform(Composite(
    (1440*2, 1080),
    (0, 0), 'bg countryside',
    (1440, 0), Transform('bg countryside', xzoom=-1),
), zoom=0.5)

transform ed.driving_scroll(delay, ypos_):
    ypos ypos_
    pause (driving_dur + delay)
    linear (credits_dur - driving_dur) ypos (ypos_+driving_scrolls_at-credits_size)

transform ed.car(delay, ypos_):
    zoom 0.5
    xpos 1.3
    # drive on to the screen quickly
    parallel:
        pause (delay + 2.0)
        linear 3.0 xpos 0.6
    # creep forward slowly during the credits
    parallel:
        pause (delay + 2.0 + 2.0)
        linear (credits_dur - driving_dur + 10) xpos 0.2
    # drive off the screen quickly
    parallel:
        pause (credits_dur - driving_dur + 9)
        linear 3.0 xpos -0.3
    # scroll up matching the terrain
    parallel:
        ed.driving_scroll(delay, ypos_)

image ed_car_ph = ParameterizedText(size=80, outlines=[(3, '#000', 0, 0)], xalign=0.5)
define ed_car_ph_text = """            ____________________\n          /                                 \\\n  ____/                                     \\\n/ o o                                          \\\n________PLACEHOLDER CAR______\n          \___/                   \___/"""
label ed.driving(delay):
    call fx.bgloop_x('ed_bg_driving', dur=4.0, transform_=ed.driving_scroll(delay, ypos_=0.5))
    show linda smile              at fx.xoffset(-150), ed.car(delay, ypos_=0.95)
    show usagi postgrad happy 1   at fx.xoffset(-100), ed.car(delay, ypos_=0.95)
    show takeshi postgrad happy 1 at fx.xoffset( 100), ed.car(delay, ypos_=0.95)
    show sanders postgrad happy   at fx.xoffset( 200), ed.car(delay, ypos_=0.95)
    show ed_car_ph ed_car_ph_text at fx.xoffset(0), ed.car(delay, ypos_=1.00):
        anchor (0.5, 1.0)
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
