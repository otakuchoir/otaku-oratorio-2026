label scene28:
    # https://otaku-oratorio-2026-gallery.netlify.app/?t=bg&t=usagi+young&t=linda
    # show jojo neutral at left
    # show bart neutral at right
    # show kelisha neutral at top
    # > 28       INT. NIGHT; KITADANI RESIDENCE                                           28
    scene bg usagi dorm night
    show usagi young happy at right2
    show linda smile at center, flip
    usagi "That’s my favorite story mom! Thanks! Good night!"
    linda @ happy 2 "Good night little rabbit. Anytime you want to hear the story, let me know."
    show usagi young sleepy focus
    show linda smile focus at flip, fx.ease_xoffset(dur=1.5, x1=-1000)
    pause 1.5

    scene bg living room 2
    show kohei happy at left, flip
    show linda smile at left2, flip, fx.ease_xoffset(dur=1.5, x0=-1000)
    show jojo neutral at right
    show bart happy at right2
    with fade

    # https://otaku-oratorio-2026-gallery.netlify.app/?t=linda&t=kohei&t=jojo&t=bart
    kohei "How was the ten thousandth reading of the legend of Princess Kaguya?"
    linda "Just as thrilling as the last."
    show jojo grin 1
    jojo "So the little one is finally asleep? Let’s get this party started!"
    linda "A small, quiet gathering these days, Joe. It’s always a great time hanging out with you all."
    kohei "It’s just too bad the life of the party couldn’t be here."
    bart "I do hear that the Princess has fully stepped into the role of Queen over there in New Jersey."
    jojo "And doing a great job. Hey... Linda... Now that she has command of her own army... Do you think she’ll sell her mech?"
    show jojo neutral
    linda @ happy 2 "Joe! There’s way too much sentimental value in that."
    ### page 57 ###
    kohei "It’s crazy that the Crown even lets us keep them after graduation!"
    bart "Mine’s in storage. Good ole Alexander, just sitting around collecting dust."
    show jojo grin 1
    linda "Well, you are the newly appointed pope after all... meanwhile I have to stop Kohei here from running errands in his."
    kohei "But picking up groceries is just so much more fun by mech! And don’t worry about Bart, fighting was always against his religion, or so he said..."
    jojo "Hey Bart.... You thinking of selling-"
    show jojo neutral
    bart @ neutral "Don’t even think about it."

    # > Everyone’s holo-device goes off, an alarm similar to an amber
    # > alert or an earthquake warning
    show linda neutral
    show kohei confused
    show bart peaceful
    show jojo neutral
    pause 1
    linda "What the?"
    kohei "What is it?"
    jojo "The Crown is calling us in? Right now?"
    bart @ eyebrow raised "Even me? Why are they sending for me? I’m with the church now."
    kohei "Must be something big if that’s the case, Linda, can you stay with Usagi-"

    # > A knock at the door.
    linda "I’ll get that."
    # > The guys are uneasy.
    show linda at noflip, fx.ease_xoffset(dur=1, x1=-1000)
    pause 1
    show linda neutral at flip:
        pause 0.5
        fx.ease_xoffset(dur=1, x0=-1000)
    show kelisha worried at center, flip, fx.ease_xoffset(dur=0.7, x0=-1000)
    show kohei worried
    show bart worried
    show jojo serious
    ### page 58 ###
    linda "Kelisha? What are you doing here?"
    kelisha "All of you, I need you to come with me right now."
    show linda worried
    show kelisha at noflip
    kelisha "Linda, bring your daughter, we need to be moving in 60 seconds. There’s a transport outside."
    return