# https://otaku-oratorio-2026-gallery.netlify.app/?t=sanders&t=takeshi&t=usagi&t=kelisha
label scene10:
    call fx.play_music_in_dev("bgm_010_ready_set_go__kirby_and_the_forgotten_land.opus")
    scene bg lunar tarmac with fade:
        zoom 1.5
        yalign 0.8
        xalign 1.0
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
        xalign 0.9
    show kelisha neutral at left, flip
    show takeshi at left2
    show sanders at right2
    show usagi:   
        xpos 1.0
    with moveinleft
    kelisha "I’m sure whatever RIVETING conversation you’re having at 5AM can wait until we all board?"
    show sanders at noflip
    show takeshi neutral at noflip
    sanders "Yes, professor."
    sanders @ smug "See? Even the way we measure time is Earth’s standard!"
    kelisha "You three, after you’re settled, come find me in my office. We need to review some intel."

    # everyone boards the shuttle. walk offscreen...
    $ dur = 2.0
    $ dx = -2000
    show kelisha:
        noflip
        fx.ease_xoffset(dur=dur, x1=dx)
    pause 0.3
    show sanders at fx.ease_xoffset(dur=dur, x1=dx)
    show usagi at fx.ease_xoffset(dur=dur, x1=dx)
    show takeshi at fx.ease_xoffset(dur=dur, x1=dx)
    # pause dur  # breaks lint
    pause 2.0

    # zoom to the shuttle (now that the graphic is ready)...
    show shuttle:
        zoom 1.0
        anchor (0.5, 1.0)
        pos (-0.8, 0.2)
        ease 1.5 zoom 0.35 pos (0.5, 1.0)
    show bg lunar tarmac:
        ease 1.5 zoom 1.0 xalign 0.5 yalign 0.5
    pause 2.0

    # ...and back onscreen
    scene black
    call scene11.space_background
    show scene10_bg_takeoff as bg1:
        zoom 1.5
        xalign 1.0
        yalign 1.0
    show bg spaceship window transparent
    with fade
    window show

    $ dur = 1.5
    # $ dur = 0
    $ dx = 1500
    show takeshi neutral at right2, fx.ease_xoffset(dur=dur, x0=dx)
    show usagi neutral at left2, fx.ease_xoffset(dur=dur, x0=dx)
    show sanders neutral at center, fx.ease_xoffset(dur=dur, x0=dx)
    # pause dur   # breaks lint
    pause 1.5

    # > TAKE OFF SEQUENCE. SPACE SHUTTLE TRAVELS FROM THE MOON TO
    # > EARTH.
    # no lengthy wait for blastoff, just go
    pause 1
    show scene10_bg_takeoff as bg1:
        xalign 1.0
        yalign 1.0
        parallel:
            easeout 3.0 xalign 0.0
        parallel:
            pause 1.5
            easeout 1.5 yalign 0.25
    show bg white as bgfx behind bg:
        alpha 0.0
        pause 1.0
        easeout 2.0 alpha 1.0
        pause 1.5
        easein 2.0 alpha 0.0
    show bg white as fgfx:
        alpha 0.0
        pause 1.0
        easeout 2.0 alpha 0.3
        pause 1.5
        easein 2.0 alpha 0.0
    pause 3.0
    hide bg1
    hide bg2
    pause 4.0
    show bg black with dissolve
    return

image scene10_bg_takeoff = Composite(
    (1440 * 2, 1080),
    (0, 0), Transform('bg lunar tarmac', xzoom=-1.0),
    (1440, 0), 'bg lunar tarmac',
)