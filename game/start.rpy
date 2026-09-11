label start:
    call start_at(0)
    return

label start_at(i):
    $ quick_menu = False
    call fx.log("# Don't forget: F11 to fullscreen the show. Move your mouse offscreen, advance with the spacebar") from _call_fx_log_16
    while i < len_scenes:
        call fx.log(f'# {scenes[i]}')
        call expression scenes[i].label
        $ i += 1
    return