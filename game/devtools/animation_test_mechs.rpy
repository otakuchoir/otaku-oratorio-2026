label mech_test:
    scene bg beige with fade
    show usagi postgrad mech neutral at left, fx.hover()
    show bart mech neutral at right2, fx.hover()
    "mechs 1"
    scene bg beige
    show usagi postgrad mech neutral flip at left, fx.hover()
    show bart mech neutral flip at right2, fx.hover()
    "mechs 1 flip"
    scene bg beige
    show usagi postgrad mech neutral focus at left, fx.hover()
    show bart mech neutral focus at right2, fx.hover()
    "mechs 1 focus"
    scene bg beige
    show usagi postgrad mech neutral flip focus at left, fx.hover()
    show bart mech neutral flip focus at right2, fx.hover()
    "mechs 1 flip focus"

    scene bg beige
    show linda mech neutral at left, fx.hover()
    show kohei mech neutral at center, fx.hover()
    show jojo mech neutral at right2, fx.hover()
    "mechs 2"
    scene bg beige
    show linda mech neutral flip at left, fx.hover()
    show kohei mech neutral flip at center, fx.hover()
    show jojo mech neutral flip at right2, fx.hover()
    "mechs 2 flip"
    scene bg beige
    show linda mech neutral focus at left, fx.hover()
    show kohei mech neutral focus at center, fx.hover()
    show jojo mech neutral focus at right2, fx.hover()
    "mechs 2 focus"
    scene bg beige
    show linda mech neutral flip focus at left, fx.hover()
    show kohei mech neutral flip focus at center, fx.hover()
    show jojo mech neutral flip focus at right2, fx.hover()
    "mechs 2 flip focus"

    scene bg beige
    show huxtable mech neutral at left, fx.hover()
    show sanders mech postgrad neutral at center, fx.hover()
    show takeshi mech postgrad neutral at right, fx.hover()
    "mechs 3"
    scene bg beige
    show huxtable mech neutral flip at left, fx.hover()
    show sanders mech postgrad neutral flip at center, fx.hover()
    show takeshi mech postgrad neutral flip at right, fx.hover()
    "mechs 3 flip"
    scene bg beige
    show huxtable mech neutral focus at left, fx.hover()
    show sanders mech postgrad neutral focus at center, fx.hover()
    show takeshi mech postgrad neutral focus at right, fx.hover()
    "mechs 3 focus"
    scene bg beige
    show huxtable mech neutral flip focus at left, fx.hover()
    show sanders mech postgrad neutral flip focus at center, fx.hover()
    show takeshi mech postgrad neutral flip focus at right, fx.hover()
    "mechs 3 flip focus"

    scene bg beige
    show queen mech neutral at left, fx.hover()
    show kelisha mech neutral at center, fx.hover()
    show child mech neutral at right, fx.hover()
    "mechs 4"
    scene bg beige
    show queen mech neutral flip at left2, fx.hover()
    show kelisha mech neutral flip at center, fx.hover()
    show child mech neutral flip at right, fx.hover()
    "mechs 4 flip"
    scene bg beige
    show queen mech neutral focus at left, fx.hover()
    show kelisha mech neutral focus at center, fx.hover()
    show child mech neutral focus at right, fx.hover()
    "mechs 4 focus"
    scene bg beige
    show queen mech neutral flip focus at left2, fx.hover()
    show kelisha mech neutral flip focus at center, fx.hover()
    show child mech neutral flip focus at right, fx.hover()
    "mechs 4 flip focus"

    scene bg beige
    show usagi mech focus as usagimech at left, fx.hover()
    show usagi postgrad neutral focus at left, fx.hover():
        zoom 0.5
        ypos 0.75
        xoffset -20
    show bart mech as bartmech at right2, fx.hover()
    show bart neutral at right2, fx.hover():
        zoom 0.5
        ypos 0.64
        xoffset 20
    with fade
    usagi "OLD mech layout A: pilot on chest. a little ugly, but the audience always knows who's driving which mech"

    scene bg beige
    show usagi mech focus as usagimech at left, fx.hover()
    show bg black as usagiscreen at left, fx.hover() behind usagi:
        anchor (0.5, 1.0)
        crop (0, 0, 140, 120)
        ypos 0.75
        xoffset 5
    show usagi postgrad neutral focus at left, fx.hover():
        zoom 0.4
        ypos 0.75
        xoffset -5
    show fx_crt_scanlines as usagicrt at left, fx.hover():
        anchor (0.5, 1.0)
        crop (0, 0, 140, 120)
        ypos 0.75
        xoffset 5
    with fade
    usagi "OLD mech layout B: pilot-screen on chest. it's a good idea! but my attempt at it is REALLY ugly. has potential with a better screen graphic, though. also, worried that the screen has to be pretty small to fit nicely"
    
    scene bg beige
    show usagi mech focus as usagimech at left, fx.hover()
    show bart mech at right2, fx.hover()
    with fade
    usagi postgrad neutral "OLD mech layout C: speaker portrait only. prettier, but the audience has already forgotten who's in the non-speaking mechs"

    scene bg beige
    show usagi postgrad neutral focus at left, fx.hover() behind usagimech:
        zoom 0.5
        ypos 0.48
        xoffset 0
    show usagi mech focus as usagimech at left, fx.hover()
    show bart neutral at right2, fx.hover():
        zoom 0.5
        ypos 0.33
        xoffset 70
    show bart mech as bartmech at right2, fx.hover()
    with fade
    usagi "OLD mech layout D: pilot rides on top. less ugly, and the audience always knows who's driving which mech. but how do they breathe in space...?"

    return