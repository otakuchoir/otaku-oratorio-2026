# Evan is learning/practicing ren'py here. Not used in the real performance.

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

label test_scene:
    # scene bg room
    show usagi happy1 at center, dim
    show takeshi happy1 at right, dim
    show sanders happy at left, dim

    $ config.speaking_attribute = None
    "Evan is learning ren'py in this scene. It won't be used in the performance, of course."
    show usagi at center, nodim
    usagi "at-transforms are one way to highlight the speaking character."
    show usagi at center, dim
    show takeshi at right, nodim
    takeshi "it works, and it's pretty simple."
    show takeshi at right, dim
    show sanders angry1 at left, nodim
    sanders "tedious, though. very verbose. easy to mess up."
    show sanders at left, dim
    # narrator/no speaker
    "surely there's a better way?"
    # hide and re-show to remove all old transforms
    hide usagi
    hide takeshi
    hide sanders

    $ config.speaking_attribute = '-dim'
    show usagi happy1 dim at center
    show takeshi happy1 dim at right
    show sanders happy dim at left
    usagi "speaking_attribute is a lot shorter!"
    takeshi "it takes a lot more setup. every sprite needs a \"dim\" attribute."
    sanders "and I haven't yet got it working with layered images or arbitrary transforms."
    usagi hello dim "but once it's set up, it seems to work well"
    "narrator speech doesn't highlight any characters"

    show kelisha stinkeye at offscreenleft, blink, slide_left
    kelisha "let's try some animation!"