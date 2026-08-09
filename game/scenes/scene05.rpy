# scene 05 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi&t=jojo&t=bart
label scene05:
    scene bg campus
    play music bgm_scene05_01

    # slide onto the screen from the right
    show usagi happy 1 at offscreenright
    show takeshi happy 1 at offscreenright behind usagi
    show sanders happy at offscreenright
    pause 0
    show usagi at left2
    show takeshi at right2
    show sanders at right
    with ease

    # usagi turns around to talk to the other two
    show usagi at left2, flip

    # > 5        EXT. SCHOOL GROUNDS                                                       5
    # > Students are finished with classes, moving around campus.
    # > SANDERS, TAKESHI AND USAGI are walking together.
    sanders "Yo Usagi, you want to head to that new pho spot over at Rush Crater?"
    usagi neutral "I’m not riding the train for two hours for some pho when we should be studying for mid terms."
    takeshi "We could study on the train."

    show takeshi at right2, flip
    sanders "Exactly! See? Takeshi’s smart!"

    show takeshi at right2, noflip
    usagi annoyed "You guys know how I am about reading on moving vehicles."
    sanders "Even on the traaaaain!?"
    usagi "Yes even on the traaaaain."
    sanders teasing "But it’s PHO!"

    show usagi excited
    usagi "And I don’t give a Phooooo-"

    # > The three of them bust out into laughter when USAGI bumps
    # > into a man dressed in holy vestments. It’s BARTHANDELUS.
    ### page 8 ###

    # bart enters the screen as usagi walks toward him
    # both are walking backwards - a little weird, but signals to the audience neither is paying attention
    show takeshi happy 2
    show sanders
    show bart peaceful at offscreenleft
    pause 0
    show bart at left behind usagi
    show usagi at left
    show takeshi at center
    show sanders at right2
    with ease

    # usagi/bart bump into each other
    stop music
    show bart shock at fx.hop
    show usagi shock at left2, fx.hop
    # takeshi/sanders don't recognize bart immediately...
    show takeshi neutral
    show sanders neutral
    with ease

    # usagi/bart turn toward each other to talk
    show bart peaceful at flip
    show usagi worried at noflip
    # takeshi/sanders recognize bart; oh shit
    #
    # usagi hops later when she recognizes bart, to show surprise.
    # takeshi/sanders do not, because the hop looks too much like the
    # bump that happened just a moment ago
    show takeshi worried 1
    show sanders shock
    usagi "Oh, I’m so sorry."

    # takeshi/sanders collect themselves.
    show takeshi neutral at fx.bowdown(0.3)
    show sanders deadpan at fx.bowdown(0.3)
    takeshi "Your Holiness."

    # usagi's still clueless, why are her friends reacting?
    show usagi confused at flip
    usagi "My holy what?"

    # > Usagi realizes that she bumped into BARTHANDELUS the high
    # > prelate of the Church, a pope-like figure. She is lost for
    # > words.
    # > RAGNAROK
    # TODO: pending for ragnarok clip
    sanders @ angry 1 "Usagi!"

    # usagi recognizes bart now!
    show usagi at noflip
    pause 0.3
    show usagi shock:
        fx.hop
        "usagi neutral"
        fx.bowdown(0.15)
    bart "I see that the legacy of The Eden runs strong. Good day to you, Kitadani."

    # > USAGI, TAKESHI AND SANDERS exit stage while whispering
    # ...but they're still speaking, so they can't truly exit the stage!
    # I'm interpreting this as bart exiting the stage instead.
    show bart at offscreenleft, noflip
    with ease
    show usagi at fx.bowup(0.2)
    show takeshi at fx.bowup(0.2)
    show sanders at fx.bowup(0.2)
    sanders shock "How does the POPE know who you are??"
    takeshi "Well she is kind of famous."

    show usagi cry 2
    usagi "Guys shut UP I want to die so baaad right now....."
    sanders "No but seriously, why is he HERE?"
    takeshi "Doesn’t he need, like... a security detail?"

    show usagi at flip, left2
    usagi "He’s a really powerful HEAL class, so he’s probably walking around with max defense buffs at all times GUYS get me OUT OF HERE."

    # pan the camera to bart and jojo, away from the trio
    # jojo moves backwards across the screen awfully fast, but I think it's clear it's a pan, not a moonwalk
    show jojo neutral at offscreenleft
    pause 0
    show usagi at offscreenright
    show sanders neutral at offscreenright
    show takeshi at offscreenright
    show bart at left2
    show jojo at right behind bart
    with ease

    ### page 9 ###
    bart @ grin 1 "An interesting development..."
    bart @ scheming "You may yet prove to be useful in righting your wrongs, Kohei...."

    # > RAGNAROK ENDS
    stop music

    # > BARTHANDELUS WALKS OFF OPPOSITE SIDE OF STAGE WHERE PROFESSOR
    # > JOJO HAS BEEN WATCHING, THEY GREET EACH OTHER AND WALK OFF.
    # "they greet each other" - i'm interpreting this as "they walk offstage together"
    show bart grin 1 at right2, flip
    with ease
    show bart at offscreenright, flip
    show jojo at offscreenright, flip
    with ease
    show bg black with dissolve
    return