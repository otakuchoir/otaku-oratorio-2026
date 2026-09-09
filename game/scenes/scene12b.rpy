label scene12b: 
    scene bg black with dissolve
    # > SONG
    call fx.play_music_in_dev("bgm_007_mii_news__tomodachi_life_living_the_dream.opus")
    window hide
    window auto
    show bg breaking news as bg2:
        top
        zoom 0.0
        alpha 0.0

        ease 0.5 alpha 1.0 zoom 1.0
    pause 1.0
    show bg great hall outside
    show reporter1 at left
    show reporter2 at center
    show reporter3 at right
    hide bg2
    with dissolve
    reporter1 "BREAKING NEWS, we take you now live to the Kingdom of New Jersey where talks are underway in the ongoing miners strike..."
    ### page 22 ###
    reporter2 "That’s right, inside this building behind me, negotiations are unfolding as we speak."
    reporter3 "Both parties have decided to handle these talks privately, and so we wait outside for the outcome."
    scene bg black with dissolve
    stop music fadeout 1
    return