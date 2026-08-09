# redefine builtin positions so the bottom edge of our sprites is sitting on top of the textbox.
# don't use yoffset, special effects use that for small adjustments relative to screen position
# ((x/y/"")pos is a float percent from 0.0-1.0; (x/y/"")offset is an integer number of pixels)
define ypos_textbox = 880.0/1080.0

# usually I like using namespaces, but some of these deliberately override builtin positions
transform ytextbox:
    ypos ypos_textbox

transform offscreenleft:
    xpos -0.6
    ytextbox
transform left:
    xpos 0.15
    ytextbox
transform left2:
    xpos 0.33
    ytextbox
transform center:
    xpos 0.5
    ytextbox
transform right2:
    xpos 0.67  # SIX SEVEN LOLOLOL
    ytextbox
transform right:
    xpos 0.85
    ytextbox
transform offscreenright:
    xpos 1.6
    ytextbox

# TODO: avoid changing sprite anchors, special effects rely on it
transform ytop:
    yanchor 0.0

transform topoffscreenleft:
    xalign -0.6
    ytop
transform topleft:
    xalign 0.0
    ytop
transform topleft2:
    xalign 0.25
    ytop
transform topcenter:
    xalign 0.5
    ytop
transform topright2:
    xalign 0.75
    ytop
transform topright:
    xalign 1.0
    ytop
transform topoffscreenright:
    xalign 1.6
    ytop

transform offscreentop:
    yalign -0.9
    xalign 0.5