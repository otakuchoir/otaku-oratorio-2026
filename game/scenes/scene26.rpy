
label scene26:
    # show takeshi neutral at right2
    # show reporter1 at left
    # show king at right
    # > 26       INT. USAGI’S APARTMENT                                                   26
    # > USAGI AND LINDA ARE ON ANOTHER ONE OF THEIR HOLO-TIME CALLS.

    scene bg living room
    # https://otaku-oratorio-2026-gallery.netlify.app/?t=linda&t=usagi+postgrad
    show linda happy holo at right2
    show usagi postgrad happy 1 at left2, flip
    linda "Yeah, Elizabeth and I ended the fight right there."
    usagi @ postgrad shock "What?"
    show linda happy 2 holo
    linda "They didn’t even get past the first tower. Yeah... It was done after we took Jojo out."
    linda "Your father... He was a good ace... but not as good as me."
    usagi "So you were REAL."
    show linda smile holo
    linda "Well you know what they say. Real recognize real."
    show usagi postgrad happy 3
    usagi "Omg what an old people saying."
    show linda happy holo
    linda "Timeless young lady. Timeless. And speaking of time don’t you have to get to sleep soon?"
    show usagi postgrad happy 1
    usagi "You’re right. Well mom, I’ll call you again later this week."
    show linda happy 2 holo
    linda "Ok little rabbit. Love ya."
    show linda smile holo
    hide linda with dissolve

    # > USAGI HANGS UP ANOTHER CALL IS COMING IN.
    pause
    ### page 50 ###
    # https://otaku-oratorio-2026-gallery.netlify.app/?t=usagi+postgrad&t=sanders+postgrad&t=takeshi+postgrad
    show takeshi postgrad happy 1 holo at right2 with dissolve
    show usagi postgrad happy 2
    usagi "Takeshi? How are YOU doing!?"
    takeshi "Hey Usagi, I’m good. Is now a good time?"
    show usagi postgrad happy 1
    usagi "It’s fine, what’s up? I haven’t heard from you in... gosh how long HAS it been?"
    show takeshi postgrad neutral holo
    takeshi "You haven’t seen the news then?"
    show usagi postgrad neutral
    usagi "Huh? Oh, wait let me check now."

    scene bg news studio
    $ y = 0.48
    show bg news studio behind bg2:
        noflip
        anchor (0.5,1.0)
        pos (0.5,1.0)
        zoom 1.15
    show reporter1:
        zoom 1.0
        xpos 0.2
        ypos y
    show reporter2:
        zoom 1.0
        xpos 0.5
        ypos y+0.03
    show reporter3:
        zoom 1.0
        xpos 0.8
        ypos y
    with irisin
    reporter1 "And here they come now, Colonel Sanders and... Oh it’s the King himself, to deliver the news..."
    hide reporter1
    hide reporter2
    hide reporter3
    show king at center
    with dissolve
    king "Good evening. Tonight I can report to the people of the Earth Moon Federation and all our colonies that the EMF has conducted an operation that killed the leader of the resistance."
    usagi postgrad neutral "But that was..."
    takeshi postgrad worried 1 holo "Yeah and they’ll never name her because they already told everyone she was dead after that mission 3 years ago, but..."
    takeshi postgrad neutral holo "Usagi, I’m so sorry. Your aunt Elizabeth fought until the very end."
    king "Today, at my direction, the EMF launch a targeted operation against a compound in Bakersfield California."
    show king at left2, fx.ease_xpos(dur=1, x0=0.5, x1=0.33)
    show sanders postgrad smug at right2, fx.ease_xoffset(dur=1, x0=1000)
    king "At the head of this operation was Colonel George Sanders."
    ### page 51 ###
    usagi postgrad shock "What the-"
    takeshi postgrad worried 1 holo "Yeah, I wanted to tell you..."
    show sanders postgrad prideful
    king "It is therefore decided that from this moment hence, Sanders will be granted the title of Commander. Congratulations Commander Sanders."

    scene bg living room
    # https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi+postgrad&t=usagi+postgrad
    show usagi postgrad shock at left2, flip
    show takeshi postgrad worried 1 holo at right2
    with irisin
    show usagi postgrad worried
    usagi "...."
    show usagi:
        noflip
        pause 0.3
        flip
        pause 0.3
        repeat 2
    show takeshi postgrad neutral holo
    takeshi "Usagi, I’m sorry. I-"
    show usagi postgrad neutral
    usagi "You need to be careful Takeshi. I know what you’re up to."
    usagi "I’m not joining the resistance. But I’m not going to report you either. Never call here again."
    scene bg black with dissolve
    return