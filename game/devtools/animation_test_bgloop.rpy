label animation_test_bgloop:
    scene bg beige
    call scene11.space_background
    "scene 11's space background scroll, hardcoded-ish"

    #scene bg beige
    #call fx.bgloop(Transform('bg space', zoom=1440.0/1280.0), dur=(23, 79))
    #"what"

    scene bg beige
    call fx.bgloop_x('bg countryside', dur=3.0)
    "horizontal scrolling fx. any background, dynamic dimensions"
    scene bg beige
    call fx.bgloop_x('bg countryside', dur=-3.0)
    "to the right"

    scene bg beige
    $ test_bgloop_space = Transform('bg space', zoom=1440.0/1280.0)
    call fx.bgloop(test_bgloop_space, dur=(3.0, 7.0))
    "horizontal + vertical scrolling. any background, dynamic dimensions. traveling up and left"
    scene bg beige
    call fx.bgloop(test_bgloop_space, dur=(-3.0, 7.0))
    "now we're going right instead of left"
    scene bg beige
    call fx.bgloop(test_bgloop_space, dur=(-3.0, -7.0))
    "and now down"
    scene bg beige
    call fx.bgloop('bg space', dur=(-3.0, -7.0))
    "oops, bg image is smaller than the screen. too small! right side clips"

    pause
    return
