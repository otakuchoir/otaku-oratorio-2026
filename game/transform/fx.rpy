image bg default = Solid("#ccc")
image bg black = Solid('#000')
image bg white = Solid('#fff')
image bg red = Solid('#f00')
image bg beige = Solid("#e7dbc7")
image bg neongreen = Solid("#0fff50")

transform flip:
    xzoom -1.0
transform noflip:
    xzoom 1.0
transform nozoom:
    zoom 1.0

transform yshake(size, n, dur):
    yoffset 0
    ease dur yoffset size
    easeout dur yoffset 0
    easein dur yoffset -size
    ease dur yoffset 0
    repeat n

transform blinkon:
    matrixcolor BrightnessMatrix(0.65)
    # zoom 0.97
transform blinkoff:
    matrixcolor BrightnessMatrix(0)
    # zoom 1
transform blink(n, dur):
    blinkoff
    linear dur blinkon
    linear dur blinkoff
    repeat n

transform smoothzoom:
    ease 0.4 zoom 1

transform hvibrate(n=None):
    xoffset 0
    easein 0.02 xoffset 10
    ease 0.04 xoffset -10
    repeat n

transform fx.hop(dur=0.3, y=50):
    yoffset 0
    # yanchor 1
    xanchor 0.5
    easein (dur/2) yoffset -y
    easeout (dur/2) yoffset 0
transform fx.hopN(dur=(0.1, 0.3), y=50, stretch=(0.2, 0.3), n=1, flip=False):
    yoffset 0
    # yanchor 1
    xanchor 0.5
    fx.stretch(1, 1, flip=flip)
    block:
        # squash down in anticipation
        easein dur[0]/2 fx.stretch(1 + stretch[0], 1 - stretch[0], flip=flip)
        easeout dur[0]/2 fx.stretch(1, 1, flip=flip)
        # hop, along with a stretch upward
        easein (dur[1]/2) fx.stretch(1 - stretch[1], 1 + stretch[1], flip=flip) yoffset -y
        easeout (dur[1]/2) fx.stretch(1, 1, flip=flip) yoffset 0
        repeat n
    # squash down on landing
    easein dur[0]/2 fx.stretch(1 + stretch[0], 1 - stretch[0], flip=flip)
    easeout dur[0]/2 fx.stretch(1, 1, flip=flip)

define angle_bow = -15
transform fx.bowdown(dur, a=angle_bow, y=abs(a)*2):
    transform_anchor True
    yoffset 0
    rotate 0
    ease dur yoffset y rotate a
transform fx.bowup(dur, a=angle_bow, y=abs(a)*2):
    transform_anchor True
    yoffset y
    rotate a
    ease dur yoffset 0 rotate 0
transform fx.stretch(x, y, flip=False):
    xzoom (-x if flip else x)
    yzoom y

# transform fx.glitch_child:
label fx.glitch_child:
    show child:
        flip
        parallel:
            "child faceless focus"
            pause 0.05
            "child glitch focus"
            pause 0.05
            "child faceless focus"
            pause 0.05
            "child glitch 2 focus"
            pause 0.05
            repeat 3
        parallel:
            yshake(20, 15, 0.01)
    pause 0.6
    return

transform fx.glitch_lights:
    # matrixcolor BrightnessMatrix(0)
    matrixcolor BrightnessMatrix(0.5)
    pause 0.1
    matrixcolor BrightnessMatrix(0)
    pause 0.1
    matrixcolor BrightnessMatrix(-0.5)
    pause 0.1
    matrixcolor BrightnessMatrix(0)
    repeat 2

transform fx.xoffset(x=0):
    xoffset x
transform fx.xpos(x=0):
    xpos x
transform fx.yoffset(y=0):
    yoffset y
transform fx.ypos(y=0):
    ypos y

transform fx.ease_xoffset(dur=1.0, x0=0, x1=0):
    fx.xoffset(x0)
    ease dur fx.xoffset(x1)
transform fx.ease_xpos(dur=1.0, x0=0, x1=0):
    fx.xpos(x0)
    ease dur fx.xpos(x1)
transform fx.ease_yoffset(dur=1.0, y0=0, y1=0):
    fx.yoffset(y0)
    ease dur fx.yoffset(y1)
transform fx.ease_ypos(dur=1.0, y0=880.0/1080.0, y1=880.0/1080.0):
    fx.ypos(y0)
    ease dur fx.ypos(y1)

label fx.play_music_in_dev(f):
    $ if config.developer: renpy.music.play(f)
    return
label fx.play_music_if_changed_in_dev(f):
    $ if config.developer: renpy.music.play(f, if_changed=True)
    return

transform fx.hover(dur=2.0, y0=0, dy=50):
    yoffset y0
    easein  dur/4 yoffset y0+dy
    easeout dur/4 yoffset y0
    easein  dur/4 yoffset y0-dy
    easeout dur/4 yoffset y0
    repeat