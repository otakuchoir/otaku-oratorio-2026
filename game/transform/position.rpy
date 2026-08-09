# redefine builtin positions so the bottom edge of our sprites is sitting on top of the textbox.
define ypos_textbox = 880

# usually I like using namespaces, but some of these deliberately override builtin positions
transform ytextbox:
    ypos ypos_textbox
    yanchor 1.0

transform offscreenleft:
    xalign -0.6
    ytextbox
transform left:
    xalign 0.0
    ytextbox
transform left2:
    xalign 0.25
    ytextbox
transform center:
    xalign 0.5
    ytextbox
transform right2:
    xalign 0.75
    ytextbox
transform right:
    xalign 1.0
    ytextbox
transform offscreenright:
    xalign 1.6
    ytextbox

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