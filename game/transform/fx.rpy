image bg default = Solid("#ccc")
image bg black = Solid('#000')
image bg white = Solid('#fff')
image bg red = Solid('#f00')
image bg beige = Solid("#e7dbc7")
image bg neongreen = Solid("#0fff50")
image bg linda hits = Solid(color_linda)
image bg bart hits = Solid(color_bart)
image bg queen hits = Solid(color_queen)
image bg kelisha hits = Solid(color_kelisha)

transform flip:
    xzoom -1.0
transform noflip:
    xzoom 1.0
transform nozoom:
    zoom 1.0

transform yflip:
    yzoom -1.0
transform noyflip:
    yzoom 1.0

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

transform fx.ease_pos(dur=1.0, xy0=(0, 880.0/1080.0), xy1=(0, 880.0/1080.0)):
    pos xy0
    ease dur pos xy1
transform fx.ease_xyoffset(dur=1.0, xy0=(0, 0), xy1=(0, 0)):
    xoffset xy0[0]
    yoffset xy0[1]
    ease dur xoffset xy1[0] yoffset xy1[1]

label fx.play_music_in_dev(f):
    $ if config.developer: renpy.music.play(f)
    return
label fx.play_music_if_changed_in_dev(f):
    $ if config.developer: renpy.music.play(f, if_changed=True)
    return

transform fx.hover(dur=2.0, loops=None, y0=0, dy=50):
    # Start hovering, initializing the start location
    # yoffset y0
    fx.hovering(dur=dur, loops=loops, y0=y0, dy=dy)

transform fx.hovering(dur=2.0, loops=None, y0=0, dy=50):
    animation
    # Continue hovering after an earlier fx.hover(), without initializing the start location
    easein  dur/4 yoffset y0+dy
    easeout dur/4 yoffset y0
    easein  dur/4 yoffset y0-dy
    easeout dur/4 yoffset y0
    repeat loops

#transform fx.hover_xoffset(hdur=2.0, xdur=1.0, x0=0, x1=0, loops=None, y0=0, dy=50):
#    parallel:
#        fx.hovering(dur=hdur, loops=loops, y0=y0, dy=dy)
#    parallel:
#        fx.ease_xoffset(dur=xdur, x0=x0, x1=x1)

transform fx.flashback():
    #matrixcolor SepiaMatrix()
    # no, this removes all color. I want partial color!
    #
    # docs say sepiamatrix is equivalent to:
    # matrixcolor TintMatrix('#ffeec2') * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
    # so we copy and modify that:
    matrixcolor TintMatrix('#ffeec2') * SaturationMatrix(0.15, (0.2126, 0.7152, 0.0722))

transform fx.bgloop0:
    anchor (0.0, 0.0)
    pos (0.0, 0.0)

label fx.bgloop_x_hide:
    hide bgloop_x_0
    hide bgloop_x_1
    return

transform fx.noop:
    pass

label fx.bgloop_x(img, dur, transform_=None):
    # mirror the background for a cleanish-looking loop point
    show expression img as bgloop_x_0 at fx.bgloop0
    show expression img as bgloop_x_1 at fx.bgloop0

    python:
        xdur = dur
        x, y, w, h = renpy.get_image_bounds('bgloop_x_0')
        if xdur < 0:
            xdur = -xdur
            w = -w
        transform_ = transform_ if transform_ is not None else fx.noop
    show expression img as bgloop_x_0:
        parallel:
            transform_
        parallel:
            xoffset 0
            linear xdur xoffset w
            xoffset -w
            linear xdur xoffset 0
            repeat
    show expression img as bgloop_x_1:
        flip
        parallel:
            transform_
        parallel:
            xoffset -w
            linear xdur xoffset 0
            linear xdur xoffset w
            repeat
    return

label fx.bgloop_hide:
    hide bgloop_00
    hide bgloop_01
    hide bgloop_10
    hide bgloop_11
    return

label fx.bgloop(img, dur):
    # mirror the background for a cleanish-looking loop point
    show expression img as bgloop_00 at fx.bgloop0
    show expression img as bgloop_10 at fx.bgloop0
    show expression img as bgloop_01 at fx.bgloop0
    show expression img as bgloop_11 at fx.bgloop0

    python:
        xdur, ydur = dur
        x, y, w, h = renpy.get_image_bounds('bgloop_00')
        if xdur < 0:
            xdur = -xdur
            w = -w
        if ydur < 0:
            ydur = -ydur
            h = -h
    show expression img as bgloop_00:
        parallel:
            xoffset 0
            linear xdur xoffset w
            xoffset -w
            linear xdur xoffset 0
            repeat
        parallel:
            yoffset 0
            linear ydur yoffset h
            yoffset -h
            linear ydur yoffset 0
            repeat
    show expression img as bgloop_01:
        flip
        parallel:
            xoffset -w
            linear xdur xoffset 0
            linear xdur xoffset w
            repeat
        parallel:
            yoffset 0
            linear ydur yoffset h
            yoffset -h
            linear ydur yoffset 0
            repeat
    show expression img as bgloop_10:
        yflip
        parallel:
            xoffset 0
            linear xdur xoffset w
            xoffset -w
            linear xdur xoffset 0
            repeat
        parallel:
            yoffset -h
            linear ydur yoffset 0
            linear ydur yoffset h
            repeat
    show expression img as bgloop_11:
        flip
        yflip
        parallel:
            xoffset -w
            linear xdur xoffset 0
            linear xdur xoffset w
            repeat
        parallel:
            yoffset -h
            linear ydur yoffset 0
            linear ydur yoffset h
            repeat
    return
