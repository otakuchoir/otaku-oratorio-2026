label scene05:
    scene bg default
    play music bgm_scene05_01
    show usagi happy1 at offscreenright
    show takeshi happy1 at offscreenright behind usagi
    show sanders happy at offscreenright
    pause 0
    show usagi at left2
    show takeshi at right2
    show sanders at right
    with ease
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
    # > The three of them bust out into laughter when USAGI bumps
    # > into a man dressed in holy vestments. It’s BARTHANDELUS.
    ### page 8 ###
    show usagi excited
    usagi "And I don’t give a Phooooo-"
    show takeshi happy2
    show sanders
    show bart peaceful at offscreenleft
    pause 0
    show bart at left behind usagi
    show usagi at left
    show takeshi at center
    show sanders at right2
    with ease
    stop music
    show bart shock at hop
    show usagi shock at left2, hop
    show takeshi neutral
    show sanders neutral
    with ease
    show bart peaceful at flip
    show usagi worried at noflip
    # show takeshi shock
    show takeshi worried1
    show sanders shock
    usagi "Oh, I’m so sorry."
    show takeshi neutral
    show sanders deadpan
    takeshi "Your Holiness."
    show usagi confused at flip
    usagi "My holy what?"
    # > Usagi realizes that she bumped into BARTHANDELUS the high
    # > prelate of the Church, a pope-like figure. She is lost for
    # > words.
    # > RAGNAROK
    sanders @ angry1 "Usagi!"
    show usagi at noflip
    pause 0.3
    show usagi shock at hop
    bart "I see that the legacy of The Eden runs strong. Good day to you, Kitadani."
    # > USAGI, TAKESHI AND SANDERS exit stage while whispering
    show bart at offscreenleft, noflip
    with ease
    sanders shock "How does the POPE know who you are??"
    takeshi "Well she is kind of famous."
    show usagi cry2
    usagi "Guys shut UP I want to die so baaad right now....."
    sanders "No but seriously, why is he HERE?"
    takeshi "Doesn’t he need, like... a security detail?"
    show usagi at flip
    usagi "He’s a really powerful HEAL class, so he’s probably walking around with max defense buffs at all times GUYS get me OUT OF HERE."
    show jojo neutral at offscreenright
    pause 0
    show usagi at offscreenright
    show sanders neutral at offscreenright
    show takeshi at offscreenright
    show bart at left2
    show jojo at right behind bart
    with ease
    ### page 9 ###
    bart @ grin1 "An interesting development..."
    bart @ scheming "You may yet prove to be useful in righting your wrongs, Kohei...."
    show bart grin1 at right2, flip
    with ease
    show bart at offscreenright, flip
    show jojo at offscreenright, flip
    with ease
    # > RAGNAROK ENDS
    # > BARTHANDELUS WALKS OFF OPPOSITE SIDE OF STAGE WHERE PROFESSOR
    # > JOJO HAS BEEN WATCHING, THEY GREET EACH OTHER AND WALK OFF.
    return

transform hop:
    ypos 880
    easein 0.15 ypos 830
    easeout 0.15 ypos 880