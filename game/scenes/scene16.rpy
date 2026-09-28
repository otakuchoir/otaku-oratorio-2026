# scene 16 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi+postgrad&t=usagi+postgrad&t=sanders+postgrad&t=jojo&t=kelisha&t=bart
label scene16: 
    scene black
    # scroll the ground, keep the sky the same. not a perfect effect, visible seam if you're looking,
    # but the big ol mechs mostly block it. cheating(tm)
    call fx.bgloop_x('bg moon and earth', dur=3.0) 
    show bg moon and earth:
        crop (0.0, 0.0, 1.0, 0.67)
    show sanders mech postgrad neutral at center, fx.yoffset(-50), fx.hover(2.3, y0=-50)
    show takeshi mech postgrad neutral at right,  fx.yoffset(-50), fx.hover(2.5, y0=-50)
    show usagi mech postgrad neutral   at left,   fx.yoffset(-50), fx.hover(1.7, y0=-50)
    with dissolve
    sanders "You know, on Earth, there used to be collections of trees called forests. Now everyone lives in domed regions..."
    sanders mech postgrad happy "What I’m saying is... flying out here is awesome. It’s so open wide and spacious."
    takeshi mech postgrad happy 1 "You actually have something positive to say about the moon for once?"
    show sanders mech postgrad neutral
    show takeshi mech postgrad neutral
    usagi "Orders are to keep comms clear. We don’t know if the energy pattern is aware of our approaching. Stay silent."

    # > 16       EXT. SPACE - MECHS                                                       16
    # > Usagi, Sanders, and Takeshi are traveling to the dark side of
    # > the moon via mech.

    # IRL section: cut from dialogue shown here
    #
    #
    # end IRL section

    # > They land on the surface.
    ### page 29 ###
    scene bg lunar surface with fade

    # show jojo neutral at left
    # show kelisha neutral at right
    # show bart neutral at top
    computer "Approaching the drop zone. Prepare for landing."
    $ y0 = -0.7
    $ x0 = 0.5
    show sanders mech postgrad neutral:
        ypos y0 xpos x0
        easein 3 ytextbox xpos 0.65
    show takeshi mech postgrad neutral flip:
        ypos y0 xpos x0
        pause 0.3
        easein 3 ytextbox xpos 0.15
    show jojo mech neutral:
        ypos y0 xpos x0
        pause 0.6
        easein 3 ytextbox xpos 1.3
    show usagi mech postgrad neutral:
        ypos y0 xpos x0
        pause 1
        easein 3 ytextbox xpos 0.35
    show bart mech neutral flip:
        ypos y0 xpos x0
        pause 1.4
        easein 3 ytextbox xpos -0.3
    show kelisha mech neutral:
        ypos y0 xpos x0
        pause 2
        easein 3 ytextbox xpos 1.3
    pause 4
    #show sanders at right2
    #show takeshi at left, flip
    #show usagi at left2
    #show bart at offscreenright
    #show kelisha at offscreenright
    #show jojo at offscreenleft, flip
    #with MoveTransition(3, time_warp=_warper.easein)
    usagi "Internal loop comms activated. Proximity mode activated. We’re free to speak..."
    show usagi mech postgrad serious 1 flip at left2
    usagi "That doesn’t mean get on my nerves."

    show sanders mech postgrad angry 2
    sanders "Yo, what’s your problem."
    usagi "You’re already getting on my nerves."

    # > Professor Jojo approaches.
    show jojo mech neutral at offscreenright
    pause 0
    show jojo at right with ease
    takeshi "It has been months... we haven’t talked about it."

    # > Jojo walks off. Kelisha passes.
    show sanders mech postgrad angry 1 flip
    jojo @ serious "We’re moving out. Do not lag behind. If you find the source of the pattern, ping your location to the rest of the squad."
    show kelisha mech worried at offscreenright
    pause 0
    show jojo flip at offscreenright
    show kelisha at right
    with ease

    # > Kelisha moves on.
    show usagi mech postgrad neutral
    kelisha "Now is not the time. Remember what I told you during the New Jersey mission."
    show kelisha flip at offscreenright
    with ease
    show sanders -flip
    show takeshi mech postgrad annoyed
    show usagi mech postgrad serious 1
    sanders "That’s what this is about? That’s why we’ve barely spoken since midterms? Because you suddenly want to care about social justice or something?"
    takeshi "Sanders... stop."
    # > The three begin their search for the energy pattern.
    usagi "Let’s move out."

    sanders "No... I just don’t get it."
    ### page 30 ###
    show takeshi mech postgrad angry 1
    takeshi "Let it go Sanders..."

    sanders "No because... Kitadani. We’re not kids anymore. Haven’t been for a long time."
    sanders "We graduated from military academy. You know that we fight. Our combat training isn’t theory."
    sanders "And sometimes, to keep the peace, we’ve got to get our hands dirty."

    takeshi @ angry 2 "For the greater good?"
    show sanders flip at right, fx.hop with ease
    sanders "For the greater good, dammit. I don’t know why you act like you don’t understand this."

    show usagi at center with ease
    show usagi mech postgrad serious 2
    usagi "I don’t know why you can’t imagine a world where “corrective action” isn’t the default when someone disagrees with you."
    usagi "I don’t understand how, in all the time you’ve been around a Colony Born like Takeshi, you’ve somehow held on to this ridiculous Earth born nobility."
    show usagi mech postgrad angry
    usagi "I don’t know how you can look people in the face and just LIE."

    show sanders mech postgrad angry 2 -flip
    sanders "Because we all know the alternative, Kitadani. And you know that if Williamson here ever behaved with even a FRACTION of the way you do..."
    sanders "He’s not the child of a legend. If you weren’t you, you would have been dealt with a long time ago."
    sanders @ postgrad angry 3 "You’re just as bad as The Queen of New Jersey... Only you don’t even take a stand. You just go with it, sulk and pretend like you’re not benefiting."

    # > Silence.
    # disable the speaker spotlight for this moment of silence
    # (jeez, this is way harder than it should be)
    show usagi focus
    show takeshi focus
    show sanders focus
    pause
    # show sanders at right2
    # with ease
    show usagi -focus
    show takeshi -focus
    show sanders -focus
    show usagi mech postgrad shock at fx.hop
    sanders "No quippy comeback? What? Cat got your tongue?"
    show takeshi mech postgrad shock at fx.hop
    ### page 31 ###

    # > They have happened upon a large crystal structure.
    usagi "What is that..."
    call fx.log("SONG: Ragnarok. show keeps going with no visible lyrics")

    # everyone walks toward the crystal. first usagi, then the rest of the trio...
    $ x0 = -0.3
    $ x1 = 1.3
    show usagi mech postgrad worried:
        ease 3 xpos x1
    show takeshi mech postgrad worried 1:
        pause 1
        ease 3 xpos x1
    show sanders mech postgrad shock flip:
        fx.hop
        pause 1.5
        ease 3 xpos x1
    # next kelisha, worried for what happens next...
    show kelisha mech worried flip:
        xpos x0
        pause 1.5
        ease 5 xpos x1
    # finally bart and jojo, giddy about finding it at last
    show jojo mech grin 2 flip:
        xpos x0
        pause 3
        parallel:
            fx.hop
            repeat
        parallel:
            ease 4.5 xpos x1
    show bart mech grin 2 flip:
        xpos x0
        pause 3.7
        ease 4.5 xpos x1
    pause 6
    return