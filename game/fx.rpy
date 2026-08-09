
transform fx.hop(duration=0.3, y=50):
    ypos ypos_textbox
    easein (duration/2) ypos (ypos_textbox - y)
    easeout (duration/2) ypos ypos_textbox

define angle_bow = -15
transform fx.bowdown(duration, y, a=angle_bow):
    transform_anchor True
    yoffset 0
    rotate 0
    linear duration yoffset y rotate a
transform fx.bowup(duration, y, a=angle_bow):
    transform_anchor True
    yoffset y
    rotate a
    linear duration yoffset 0 rotate 0