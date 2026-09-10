label start(i=0):
    $ quick_menu = False
    $ fx.log("# Don't forget: F11 to fullscreen the show. Move your mouse offscreen, advance with the spacebar")
    while i < len_scenes:
        call fx.log(f'# {scenes[i]}')
        call expression scenes[i].label
        $ i += 1