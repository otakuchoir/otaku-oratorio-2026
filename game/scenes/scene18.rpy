
label scene18:
    play music bgm_007_mii_news__tomodachi_life_living_the_dream
    window hide
    window auto
    $ y = 0.48
    scene bg news studio:
        noflip
        anchor (0.5,1.0)
        pos (0.5,1.0)
        zoom 1.15
    show reporter1:
        zoom 1.0
        xpos 0.2
        ypos y
    show reporter2:
        zoom 1.0
        xpos 0.5
        ypos y+0.03
    show reporter3:
        zoom 1.0
        xpos 0.8
        ypos y
    show bg breaking news as bg2:
        ease 0.5 zoom 1.0
    show fx_crt_scanlines
    with dissolve
    pause 1.0
    hide bg2
    # > 18       VARIOUS SCREENS SHOWING THE NEWS OF THE SPACESHIP EDEN AS IT 18
    # > EMBARKS ON A MISSION TO DESTROY THE SPACE CRYSTAL.
    reporter1 "Breaking news, The Earth Crown Military is now moving on the Crystal"
    reporter2 "Earth’s last defense against absolute destruction at the hands of a humanoid space alien who, six months ago, doomed the planet"
    reporter3 "Leading this operation is none other than decorated Earth Crown Military Captain, Kohei Kitadani"
    reporter1 "Kitadani, a well respected geological scientist with the ECM is often credited as the father of the ULTIMA CANNON"
    reporter2 "The very same canon we use for mining ULTIMA to power our homes"
    ### page 34 ###
    # > THE FINAL DAY - FINAL FANTASY XIV ENDWALKER
    reporter3 "Now being repurposed to save us from this angelic terror..."
    stop music fadeout 1
    scene bg black with dissolve
    return