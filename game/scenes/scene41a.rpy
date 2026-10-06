define ed_credits_text = credits_text(renpy.open_file('images/credits-20260928.md').read().decode('utf-8'))
define lines_per_screen = 35.0
# estimate length of the credits, to determine scroll speed
define credits_text_wrap = 60.0  # approximate word wrap line size. actual word wrap is handled by renpy
define credits_text_lines_nowrap = len([l for l in ed_credits_text.split('\n')])
define credits_text_lines = sum([
    max(1, math.ceil(len(str(l)) / credits_text_wrap))
    for l in ed_credits_text.split('\n')
    ])
define credits_text_size = float(credits_text_lines) / lines_per_screen

# define credits_size = 8.0
# empty starting screen, empty ending screen
define credits_size = credits_text_size + 2.0
define driving_scrolls_size = credits_size - 1.0
define driving_leaves_size = driving_scrolls_size + 0.5
# we're singing "welcome to the new world" here, so duration should be a bit longer than that.
# but... that's so slow during dev. lines below speed things up for dev
# define driving_scrolls_dur = 10
#
# Welcome To the New World is 3:31 = 180 + 31 = 211 seconds. driving should start scrolling right at the end of that
# https://drive.google.com/drive/folders/1Qku19Yo1G2XxDiu4NmdUiW_spwPMx6mh
define driving_scrolls_dur = 211
define driving_leaves_dur = int(driving_leaves_size / driving_scrolls_size * driving_scrolls_dur)
define credits_dur = int(credits_size / driving_scrolls_size * driving_scrolls_dur)
define dur_per_screen = driving_scrolls_dur / driving_scrolls_size
define owari_pause_dur = -dur_per_screen * 0.5
define owari_dur = dur_per_screen
define roxbury_pause_dur = owari_pause_dur + dur_per_screen + 2.5
define roxbury_dur = dur_per_screen / 2.0

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

    call fx.log("you're done! awesome work! now, hands off during the credits.")
    call fx.log(f"credits lines: {credits_text_lines}, screens: {credits_size}, nowrap: {credits_text_lines_nowrap}")
    
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
        # c = c+'\n\n'
    #show bg_credits_qrcode:
    #    anchor (0.5, 0.0)
    #    pos (0.25, 1.0)
    #    size (1440.0/4, 1440.0/4)
    #    pause dur_per_screen * 1.39
    #    linear dur_per_screen * 2.0 ypos -1.0
    #show github_qrcode:
    #    anchor (0.5, 0.0)
    #    pos (0.25, 1.0)
    #    size (1440.0/4, 1440.0/4)
    #    pause dur_per_screen * 5.731
    #    linear dur_per_screen * 2.0 ypos -1.0
    show ed_text "{font=[jpfont]}{color=#fff}{size=160}おわり{/size}\n{size=60}The end{/size}{/color}{/font}" as owari at truecenter:
        pos (0.5, 1.5)
        anchor (0.5, 0.5)
        pause credits_dur + owari_pause_dur
        linear owari_dur ypos 0.5
    #call roxbury
    #show layer roxbury:
    #    alpha 0.0
    #    anchor (0.5, 0.5)
    #    zoom 0.5
    #    pos (0.5, 1.5)
    #    pause credits_dur + roxbury_pause_dur
    #    alpha 1.0
    #    linear roxbury_dur ypos -0.5

    pause 30
    call fx.bgloop_x('bg jersey city cityscape', dur=4.0, transform_=ed.bg_scroll(-30.0, ypos_=0.0))
    with dissolve # +0.5 sec
    pause 29.5
    call fx.bgloop_x('bg alpine landscape', dur=4.0, transform_=ed.bg_scroll(-60.0, ypos_=0.0))
    with dissolve # +0.5 sec
    pause 29.5
    call fx.bgloop_x('bg countryside landscape', dur=4.0, transform_=ed.bg_scroll(-90.0, ypos_=0.0))
    with dissolve # +0.5 sec
    pause 29.5
    call fx.bgloop_x('bg forest landscape', dur=4.0, transform_=ed.bg_scroll(-120.0, ypos_=0.0))
    with dissolve # +0.5 sec
    pause 29.5
    call fx.bgloop_x('bg desert landscape', dur=4.0, transform_=ed.bg_scroll(-150.0, ypos_=0.0))
    with dissolve # +0.5 sec
    pause 29.5
    call fx.bgloop_x('bg countryside sunset', dur=4.0, transform_=ed.bg_scroll(-180.2, ypos_=0.0))
    with dissolve # +0.5 sec
    # not sure where the extra 0.1 comes from, but it needs to be in the last background change for correct timing
    #pause 24.5
    #call fx.bgloop_x('bg countryside', dur=4.0, transform_=ed.bg_scroll(-20.1, ypos_=0.0))
    #with dissolve
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

transform ed.bg_scroll(delay, ypos_):
    screen_size
    ed.driving_scroll(delay, ypos_)

transform ed.driving_scroll(delay, ypos_):
    ypos ypos_
    pause (driving_scrolls_dur + delay)
    linear (credits_dur - driving_scrolls_dur) ypos (ypos_+driving_scrolls_size-credits_size)

transform ed.car(delay, ypos_, zoom_=0.3):
    subpixel True
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
    call fx.bgloop_x('bg countryside', dur=4.0, transform_=ed.bg_scroll(delay, ypos_=0.0))
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

init -1 python:
    import math
    import re
    def credits_text(c: str) -> Text:
        # skip the first few lines describing the file to humans
        c ='\n'.join(c.splitlines()[5:])
        c = markdown_to_renpy(c)
        # c = c.replace('[Background Image Credits](https://docs.google.com/spreadsheets/d/1Fh0YKSAyx_duHP-MNdtIQqkaKUC9Tv9ZExgeEPl63Ww/edit?usp=drive_link)', '\n'*15+'Background Image Credits')
        c = c.replace('{b}No generative AI was used to create this show.{/b}', '{b}Visual novel source code{/b}\nhttps://github.com/otakuchoir/otaku-oratorio-2026\n\n' + '{b}No generative AI was used to create this show.{/b}')
        # return Text(c, text_align=0.5)
        return c

    def markdown_to_renpy(t) -> str:
        t = re.sub(r'\*\*\*(?P<body>[^\*]*)\*\*\*', r'{b}{i}\g<body>{/i}{/b}', t)
        t = re.sub(r'\*\*(?P<body>[^\*]*)\*\*', r'{b}\g<body>{/b}', t)
        t = re.sub(r'\*(?P<body>[^\*]*)\*', r'{i}\g<body>{/i}', t)
        t = re.sub(r'~~(?P<body>[^\~]*)~~', r'{s}\g<body>{/s}', t)
        t = re.sub(r'\\-', r'-', t)
        t = re.sub(r'\\#', r'#', t)
        t = re.sub(r'\\!', r'!', t)
        t = re.sub(r'\\\)', r'\)', t)
        t = re.sub(r'\\<[Yy]our [Nn]ame [Hh]ere\\>\n', r'', t)
        return t

# thanks, https://scanqr.org/qr-code-generator/#link
image bg_credits_qrcode = 'images/bg_credits_qrcode.png'
image github_qrcode = 'images/github_qrcode.png'
