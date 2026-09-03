image roxbury = Movie(play="images/roxbury.webm", loops=-1)
init python:
    renpy.add_layer('roxbury', above='master')

label animation_test_roxbury:
    show bg beige
    "what is love"

    $ roxz = 0.5
    show roxbury at truecenter:
        # DURATION        : 00:00:00.480000000
        zoom roxz * 1440.0/498.0
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    "baby don't hurt me"

    hide roxbury # reset for gif timing

    call roxbury
    show layer roxbury:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom roxz
    "don't hurt me"

    # scene layer "roxbury"
    $ renpy.scene(layer="roxbury")
    "no more"

    return

label roxbury:
    show roxbury onlayer roxbury at truecenter:
        # DURATION        : 00:00:00.480000000
        zoom 1440.0/498.0
        anchor (0.5, 0.5)
        pos (0.5, 0.5)

    $ opacity = 1.0
    $ sanders_head_crop = 0.52
    show sanders postgrad smug focus onlayer roxbury as sanders_body:
        crop (0.0, sanders_head_crop, 1.0, 1.0-sanders_head_crop)
        flip
        zoom 1.37
        alpha opacity
        anchor (0.5, 1.0)
        block:
            pos (0.45, 0.72)
            easein 0.3 pos (0.45, 0.74)
            linear 0.18 pos (0.45, 0.72)
            repeat
    show sanders postgrad smug focus onlayer roxbury as sanders_head:
        crop (0.0, 0.0, 1.0, sanders_head_crop)
        flip
        zoom 1.37
        alpha opacity
        anchor (0.5, 0.0)
        block:
            pos (0.4, 0.155)
            easein 0.38 pos (0.5, 0.175)
            linear 0.10 pos (0.4, 0.155)
            repeat

    show takeshi postgrad happy 2 focus onlayer roxbury:
        crop (0.0, 0.0, 1.0, 0.7)
        flip
        zoom 1.42
        alpha opacity
        anchor (0.5, 1.0)
        transform_anchor True
        block:
            rotate 0
            pos (0.8, 0.61)
            easein 0.38 rotate 5 pos (0.8, 0.65) 
            # ease 0.10 rotate 3 pos (0.8, 0.63) 
            # easein 0.28 rotate 5 pos (0.8, 0.65) 
            linear 0.10 rotate 0 pos (0.8, 0.61) 
            repeat

    $ usagi_head_crop = 0.61
    show usagi postgrad smug focus onlayer roxbury as usagi_body:
        crop (0.0, usagi_head_crop, 1.0, 1.0-usagi_head_crop)
        noflip
        zoom 1.52
        alpha opacity
        anchor (0.5, 1.0)
        parallel:
            pos (0.15, 0.70)
            easein 0.38 pos (0.15, 0.72)
            linear 0.10 pos (0.15, 0.70)
            repeat
        parallel:
            "usagi postgrad happy 3"
            pause 0.1
            "usagi postgrad smug"
            pause 0.33
            "usagi postgrad happy 3"
            pause 0.05
            repeat
    show usagi postgrad smug focus onlayer roxbury as usagi_head:
        crop (0.0, 0.0, 1.0, usagi_head_crop)
        noflip
        zoom 1.52
        alpha opacity
        anchor (0.5, 1.0)
        transform_anchor True
        parallel:
            rotate -15
            pos (0.15, 0.61)
            easein 0.33 rotate 15 pos (0.15, 0.65)
            linear 0.15 rotate -15 pos (0.15, 0.61)
            repeat
        parallel:
            "usagi postgrad happy 3"
            pause 0.1
            "usagi postgrad smug"
            pause 0.28
            "usagi postgrad happy 3"
            pause 0.1
            repeat
    return