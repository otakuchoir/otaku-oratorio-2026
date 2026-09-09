
label scene12:
    scene bg earth tarmac at flip:
        zoom 1.0
        pos (0.5, 1.0)
        anchor (0.5, 1.0)
    show shuttle at fx.ease_xyoffset(dur=3.0, xy0=(1500, -400)):
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.35
    with fade
    pause 4.0

    show bg earth tarmac at flip:
        ease 2.0 zoom 1.2
    show shuttle:
        ease 2.0 zoom 1.0 pos (0.5, -0.2)
    show sanders prideful at center, flip, fx.ease_yoffset(dur=2.0, y0=500)
    show usagi weary at left, flip, fx.ease_yoffset(dur=2.0, y0=500)
    show takeshi neutral at right, fx.ease_yoffset(dur=2.0, y0=500)
    with dissolve
    # > 12       EXT. DAY; EARTH, KINGDOM OF NEW JERSEY SPACE PORT                        12
    # > USAGI, TAKESHI AND SANDERS ARE DE-SHUTTLING
    ### page 20 ###
    sanders "You smell that Takeshi!? That’s good ole EARTH air."
    usagi "Oh my GOD. We’re meeting the convoy in 22 minutes. I’m getting something to eat."
    show sanders happy at noflip
    sanders "Can you get me a coffee please!?"
    show usagi neutral
    usagi "Earth’s finest blend, I know."
    show usagi at flip
    show usagi at offscreenleft, noflip
    with ease

    # show sanders at left2
    # show takeshi at right2
    # with ease
    takeshi "Hey, Sanders, do you... have you ever thought of what happens after something like this conflict?"

    show sanders at flip
    sanders "You mean with the New Jersians?"
    takeshi "Yeah."
    show sanders neutral
    sanders "I mean... There’s nothing to think about."
    sanders "They’re rebelling against The Crown. If they don’t comply, they’ll get “corrective stabilization”..."
    show takeshi worried 1
    sanders "They get blown to smithereens. Everyone knows that."
    takeshi "Oh... yeah. And you don’t think thats...?"
    sanders "What?"
    show takeshi annoyed
    takeshi "George, what do you plan on doing after we graduate?"
    sanders @ happy "I’m aiming for the Elites, you know that."
    takeshi "The same squadron we’re observing today."
    show takeshi angry 1
    takeshi "The ones who blow people to smithereens if they don’t listen to the Crown."
    ### page 21 ###
    show sanders angry 1
    sanders "..."
    show takeshi worried 1
    takeshi "I thought after hanging out over the past few-"
    show sanders neutral
    sanders "Hanging out with you guys during my time at the Academy has been a blast. We’re friends, but.. I have a long line of Earth born-"
    takeshi "But you’re not Planeteristic. You’ve learned to distance yourself from that way of thinking."
    show sanders angry 1
    sanders "No, I never agreed to that Williamson. When we met, it was a fight, and Usagi made us get along."
    sanders @ eyeroll "And let’s remember, you and your friends were talking mad shit about me simply for being Earth Born."
    show takeshi angry 1
    takeshi "Only because you and everyone like you looks down on us, yet you’re VISITORS in our colony."
    show sanders angry 1
    sanders "A colony that Earth Born people made..."
    show sanders at noflip 
    sanders "Look, this is an old argument. We’re about to graduate soon, there’s nothing either of us can change, so why don’t we just drop it."
    show sanders at flip 
    show sanders neutral
    sanders "What about you? What exactly do you plan on doing once your out of here?"
    return