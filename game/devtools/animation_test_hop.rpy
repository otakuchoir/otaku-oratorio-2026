label animation_test_hop:
    scene bg black
    show usagi happy 2 focus as u1:
        xpos 0.1
        ypos 0.8
        pause 0.2
        block:
            fx.hop(dur=0.5, y=100)
            pause 0.5
            repeat
    show usagi happy 2 focus as u2:
        xpos 0.3
        ypos 0.8
        fx.hopN(dur=(0.2, 0.3), y=100, stretch=(0.1, 0.15))
        pause 0.3
        repeat
    show usagi happy 2 focus as u3:
        xpos 0.5
        ypos 0.8
        fx.hopN(dur=(0.2, 0.3), y=100, stretch=(0.2, 0.3))
        pause 0.3
        repeat

    show usagi happy 2 focus as tu1:
        xpos 0.1
        ypos 0.4
        pause 0.2
        # block:
            # fx.hop(dur=0.5, y=100)
            # repeat
        fx.hopN(dur=(0, 0.5), y=100, stretch=(0,0), n=None)
    show usagi happy 2 focus as tu2:
        xpos 0.3
        ypos 0.4
        fx.hopN(dur=(0.2, 0.3), y=100, stretch=(0.1, 0.15), n=None)
    show usagi happy 2 focus as tu3:
        xpos 0.5
        ypos 0.4
        fx.hopN(dur=(0.2, 0.3), y=100, stretch=(0.2, 0.3), n=None)

    show usagi happy 2 focus as u4:
        xpos 0.8
        ypos 0.8

        # these seem to apply rotation+scaling in a fixed order
        # if we want the other order, we have to use matrixes
        xzoom 1
        rotate 0
        #xzoom 0.3
        #linear 1 rotate 90
        #linear 1 rotate 180
        #linear 1 rotate 270
        #linear 1 rotate 360
        #linear 1 rotate 90  xzoom 0.1
        #linear 1 rotate 180 xzoom 1
        #linear 1 rotate 270 xzoom 0.1
        #linear 1 rotate 360 xzoom 1
        linear 1 xzoom 0.1 rotate 90  
        linear 1 xzoom 1   rotate 180 
        linear 1 xzoom 0.1 rotate 270 
        linear 1 xzoom 1   rotate 360 
        repeat
    show usagi happy 2 focus as tu4:
        xpos 0.8
        ypos 0.4

        # Matrix.rotate and Matrix.scale sort of work, but don't animate
        matrixtransform          ScaleMatrix(0.3, 1, 1)*RotateMatrix(0, 0,   0)
        linear 1 matrixtransform ScaleMatrix(0.3, 1, 1)*RotateMatrix(0, 0,  90)
        linear 1 matrixtransform ScaleMatrix(0.3, 1, 1)*RotateMatrix(0, 0, 180)
        linear 1 matrixtransform ScaleMatrix(0.3, 1, 1)*RotateMatrix(0, 0, 270)
        linear 1 matrixtransform ScaleMatrix(0.3, 1, 1)*RotateMatrix(0, 0, 360)
        repeat
    show text "no squash/stretch" as t1 at left:
        ypos 0.45
    show text "\na little squash/stretch" as t2 at left2:
        ypos 0.45
    show text "lots of squash/stretch" as t3 at center:
        ypos 0.45
    show text "rotate AFTER stretch\nrenpy default" as t4 at right
    show text "rotate BEFORE stretch\nwith matrices" as t5 at right:
        ypos 0.45
    pause
    return