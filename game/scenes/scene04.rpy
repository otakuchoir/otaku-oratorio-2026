# scene 04 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi&t=kelisha
label scene04:
    scene bg classroom at flip with dissolve
    play music bgm_scene04_01

    # the trio walk into the classroom (the stage) from the right. kelisha's already in class.
    show kelisha serious at left, flip
    show sanders neutral at offscreenright
    show takeshi neutral at offscreenright
    show usagi neutral at offscreenright
    pause 0
    show sanders neutral at center
    show takeshi neutral at right2
    show usagi neutral at right
    with ease

    # > 4        INT. CROWN MILITARY ACADEMY, CLASSROOM                                    4
    kelisha "Late again?"

    # autofocusing-on-speech only works with one speaker at a time.
    # the trio is speaking here, so highlight them manually for this one line.
    show sanders neutral focus
    show usagi neutral focus
    show takeshi neutral focus
    trio "Sorry professor."
    show sanders neutral
    show usagi neutral
    show takeshi neutral

    kelisha "No, that grade is gonna be sorry if you three don’t get it together before the midterm."
    kelisha "Sanders, you most of all can’t afford to miss out on any points on account of lateness..."
    sanders angry 1 "Why you gotta bust me out like that?"
    kelisha stinkeye "Because I don’t want you in my classroom another year if you fail."

    # I think it's okay for usagi/takeshi to laugh at sanders with the class here.
    # later, their reactions don't match the class reactions which isn't ideal, but I don't think that causes much confusion.
    show usagi excited
    show takeshi happy 2
    # a few other sanders emotes could work here, I think this one's most in character but I could be wrong
    show sanders eyeroll
    "The classroom laughs, she got him good."
    # laughter doesn't last very long
    show usagi neutral
    show takeshi neutral
    # "get it together, sanders..."
    show sanders deadpan

    kelisha serious "And as for you, Kitadani... You think you can just come in here whenever you want? You should know better."
    ### page 6 ###
    usagi "Sorry, professor."

    show sanders neutral
    show kelisha neutral
    kelisha "And you, Williamson... you could fail everything from now until the end of the year and you’d be good, but you DON’T need to be late. Don’t let your little friends drag you down."
    takeshi @ happy 1 "My apologies professor, we just ran over time in the training simulator."
    "The classroom is annoyed with Takeshi’s apology..."
    classmate "It’s crazy he’s so smart... He’s a Lunar."

    show kelisha serious
    show usagi annoyed
    show takeshi annoyed
    usagi "And what does that have to do with anything?"

    # literally falls silent.
    stop music fadeout 1
    # TODO: remove this narration and just pause the music instead?
    "The classroom falls silent."

    kelisha "Take your seats your three. And for the rest of you, we prefer the term colony-born. Lunars sounds so... alien."
    # > On the screen a news story appears
    # fade-in the reporters at a distance (zoomed out), but not the others' expression changes
    show usagi neutral
    show takeshi neutral
    show kelisha neutral
    pause 0
    # because they're zoomed out, "topleft2", "topcenter", etc. aren't quite aligned right
    show reporter1:
        zoom 0.5 yalign 0 xalign 0.4
    show reporter2:
        zoom 0.5 yalign 0 xalign 0.5
    show reporter3:
        zoom 0.5 yalign 0 xalign 0.6
    with dissolve

    kelisha "And speaking of the colony-born Earth-born dichotomy, there are developments in the North American mining region, Northeast sector."
    kelisha "Pay attention, this has to do with your midterms..."

    # news report starts. zoom in on the reporters, pushing the others off screen
    show bg jersey city cityscape as bg2 behind kelisha, usagi, sanders, takeshi:
        top
        zoom 0.0
        ease 0.5 zoom 1.0
    pause 0
    play music bgm_scene04_02
    show kelisha at offscreenleft
    show usagi at offscreenright
    show takeshi at offscreenright
    show sanders at offscreenright
    show reporter1 at left, smoothzoom
    show reporter2 at center, smoothzoom
    show reporter3 at right, smoothzoom
    with ease
    hide bg

    reporter1 "Tensions flare in the North American region as we approach day 42 of the mine workers strike."
    reporter2 "Residents and workers in the Kingdom of New Jersey continue to resist Crown Military orders to extract Ultima Ore."
    reporter3 "But not to fear, this dispute won’t be affecting your vacation plans."
    # > (MORE)
    ### page 7 ###
    reporter3 "While the Kingdom of New Jersey is responsible for a large part of the Ultima Ore supply chain, Our Crown Military King, is confident that an agreement will be reached before the situations impacts the economy."
    hide reporter1
    hide reporter2
    hide reporter3
    show king at center
    with dissolve
    # > TRANSITION TO
    king "WE ARE FULLY CONFIDENT THAT THE PEOPLE OF THE KINGDOM OF NEW JERSEY WILL COMPLY WITH ORDERS AND ALL WILL BE WELL."

    scene black with dissolve
    stop music fadeout 1
    return

transform smoothzoom:
    ease 0.4 zoom 1