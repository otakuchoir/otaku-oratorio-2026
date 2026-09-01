# scene 06 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi
label scene06:
    scene bg train station
    call fx.play_music_in_dev("bgm_009_namis_theme__one_piece.opus")

    # a crude train-departures sign
    show black as sign_bg at top, scene06_sign_bg
    show scene06_train_sign "DEPARTURES" as sign_line0 at top
    show scene06_train_sign "\n1. Rush Crater     2 min" as sign_line1 at top
    show scene06_train_sign "\n\n2. Rush Crater   62 min" as sign_line2 at top
    with dissolve

    show sanders neutral at offscreenright
    show usagi neutral at offscreenright
    # takeshi doesn't have much dialogue in this scene so put him in the back
    show takeshi neutral at offscreenright behind sanders, usagi
    pause 0
    show sanders at right
    show takeshi at right2
    show usagi at center
    with ease

    # > 6        EXT. TRAIN STATION - AFTERNOON                                            6
    sanders @ angry 1 "Once again we’re late."
    takeshi "No, there’s still time. We’re gonna make it."
    usagi "I still don’t like the idea of going all the way to RUSH CRATER for some food. That’s nearly across the entire Moon’s surface."
    sanders @ teasing "I heard they have really good strawberry parfaits."
    show usagi at flip
    usagi @ happy 2 "Ok, I might be convinced..."
    usagi neutral "But seriously, midterms are coming up. We need to be studying."
    sanders @ eyeroll "We can study on the train."
    sanders "If we make it, that is..."

    # fake anger, she's clearly not actually serious
    usagi serious 2 "I hope we MISS our train and then we don’t have to GO."
    show usagi excited at noflip
    show takeshi happy 2
    sanders @ angry 2 "YOU’RE SO EVIL!"

    show scene06_train_sign "\n1. Rush Crater     1 min" as sign_line1 at top
    show scene06_train_sign "\n\n2. Rush Crater   61 min" as sign_line2 at top
    # usagi/takeshi walk left, through the gate.
    #
    # normally this would be easy - "at <place> with ease". but sanders is
    # jumping the gate at the same time, and renpy seems to only do one
    # transition ("with") at a time. so, use a more complex transform.
    show usagi neutral:
        xalign 0.5
        ease 0.15 * 3 + 0.4 + 0.8 xalign 0
    show takeshi neutral: 
        xalign 0.75
        ease 0.15 * 3 + 0.4 + 0.8 xalign 0.25
    # with MoveTransition(0.15 * 3 + 0.4 + 0.8, time_warp=_warper.easein)

    # about to jump the gate. act casual...
    show sanders deadpan at right
    # look around for danger...
    show sanders at flip
    pause 0.15
    show sanders at noflip
    pause 0.15
    show sanders at flip
    pause 0.15
    show sanders at noflip
    pause 0.4
    # and finally, jump
    show sanders angry 1 at scene06_gate_jump
    pause 0.8
    show sanders deadpan
    pause 0.2

    show sanders anxious at fx.hop
    stop music
    show train_security:
        right
        xoffset 500
        ease 0.5 xoffset 0

    train_security "Hey you! Stop!"

    # everyone looks back at the guard
    show usagi at left, flip
    show takeshi at left2, flip
    show sanders deadpan at center, flip
    usagi "Us?"
    train_security "Did you hop the gate?"
    ### page 10 ###
    sanders @ eyeroll "Everyone hops the gate."

    show sanders angry 1 at noflip
    usagi "I didn’t hop the gate."
    takeshi "Me either."
    show sanders neutral at flip

    # > THEY HAND OVER THEIR IDs. A TRAIN ANNOUNCEMENT OVER THE PA.
    # guessing that we'll have sfx here later
    # for now, departure sign blinks that the train is here. but not just yet, feels too soon
    train_security "Academy uniforms eh. Let me see some ID, the lot of yous."
    # I'm not sure what to do with faces here... usagi wasn't serious before (I think) but now they're actually missing it
    sanders angry 1 "We’re going to miss the train."
    usagi "Good. I didn’t want to go in the first place."
    sanders @ angry 2 "Evil..."

    # > USAGI IS NOT COMFORTABLE WITH THE FAME
    train_security "Kitadani... Usagi... oh, you’re the captain’s daughter!"

    # "usagi-weary" also works here, but this is serious enough for an entire scene where we call mom later so I don't think weary is quite enough
    show usagi angry
    train_security "You know, your father was an inspiration to us all-"
    sanders @ angry 2 "YO... we have somewhere to go, and yeah you’re harrassing Crown royalty so like can we go now?"

    show usagi annoyed
    show sanders eyeroll
    train_security "Sanders, George. Earthborn... you’re good to go..."

    show sanders neutral
    # this seems like a great time for the clock to tick
    show scene06_train_sign "\n1. Rush Crater     0 min" as sign_line1 at top, scene06_sign_blink
    show scene06_train_sign "\n\n2. Rush Crater   60 min" as sign_line2 at top
    train_security "Williamson, Takeshi... Colony born... A lunar..."
    train_security "Yup, it was definitely you who I saw jump the turnstile."

    # everyone reacts to that
    show sanders angry 2
    show usagi worried
    takeshi worried 2 "What??"
    ### page 11 ###
    sanders @ angry 3 "Hey old man, we don’t have TIME for this-"
    train_security "You’re gonna have to come with me."
    # usagi steps to the front to defend her friend
    show usagi at right2
    with ease
    usagi "Sir! Mr... Officer Ruckus, we’re on our way to Rush Crater and we’re about to miss our train, we REALLY have to get going."
    usagi "Williamson here did not fare evade. I swiped him in because he forgot his transit card at the dorms."

    # > TRAIN ANNOUNCEMENT, THEY HAVE MISSED THE TRAIN
    train_security "Well... If you say so."

    # it worked, we're safe, everyone's a little relieved...
    show takeshi worried 1
    show sanders angry 1
    show usagi neutral
    train_security "As you were."
    # > TRAIN SECURITY GUARD EXITS
    show train_security at flip, offscreenright

    # ...they stay relieved while running for the train...
    # (running for the train is mostly to rearrange the characters, so usagi can look toward takeshi below, instead of the other way round)
    show usagi at noflip
    show takeshi at noflip
    show sanders at noflip
    show usagi at offscreenleft
    show takeshi at offscreenleft
    show sanders at offscreenleft
    # the sign moves while running too, to signal camera movement
    # actually no it doesn't, it looked quite bad
    #show black as sign_bg at topoffscreenright, scene06_sign_bg
    #show scene06_train_sign "DEPARTURES" as sign_line0 at topoffscreenright
    #show scene06_train_sign "\n1. Rush Crater     0 min" as sign_line1 at topoffscreenright, scene06_sign_blink
    #show scene06_train_sign "\n\n2. Rush Crater   60 min" as sign_line2 at topoffscreenright
    with ease
    hide train_security

    show usagi at offscreenright
    show takeshi at offscreenright
    show sanders at offscreenright
    # fade out and back in, without destroying the scene
    show black as fade with dissolve
    show scene06_train_sign "\n1. Rush Crater     59 min" as sign_line1 at top, scene06_sign_noblink
    show scene06_train_sign "\n\n2. Rush Crater   119 min" as sign_line2 at top 
    hide fade with dissolve
    # they've just missed the train, change the sign
    pause 0
    show sanders at left2
    show usagi at center
    show takeshi at right
    with ease
    # ...until they see they've missed the train
    show usagi at noflip
    show takeshi angry 1 at noflip
    show sanders angry 2 at noflip
    # sanders "FAAAAHHHH (like the meme) we missed the train!"
    # "like the meme"? google says this, sounds like another f-word
    # https://www.tiktok.com/@soundeffectsonabudget/video/7566849185551568159?lang=en
    # no sound effects, let the voice actor handle it
    sanders @ angry 3 "FAAAAHHHH we missed the train!"
    usagi "The next one is in an hour. We can wait."

    # > USAGI LOOKS SYMPATHETICALLY TO TAKESHI WITHOUT SAYING A WORD.
    # not quite sure what to do with takeshi's expression here...
    # earlier, they run offstage to get to the train - mostly to rearrange them on stage,
    # so usagi can turn to look at takeshi
    show usagi worried focus at flip
    show takeshi annoyed focus
    pause 1.5
    show usagi neutral at noflip
    show takeshi neutral
    show sanders at flip, left2
    sanders "I thought you said you didn’t even want to GO."
    sanders "You CURSED us and now you have your wish, you’re a SORCERESS! AN EVIL SORCERESS!"
    show sanders angry 1
    usagi "I said we can wait."
    usagi happy 1 "I am craving that Pho..."
    usagi annoyed "And they better have the best damned Strawberry parfaits on the moon, or I’m coming for YOU Sanders..."
    show sanders at noflip
    # > 
    # > SONG: HANA NI NATTE    # > 
    # > 2 WEEKS LATER
    ### page 12 ###
    show black with dissolve
    return

transform scene06_gate_jump:
    transform_anchor True
    parallel:
        yoffset 0
        rotate 0
        ease 0.1 yoffset 100 
        ease 0.3 yoffset -400 rotate 30
        ease 0.2 yoffset 100 rotate 0
        ease 0.1 yoffset 0
    parallel:
        xalign 1.0
        ease 0.7 xalign 0.5
    #parallel:
    #    easeout 0.1 fx.stretch(1.2, 0.8)
    #    easeout 0.3 fx.stretch(0.7, 1.3)
    #    easeout 0.2 fx.stretch(1.2, 0.8)
    #    easeout 0.1 fx.stretch(1, 1)
    ypos ypos_textbox rotate 0

image scene06_train_sign = ParameterizedText(color="#0a0")
transform scene06_sign_blink:
    matrixcolor BrightnessMatrix(1)
    pause 0.5
    matrixcolor BrightnessMatrix(0)
    pause 0.5
    repeat
transform scene06_sign_noblink:
    matrixcolor BrightnessMatrix(0)
transform scene06_sign_bg:
    crop (0, 0, 350, 110)
