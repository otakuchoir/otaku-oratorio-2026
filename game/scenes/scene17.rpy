# https://otaku-oratorio-2026-gallery.netlify.app/?t=kohei&t=bg
label scene17:
    # start with bart in a dark room
    scene bg black
    show bart neutral focus at right2
    with dissolve
    pause 2

    # bart turns on the tv
    show bg spaceship window as tv:
        anchor (0.5, 1.0)
        zoom 0.2
        left2
    show fx_crt_scanlines as tv2:
        anchor (0.5, 1.0)
        zoom 0.2
        left2
    with dissolve
    "CLASSIFIED FOOTAGE... EDEN BLACK BOX"
    "THE TRUTH OF THAT DAY"
    
    # transition to the tv
    # crt effect makes everything darker... but this scene's characters and
    # background are already very dark! so, make them brighter.
    scene bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    # scene bg spaceship window
    show layer master at fx.flashback
    show gunner at left, flip
    show officer at right, noflip 
    show navigator at right2, noflip 
    show kohei neutral at left2
    # show kohei neutral at left2:
        # matrixcolor BrightnessMatrix(0.1)
    with irisout

    # > 17       INT. TV SCREENS                                                          17
    # > CLASSIFIED FOOTAGE... EDEN BLACK BOX... THE TRUTH OF THAT DAY
    gunner "You ready for this?"
    kitadani "I have a kid back home. Let’s get this over with so I can go see her."
    officer "Aye Captain."
    scene bg black with dissolve
    return