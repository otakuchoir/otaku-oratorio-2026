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
    show huxtable neutral at left, flip as gunner:
        matrixcolor BrightnessMatrix(-1)
    show huxtable neutral at right, noflip as officer:
        matrixcolor BrightnessMatrix(-1)
    show kohei neutral at center:
        matrixcolor BrightnessMatrix(0.1)
    show fx_crt_scanlines
    with irisout

    # > 17       INT. TV SCREENS                                                          17
    # > CLASSIFIED FOOTAGE... EDEN BLACK BOX... THE TRUTH OF THAT DAY
    show huxtable neutral focus as gunner
    gunner "You ready for this?"
    show huxtable neutral as gunner
    kitadani "I have a kid back home. Let’s get this over with so I can go see her."
    show huxtable neutral focus as officer
    officer "Aye Captain."
    show huxtable neutral as officer
    scene bg black with dissolve
    return