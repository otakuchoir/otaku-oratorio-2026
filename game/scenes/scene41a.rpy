define credits_size = 6.5
define driving_scrolls_size = 5.5
define driving_leaves_size = 6.0
# TODO: we're singing "welcome to the new world" here, so duration should be a bit longer than that.
# but... that's so slow during dev.
# define driving_scrolls_dur = driving_scrolls_size * 4.0
# define driving_scrolls_dur = driving_scrolls_size * 8.0
#
# Welcome To the New World is 3:31 = 180 + 31 = 211 seconds. driving should start scrolling right at the end of that
# https://drive.google.com/drive/folders/1Qku19Yo1G2XxDiu4NmdUiW_spwPMx6mh
define driving_scrolls_dur = 211
define driving_leaves_dur = int(driving_leaves_size / driving_scrolls_size * driving_scrolls_dur)
define credits_dur = int(credits_size / driving_scrolls_size * driving_scrolls_dur)
define roxbury_pause_dur = 5
define roxbury_dur = 15

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
    call fx.log("paused - start the credits once Welcome to the New World starts")
    pause

    call fx.log("you're done! awesome work! now, hands off during the credits. wait for the post-credits scene")
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
    # show expression ed_credits_text behind bgloop_x_0, bgloop_x_1:
    show ed_text ed_credits_text:
        anchor (0.5, 0.0)
        # pos (0.5, -2.0)
        pos (0.25, 1.0)
        linear credits_dur ypos (1.0-credits_size)
    
    call roxbury
    show layer roxbury:
        alpha 0.0
        anchor (0.5, 0.5)
        zoom 0.5
        pos (0.5, 1.5)
        pause credits_dur + roxbury_pause_dur
        alpha 1.0
        linear roxbury_dur ypos -0.5

    pause 10
    call fx.bgloop_x('bg jersey city cityscape', dur=4.0, transform_=ed.driving_scroll(-10.0, ypos_=0.0))
    with dissolve # +0.5 sec
    pause 9.5
    # not sure where the extra 0.1 comes from, but it needs to be in the last background change for correct timing
    call fx.bgloop_x('bg countryside', dur=4.0, transform_=ed.driving_scroll(-20.1, ypos_=0.0))
    with dissolve
    pause
    pause
    pause
    return

style ed_text_s:
    xalign 0.5
    size 24
    textalign 0.5
    outlines [(2, '#000', 0, 0)]
    xsize 0.5
image ed_text = ParameterizedText(style='ed_text_s')

# image ed_bg_driving = Transform(Composite(
#     (1440*2, 1080),
#     (0, 0), 'bg countryside',
#     (1440, 0), Transform('bg countryside', xzoom=-1),
# ), zoom=0.5)

transform ed.driving_scroll(delay, ypos_):
    ypos ypos_
    pause (driving_scrolls_dur + delay)
    linear (credits_dur - driving_scrolls_dur) ypos (ypos_+driving_scrolls_size-credits_size)

transform ed.car(delay, ypos_, zoom_=0.3):
    zoom zoom_
    xpos 1.3
    # drive on to the screen quickly
    parallel:
        pause (delay + 2.0)
        linear 3.0 xpos 0.6
    # creep forward slowly during the credits
    parallel:
        pause (delay + 2.0 + 2.0)
        linear (driving_leaves_dur+1) xpos 0.4
    # drive off the screen quickly
    parallel:
        pause driving_leaves_dur
        linear 3.0 xpos -0.6
        alpha 0.0
    # scroll up matching the terrain
    parallel:
        ed.driving_scroll(delay, ypos_)

# image ed_car_ph = ParameterizedText(size=80, outlines=[(3, '#000', 0, 0)], xalign=0.5)
# define ed_car_ph_text = """            ____________________\n          /                                 \\\n  ____/                                     \\\n/ o o                                          \\\n________PLACEHOLDER CAR______\n          \___/                   \___/"""

# https://pixabay.com/vectors/automobile-car-gs-1300464/
image ed_car = "images/automobile-1300464_1280.png"

label ed.driving(delay):
    # call fx.bgloop_x('ed_bg_driving', dur=4.0, transform_=ed.driving_scroll(delay, ypos_=0.5))
    call fx.bgloop_x('bg countryside', dur=4.0, transform_=ed.driving_scroll(delay, ypos_=0.0))
    show linda smile              at fx.xoffset(-50), ed.car(delay, ypos_=0.84)
    show usagi postgrad happy 1   at fx.xoffset(10), ed.car(delay, ypos_=0.84)
    show takeshi postgrad happy 1 at fx.xoffset(140), ed.car(delay, ypos_=0.86)
    show sanders postgrad happy   at fx.xoffset(220), ed.car(delay, ypos_=0.86)
    show ed_car:
        flip
        anchor (0.5, 1.0)
        fx.xoffset(0)
        ed.car(delay, ypos_=1.06, zoom_=0.65)
    # show ed_car_ph ed_car_ph_text at fx.xoffset(0), ed.car(delay, ypos_=1.00):
        # anchor (0.5, 1.0)
    return

init python:
    import re
    def credits_text(c: str) -> Text:
        # skip the first few lines describing the file to humans
        c ='\n'.join(c.splitlines()[5:])
        c = markdown_to_renpy(c)
        c = "TODO: credits work in progress. final ones will be much slower, same duration as Welcome to the New World, and hopefully have more backgrounds\n\n"+c
        # NOPE renpy's default font does not support japanese, gotta find and use one that does for this
        # c = c+'\n\nおわり'
        # return Text(c, text_align=0.5)
        return c

    def markdown_to_renpy(t) -> str:
        t = re.sub(r'\*\*\*(?P<body>[^\*]*)\*\*\*', r'{b}{i}\g<body>{/i}{/b}', t)
        t = re.sub(r'\*\*(?P<body>[^\*]*)\*\*', r'{b}\g<body>{/b}', t)
        t = re.sub(r'\*(?P<body>[^\*]*)\*', r'{i}\g<body>{/i}', t)
        t = re.sub(r'~~(?P<body>[^\~]*)~~', r'{s}\g<body>{/s}', t)
        t = re.sub(r'\\-', r'-', t)
        t = re.sub(r'\\#', r'#', t)
        t = re.sub(r'\\<[Yy]our [Nn]ame [Hh]ere\\>\n', r'', t)
        return t

define ed_credits_text = credits_text(renpy.open_file('images/credits-20260902.md').read().decode('utf-8'))
