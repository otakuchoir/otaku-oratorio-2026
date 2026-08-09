image bg default = Solid("#ccc")
image bg black = Solid('#000')
image bg white = Solid('#fff')
image bg red = Solid('#f00')

transform flip:
    xzoom -1
transform noflip:
    xzoom 1
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

transform hvibrate:
    xoffset 0
    easein 0.02 xoffset 10
    ease 0.04 xoffset -10
    repeat

transform fx.hop(dur=0.3, y=50):
    ypos ypos_textbox
    easein (dur/2) ypos (ypos_textbox - y)
    easeout (dur/2) ypos ypos_textbox

define angle_bow = -15
transform fx.bowdown(dur, y, a=angle_bow):
    transform_anchor True
    yoffset 0
    rotate 0
    linear dur yoffset y rotate a
transform fx.bowup(dur, y, a=angle_bow):
    transform_anchor True
    yoffset y
    rotate a
    linear dur yoffset 0 rotate 0
transform fx.stretch0(x, y):
    xzoom x yzoom y
transform fx.stretch(dur, x, y):
    ease dur xzoom x yzoom y
