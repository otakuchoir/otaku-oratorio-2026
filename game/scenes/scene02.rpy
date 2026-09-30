label scene02:
    call fx.log("# Hello, VN operator! These messages are to help you during the show.")
    call fx.log("# They won't be visible to the audience if you're running a desktop version of the show.")
    call fx.log("# They're visible in the web version, but you shouldn't use that on the day of the show, because wifi can fail.")
    call fx.log("# Instead, run this from a terminal/command line (ask Evan to demonstrate).")
    call fx.log("# Terminal goes on your laptop screen and shows these messages. Show goes on the projector screen.")
    call fx.log("# F11 to fullscreen the show. Move your mouse offscreen, then advance with the spacebar - not with mouse clicks, so the audience won't see the cursor.")
    call fx.log("# Thanks for stepping up to do this!")
    call fx.log("#")

    scene bg black
    call fx.play_music_in_dev("bgm_001_godzilla_1_0_godzilla_suite_ii__godzilla_minus_one.opus")
    show bg scene02 01 with dissolve
    pause 4.0
    show bg scene02 02 with dissolve
    pause 2.0
    show bg scene02 03 with dissolve
    with vpunch
    pause 1.0
    show bg scene02 04 with dissolve
    with vpunch
    pause 1.0
    show bg scene02 01 with dissolve
    # play music "bgm_001_godzilla_1_0_godzilla_suite_ii__godzilla_minus_one.opus"
    # > 2        EXT. CITY MONSTER ATTACK                                                  2
    # > A RUBBER-SUITED GODZILLA-STYLE PLANET DESTROYER STOMPS
    # > THROUGH MODEL CITY, BURNING BUILDINGS WITH ATOMIC BREATH
    announcer "Oh no! The monster is destroying the city! Can anybody stop this?"

    window hide
    window auto
    # > A HERO DRESSED IN RED RUNS IN, DRAMATICALLY SKIDDING ON TO
    # > THE SCENE AS THEIR SCARF BLOWS IN THE WIND DRAMATICALLY.
    stop music fadeout 1
    call fx.play_music_in_dev("bgm_002_seajetter_kaito.opus")
    show bg scene02 05 with dissolve
    pause 2.0
    show bg scene02 06 with dissolve
    pause 2.0
    show bg scene02 07 with dissolve
    kitadani "Fear not, announcer! Courageous Kaito! Reporting for Duty!"
    show bg scene02 08 with dissolve
    announcer "When chaos calls, the Crown answers swiftly with its bravest warrior: Sea Jetter Kai!"
    window hide
    window auto
    return