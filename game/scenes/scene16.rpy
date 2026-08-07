label scene16: 
    scene bg moon and earth with dissolve
    "PLACEHOLDER IRL scene16 first few lines only, until surface landing"

    # > 16       EXT. SPACE - MECHS                                                       16
    # > Usagi, Sanders, and Takeshi are traveling to the dark side of
    # > the moon via mech.

    # IRL section: cut from dialogue shown here
    #
    # sanders "You know, on Earth, there used to be collections of trees called forests. Now everyone lives in domed regions... What I’m saying is... flying out here is awesome. It’s so open wide and spacious."
    # takeshi "You actually have something positive to say about the moon for once?"
    # usagi "Orders are to keep comms clear. We don’t know if the energy pattern is aware of our approaching. Stay silent."
    #
    # end IRL section

    # > They land on the surface.
    ### page 29 ###
    show bg lunar surface with dissolve

    # show jojo neutral at left
    # show kelisha neutral at right
    # show bart neutral at top
    computer "Approaching the drop zone. Prepare for landing."
    show sanders postgrad neutral:
        offscreentop
        easein 3 ytextbox xalign 0.75
    show takeshi postgrad neutral:
        offscreentop
        flip
        pause 0.3
        easein 3 ytextbox xalign 0.0
    show jojo neutral:
        offscreentop
        pause 0.6
        easein 3 ytextbox xalign 1.6
    show usagi postgrad neutral:
        offscreentop
        pause 1
        easein 3 ytextbox xalign 0.25
    show bart neutral:
        offscreentop
        flip
        pause 1.4
        easein 3 ytextbox xalign -0.6
    show kelisha neutral:
        offscreentop
        pause 2
        easein 3 ytextbox xalign 1.6
    pause 4
    #show sanders at right2
    #show takeshi at left, flip
    #show usagi at left2
    #show bart at offscreenright
    #show kelisha at offscreenright
    #show jojo at offscreenleft, flip
    #with MoveTransition(3, time_warp=_warper.easein)
    usagi "Internal loop comms activated. Proximity mode activated. We’re free to speak..."
    show usagi postgrad serious 1 at left2, flip
    usagi "That doesn’t mean get on my nerves."

    show sanders postgrad angry 2
    sanders "Yo, what’s your problem."
    usagi "You’re already getting on my nerves."

    # > Professor Jojo approaches.
    show jojo at offscreenright
    pause 0
    show jojo neutral at right, noflip
    with ease
    takeshi "It has been months... we haven’t talked about it."

    # > Jojo walks off. Kelisha passes.
    show sanders postgrad angry 1 at flip
    jojo @ serious "We’re moving out. Do not lag behind. If you find the source of the pattern, ping your location to the rest of the squad."
    show kelisha at offscreenright
    pause 0
    show jojo at offscreenright, flip
    show kelisha worried at right
    with ease

    # > Kelisha moves on.
    show usagi postgrad neutral
    kelisha "Now is not the time. Remember what I told you during the New Jersey mission."
    show kelisha at offscreenright, flip
    with ease
    show sanders at noflip
    show takeshi postgrad annoyed
    show usagi postgrad serious 1
    sanders "That’s what this is about? That’s why we’ve barely spoken since midterms? Because you suddenly want to care about social justice or something?"
    takeshi "Sanders... stop."
    # > The three begin their search for the energy pattern.
    usagi "Let’s move out."

    sanders "No... I just don’t get it."
    ### page 30 ###
    show takeshi postgrad angry 1
    takeshi "Let it go Sanders..."

    sanders "No because... Kitadani. We’re not kids anymore. Haven’t been for a long time."
    sanders "We graduated from military academy. You know that we fight. Our combat training isn’t theory."
    sanders "And sometimes, to keep the peace, we’ve got to get our hands dirty."

    takeshi @ angry 2 "For the greater good?"
    show sanders at right, flip, hop with ease
    sanders "For the greater good, dammit. I don’t know why you act like you don’t understand this."

    show usagi at center with ease
    show usagi postgrad serious 2
    usagi "I don’t know why you can’t imagine a world where “corrective action” isn’t the default when someone disagrees with you."
    usagi "I don’t understand how, in all the time you’ve been around a Colony Born like Takeshi, you’ve somehow held on to this ridiculous Earth born nobility."
    show usagi postgrad angry
    usagi "I don’t know how you can look people in the face and just LIE."

    # > Silence.
    # disable the speaker spotlight for this moment of silence
    # (jeez, this is way harder than it should be)
    show usagi postgrad serious 2 focus
    show takeshi postgrad angry 1 focus
    show sanders postgrad angry 1 focus at noflip
    pause
    show sanders at right2
    with ease
    show usagi postgrad serious 2
    show takeshi postgrad angry 1
    show sanders postgrad angry 2
    sanders "Because we all know the alternative, Kitadani. And you know that if Williamson here ever behaved with even a FRACTION of the way you do..."
    sanders "He’s not the child of a legend. If you weren’t you, you would have been dealt with a long time ago."
    sanders @ postgrad angry 3 "You’re just as bad as The Queen of New Jersey... Only you don’t even take a stand. You just go with it, sulk and pretend like you’re not benefiting."
    show usagi postgrad shock at hop
    sanders "No quippy comeback? What? Cat got your tongue?"
    show takeshi postgrad shock at hop
    ### page 31 ###

    # > They have happened upon a large crystal structure.
    usagi "What is that..."
    # everyone walks toward the crystal. first usagi, then the rest of the trio...
    show usagi postgrad worried:
        ease 3 xalign 1.6
    show takeshi postgrad worried 1:
        pause 1
        ease 3 xalign 1.6
    show sanders postgrad shock:
        flip
        hop
        pause 1.5
        ease 3 xalign 1.6
    # next kelisha, worried for what happens next...
    show kelisha worried:
        offscreenleft
        flip
        pause 1.5
        ease 5 xalign 1.6
    # finally bart and jojo, giddy about finding it at last
    show jojo grin 2:
        offscreenleft
        flip
        pause 3
        parallel:
            hop
            repeat
        parallel:
            ease 4 xalign 1.6
    show bart grin 2:
        offscreenleft
        flip
        pause 3.3
        ease 4 xalign 1.6
    pause 6

    # too much clutter with sprites after this, show just the manga panel
    scene bg scene16a nofg with dissolve
    pause
    show bg scene16a with dissolve
    takeshi "The readings align... This is the wave pattern... I’m pinging the squad."
    # > A deafening sound rings over comms, this isn’t a ping. It’s
    # > something else.
    "PLACEHOLDER sfx"
    usagi "Ahhhh what the..."
    sanders "UGHHH MY HEAD.... Stop it WILLIAMSON"
    # > The ringing stops. The crystal stucture is glowing.
    takeshi "It wasn’t me... I don’t know what..."
    # > 
    # > SONG: RAGNAROK    # > 
    # > We start hearing sounds, but they do not make sense. It’s all
    # > dialogue from when Planet Destroyer announced that the Earth
    # > was doomed, to Kitadani attacking planet destroyer, and
    # > everything that ever happened on earth and the moon from then
    # > until right now.
    # > The crystal’s glowing intensifies and reveals the shaped of a
    # > human inside.
    show bg scene16b with dissolve
    sanders "Is that... A person???"
    # > Usagi moves forward.
    takeshi "The planet destroyer."

    # > The crstayl makes a LOUD crack noise, and then another. The
    # > human figure’s eyes open and look directly at Usagi Kitadani.
    show bg scene16c with dissolve
    takeshi "No! Usagi, don’t!"
    bart "At last!"

    ### page 32 ###
    # > FADE TO DARK as the Usagi, Takeshi, and Sanders stand still
    # > in shock, The Planet Destroyer’s gaze locked on Usagi, she
    # > returns the glare without blinking, the soldiers slowly move
    # > in, Jojo, Kelisha and Barthandelus watch in anticipation.
    # > END OF ACT 1
    ### page 33 ###
    # > ACT 2
    jojo "Move in and secure the specimen."

    show bg black with dissolve
    return