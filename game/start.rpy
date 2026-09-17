label start:
    call start_at(0)
    return

label start_at(i):
    $ quick_menu = False
    call fx.log("# Hello, VN operator! These messages are to help you during the show.")
    call fx.log("# They won't be visible to the audience if you're running a desktop version of the show.")
    call fx.log("# They're visible in the web version, but you shouldn't use that on the day of the show, because wifi can fail.")
    call fx.log("# Instead, run this from a terminal/command line (you can ask Evan for help with this).")
    call fx.log("# Terminal goes on your laptop screen and shows these messages, show goes on the projector screen.")
    call fx.log("# F11 to fullscreen the show. Move your mouse offscreen, then advance with the spacebar so the audience can't see the cursor.")
    call fx.log("# Thanks for stepping up to do this!")
    call fx.log("#")
    while i < len_scenes:
        call fx.log(f'# {scenes[i]}')
        call expression scenes[i].label
        $ i += 1
    return