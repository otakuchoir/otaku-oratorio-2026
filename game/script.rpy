# Evan is learning/practicing ren'py here. Not used in the real performance.

# character lists are used for speaking
# color is their text color
# renpy does some fancy stuff with image tags that I haven't sorted out just yet, and it depends on the image= argument
define usagi = Character("Usagi", color="#fd7979", image="usagi")
define takeshi = Character("Takeshi", color="#44bbff", image="takeshi")
define sanders = Character("Sanders", color="#00ff00", image="sanders")
define kelisha = Character("Kelisha", color="#0000ff", image="kelisha")

# special effects! Let's highlight the speaker by dimming all non-speaking characters.
transform dim:
    matrixcolor BrightnessMatrix(-0.25)

# no-op?! because ren'py keeps old transforms around unless you replace them.
# I tried this first, and it does not work: 
#     show takeshi-happy-1 at right, dim
#     show takeshi-happy-1 at right   # it's still dim!
# instead, this works:
#     show takeshi-happy-1 at right, dim
#     show takeshi-happy-1 at right, nodim   # highlighted!
transform nodim:
    matrixcolor BrightnessMatrix(0)

# some flashier special effects, just to see what's possible. ATL transforms
transform slide_left:
    # slide from right to left. 1.0 is right side of the screen, 0.0 is the left
    xalign 1.4
    linear 1.0 xalign -0.4
transform blink:
    # transforms can reference other transforms!
    dim
    linear 0.1 nodim
    linear 0.1 dim
    # and they can loop!
    repeat

# associating an image with a character opens up a lot of possibilites in ren'py.
# but images named with dashes aren't automatically associated. do it by hand.
# also, use image attributes to automate speaker spotlighting!
image usagi hello:
    'usagi-hello'
    dim
image usagi hello spotlight = 'usagi-hello'
image takeshi happy:
    'takeshi-happy-1'
    dim
image takeshi happy spotlight = 'takeshi-happy-1'
image sanders neutral:
    'sanders-neutral'
    dim
image sanders neutral spotlight = 'sanders-neutral'
image kelisha stinkeye = 'kelisha-stinkeye'
image kelisha stinkeye spotlight = 'kelisha-stinkeye'

init python:
    config.speaking_attribute = 'spotlight'
#transform autospotlight:
#    on spotlight:
#        linear 0.2 nodim
#    on idle:
#        linear 0.2 dim

# finally, dialogue
label start:
label test_scene:
    # scene bg room

    # this works for highlighting the speaker, but it's very tedious.
    # surely we can automate it somehow...
    #show usagi hello at center, nodim
    #show takeshi happy at right, dim
    #show sanders neutral at left, dim
    #usagi "🐇"
    #show usagi hello at center, dim
    #show takeshi happy at right, nodim
    #takeshi "🚕"
    #show takeshi happy at right, dim
    #show sanders-neutral at left, nodim
    #sanders "🍗" with vpunch
    #show sanders neutral at left, dim

    # yes we can automate it!
    show usagi hello at center
    show takeshi happy at right
    show sanders neutral at left
    usagi "🐇"
    takeshi "🚕"
    sanders "🍗" with vpunch
    show kelisha stinkeye at offscreenleft, blink, slide_left
    kelisha "🚨"