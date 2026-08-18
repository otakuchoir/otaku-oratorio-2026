
label scene17:
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