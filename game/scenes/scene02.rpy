
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
    show bg scene02 1 with dissolve
    pause 4.0
    show bg scene02 2 with dissolve
    pause 2.0
    show bg scene02 3 with dissolve
    with vpunch
    pause 1.0
    show bg scene02 4 with dissolve
    with vpunch
    pause 1.0
    show bg scene02 1 with dissolve
    # play music "bgm_001_godzilla_1_0_godzilla_suite_ii__godzilla_minus_one.opus"
    # > 2        EXT. CITY MONSTER ATTACK                                                  2
    # > A RUBBER-SUITED GODZILLA-STYLE PLANET DESTROYER STOMPS
    # > THROUGH MODEL CITY, BURNING BUILDINGS WITH ATOMIC BREATH
    announcer "Oh no! The monster is destroying the city! Can anybody stop this?"

    show bg scene02 5 with dissolve
    # > A HERO DRESSED IN RED RUNS IN, DRAMATICALLY SKIDDING ON TO
    # > THE SCENE AS THEIR SCARF BLOWS IN THE WIND DRAMATICALLY.
    stop music fadeout 1
    call fx.play_music_in_dev("bgm_002_seajetter_kaito.opus")
    kitadani "Fear not, announcer! Courageous Kaito! Reporting for Duty!"
    announcer "When chaos calls, the Crown answers swiftly with its bravest warrior: Sea Jetter Kai!"

    # > 
    # >          SONG: Fumetsu no Hero    # > 
    call scene02a

    show bg scene02 5 with dissolve
    kitadani "LET’S GO! CROWN BLASTER!"
    pause 0
    with vpunch

    # > THE MONSTER DOES NOT FLINCH.
    show bg scene02 1 with dissolve
    monster "Your precious Earth is mine to devour!"

    show bg scene02 5 with dissolve
    kitadani "DAMN!"
    computer "Ultima Cannon ready to dispense justice. Survival rate… 1%%."
    # > KITADANI GLANCES AT THE FAMILY PHOTO ON HIS DASHBOARD
    ### page 3 ###
    kitadani "This is the only way. Justice requires swift action. Citizens of Earth: Lend me your strength! For every human, on this beautiful Earth!"
    show bg scene02 1 with dissolve
    monster "WHAT!?"
    # > Monster reels back to charge it’s atomic breath
    # actually I'm gonna skip this direction because it looks too much like the monster is firing, not the ultima cannon
    kitadani "Ultima Cannon: fire!"
    show bg white as boom:
        alpha 0
        linear 1.5 alpha 1
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    scene bg black
    with dissolve
    stop music fadeout 3
    announcer "Kono bangumi wa, goran no suponsaa no teikyou de okurishimasu."
    # > PROJECTOR: “THIS CROWN NETWORK MEMORIAL SEGMENT WAS BROUGHT
    # > TO YOU BY THE FOLLOWING SPONSORS:”
    # > PROJECTOR:; IN MEMORY OF KOHEI KITADANI

    show text "{color=#fff}{size=80}THIS CROWN NETWORK\nMEMORIAL SEGMENT\nWAS BROUGHT TO YOU BY\nTHE FOLLOWING SPONSORS:{/size}{/color}" at truecenter with dissolve
    pause
    hide text with dissolve
    show text "{color=#fff}{size=160}IN MEMORY OF\nKOHEI KITADANI{/size}{/color}" at truecenter with dissolve
    pause
    hide text with dissolve
    return

label scene02a: 
    # https://drive.google.com/drive/folders/13OOlvv-BOTt1b4r9VxmytgVwE475gNtl
    # https://animelyricsaz.com/artist/masaaki-endou/fumetsu-no-hero-seajetter-kaito/971-39227
    # https://www.uta-net.com/song/320519/
    # finally, one where I can't find an english translation! could use machine translation, but that'll be bad...
    scene bg black with fade
    nvl clear
    title "Fumestu no Hero"
    lyrics "TODO lyrics. surprisingly hard to find an english translation online...!"
    nvl clear
    scene bg black with fade
    return