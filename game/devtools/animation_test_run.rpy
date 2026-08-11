label animation_test_run:
    scene bg black
    $ y = 0.2
    $ x0 = 0.2
    $ x1 = 1 - x0
    $ z = 0.5
    show usagi happy 2 focus as u1:
        xpos x0
        ypos y
        zoom z
        block:
            flip
            linear 2 xpos x1
            pause 0.5
            noflip
            linear 2 xpos x0
            pause 0.5
            repeat
    show text "simple linear motion" as t1 at center:
        ypos y

    $ y += 0.15
    show usagi happy 2 focus as u2:
        xpos x0
        ypos y
        zoom z
        block:
            flip
            ease 2 xpos x1
            pause 0.5
            noflip
            ease 2 xpos x0
            pause 0.5
            repeat
    show text "simple easing motion" as t2 at center:
        ypos y

    $ y += 0.15
    $ dx = 0.05
    $ at = 0.16
    $ mt = 1.0-at
    $ dz = 0.1
    show usagi happy 2 focus as u3:
        xpos x0
        ypos y
        zoom z
        fx.stretch(1, 1)
        block:
            flip
            easein  at xpos x0-dx fx.stretch(-(1.0-dz), 1.0+dz)
            easeout mt xpos 0.5   fx.stretch(-(1.0+dz), 1.0-dz)
            easein  mt xpos x1+dx fx.stretch(-(1.0-dz), 1.0+dz)
            easeout at xpos x1    fx.stretch(-(1.0), 1.0)
            pause 0.5
            noflip
            easein  at xpos x1+dx fx.stretch(1.0-dz, 1.0+dz)
            easeout mt xpos 0.5   fx.stretch(1.0+dz, 1.0-dz)
            easein  mt xpos x0-dx fx.stretch(1.0-dz, 1.0+dz)
            easeout at xpos x0    fx.stretch(1.0, 1.0)
            pause 0.5
            repeat
    show text "a little squash/stretch + anticipation/overshoot" as t3 at center:
        ypos y

    $ y += 0.15
    $ dx = 0.1
    $ at = 0.3
    $ mt = 1.0-at
    $ dz = 0.2
    show usagi happy 2 focus as u4:
        xpos x0
        ypos y
        zoom z
        fx.stretch(1, 1)
        block:
            flip
            easein  at xpos x0-dx fx.stretch(-(1.0-dz), 1.0+dz)
            easeout mt xpos 0.5   fx.stretch(-(1.0+dz), 1.0-dz)
            easein  mt xpos x1+dx fx.stretch(-(1.0-dz), 1.0+dz)
            easeout at xpos x1    fx.stretch(-(1.0), 1.0)
            pause 0.5
            noflip
            easein  at xpos x1+dx fx.stretch(1.0-dz, 1.0+dz)
            easeout mt xpos 0.5   fx.stretch(1.0+dz, 1.0-dz)
            easein  mt xpos x0-dx fx.stretch(1.0-dz, 1.0+dz)
            easeout at xpos x0    fx.stretch(1.0, 1.0)
            pause 0.5
            repeat
    show text "lots of squash/stretch + anticipation/overshoot" as t4 at center:
        ypos y

    $ y += 0.15
    $ a = 30
    # $ a = 90
    show usagi happy 2 focus as u5:
        xpos x0
        ypos y
        zoom z
        transform_anchor True
        rotate 0
        fx.stretch(1, 1)
        block:
            flip
            easein  at xpos x0-dx fx.stretch(-(1.0-dz), 1.0+dz) rotate  a
            easeout mt xpos 0.5   fx.stretch(-(1.0+dz), 1.0-dz) rotate  0
            easein  mt xpos x1+dx fx.stretch(-(1.0-dz), 1.0+dz) rotate -a
            easeout at xpos x1    fx.stretch(-(   1.0),    1.0) rotate  0
            pause 0.5
            noflip
            easein  at xpos x1+dx fx.stretch(1.0-dz, 1.0+dz) rotate -a
            easeout mt xpos 0.5   fx.stretch(1.0+dz, 1.0-dz) rotate  0
            easein  mt xpos x0-dx fx.stretch(1.0-dz, 1.0+dz) rotate  a
            easeout at xpos x0    fx.stretch(   1.0,    1.0) rotate  0
            pause 0.5
            repeat
    show text "rotate a little during anticipation/overshoot.\nrotate AFTER scaling (renpy default)" as t5 at center:
        ypos y

    $ y += 0.15
    $ w = 1440
    $ h = 1080
    # $ a = 90
    show usagi happy 2 focus as u6:
        zoom z
        # pos(0.0, 0.0)
        # transform_anchor True # this wrecks everything with matrices
        matrixanchor (0.5, 1.0)
        block:                         
            matrixtransform            OffsetMatrix(int(     x0*w), int(y*h), 0) * ScaleMatrix(-(   1.0),    1.0, 1.0) * RotateMatrix(0, 0, 0)
            easein  at matrixtransform OffsetMatrix(int((x0-dx)*w), int(y*h), 0) * ScaleMatrix(-(1.0-dz), 1.0+dz, 1.0) * RotateMatrix(0, 0,-a)
            easeout mt matrixtransform OffsetMatrix(int(    0.5*w), int(y*h), 0) * ScaleMatrix(-(1.0+dz), 1.0-dz, 1.0) * RotateMatrix(0, 0, 0)
            easein  mt matrixtransform OffsetMatrix(int((x1+dx)*w), int(y*h), 0) * ScaleMatrix(-(1.0-dz), 1.0+dz, 1.0) * RotateMatrix(0, 0, a)
            easeout at matrixtransform OffsetMatrix(int(     x1*w), int(y*h), 0) * ScaleMatrix(-(   1.0),    1.0, 1.0) * RotateMatrix(0, 0, 0)
            pause 0.5
            matrixtransform            OffsetMatrix(int(     x1*w), int(y*h), 0) * ScaleMatrix(   1.0,    1.0, 1.0) * RotateMatrix(0, 0, 0)
            easein  at matrixtransform OffsetMatrix(int((x1+dx)*w), int(y*h), 0) * ScaleMatrix(1.0-dz, 1.0+dz, 1.0) * RotateMatrix(0, 0,-a)
            easeout mt matrixtransform OffsetMatrix(int(    0.5*w), int(y*h), 0) * ScaleMatrix(1.0+dz, 1.0-dz, 1.0) * RotateMatrix(0, 0, 0)
            easein  mt matrixtransform OffsetMatrix(int((x0-dx)*w), int(y*h), 0) * ScaleMatrix(1.0-dz, 1.0+dz, 1.0) * RotateMatrix(0, 0, a)
            easeout at matrixtransform OffsetMatrix(int(     x0*w), int(y*h), 0) * ScaleMatrix(   1.0,    1.0, 1.0) * RotateMatrix(0, 0, 0)
            pause 0.5
            repeat
    show text "rotate BEFORE scaling (with matrices)\nthis isn't identical, but hard to see the difference with small angles" as t6 at center:
        ypos y

    pause
    return