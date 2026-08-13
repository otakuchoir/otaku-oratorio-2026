# https://otaku-oratorio-2026-gallery.netlify.app/?t=sanders&t=takeshi&t=usagi&t=kelisha
label scene10:
    play music bgm_010_ready_set_go__kirby_and_the_forgotten_land
    scene bg lunar tarmac with dissolve:
        anchor (0.0,0.0)
        zoom 1.1
        xpos -0.1
    show sanders happy at center
    show usagi weary at right
    show takeshi neutral at left
    with moveinright
    show takeshi at flip
    show sanders at flip
    # > 10       EXT. CROWN MILITARY ACADEMY, TARMAC                                      10
    # > USAGI, TAKESHI AND SANDERS ARE BOARDING A TRANSPORT
    # > SPACECRAFT
    sanders @ teasing "Mornin’ losers!"
    usagi "That’s not really nice."
    takeshi "Well, neither is New Jersey Dome, but here we are. Getting ready to do a long haul flight to Earth."
    sanders @ prideful "I’ll have you know, New Jersey Dome is one of the greatest places in the solar system!"
    usagi "Oh great, you’ve got him started."
    show takeshi annoyed
    takeshi "I never took you to be the planeteristic type."
    ### page 16 ###
    show usagi shock
    show sanders neutral at noflip
    usagi "You never took SANDERS to be the--"
    show usagi neutral
    usagi "For the past 3 years you’ve known him, every other word out of his mouth is comparing something on the Moon to something from Earth!"
    sanders "Hey hey... Planeteristic is an extremely loaded word. I just have... pride."
    takeshi "Earth pride???"
    show sanders happy
    sanders "I mean... Yeah... It’s my heritage."
    show usagi annoyed
    usagi "So tell me Sanders, why DO you hate everyone on the moon?"
    show sanders anxious at flip
    sanders "Hey! Shhhhh -- those are SERIOUS accusations. Don’t joke like that!"
    show sanders neutral
    usagi "But just yesterday weren’t you talking about how bread on the moon tastes different because of artificial gravity?"
    show takeshi angry 1
    takeshi "Hey! There’s no difference between the gravity here and on Earth!"
    show sanders at noflip
    sanders "True, but there’s just something different about it..."
    takeshi "If it’s the same, then how is it different?"
    usagi "That’s what we call a bias. A planeteristic bias."
    show sanders at flip
    sanders "Usagi, you’re from Earth."
    show usagi neutral
    usagi "And we all live here."
    sanders "And I go back home every chance I get because."
    ### page 17 ###
    takeshi "Because what?"
    show bg lunar tarmac:
        xpos -0.05
    show kelisha neutral at left, flip
    show takeshi at left2
    show sanders at right2
    show usagi:   
        xalign 1.2
    with moveinleft
    kelisha "I’m sure whatever RIVETING conversation you’re having at 5AM can wait until we all board?"
    show sanders at noflip
    show takeshi neutral at noflip
    sanders "Yes, professor."
    sanders @ smug "See? Even the way we measure time is Earth’s standard!"
    kelisha "You three, after you’re settled, come find me in my office. We need to review some intel."

    # everyone boards the shuttle. walk offscreen...
    show kelisha at noflip
    pause 0
    hide kelisha
    hide takeshi
    hide sanders
    hide usagi
    with moveoutleft

    # ...and back onscreen
    show sanders neutral at center
    show usagi neutral at left2
    show takeshi neutral at right2
    with moveinright

    # no lengthy wait for blastoff, just go
    pause 1
    show bg white as bg2:
        alpha 0.7
        easein 5 alpha 0.0
    show takeshi at scene10_blastoff
    show usagi at scene10_blastoff
    show sanders at scene10_blastoff
    pause 4
    # > TAKE OFF SEQUENCE. SPACE SHUTTLE TRAVELS FROM THE MOON TO
    # > EARTH.
    show bg black with dissolve
    return

transform scene10_blastoff:
    parallel:
        hvibrate
    parallel:
        yoffset 0
        easeout 4 yoffset -1000
    parallel:
        fx.stretch(1.0,1.0)
        easein 0.03 fx.stretch(1.08, 0.92)
        easeout 3.97 fx.stretch(1.0, 1.0)