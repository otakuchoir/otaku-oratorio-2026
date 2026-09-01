
label scene33:
    scene bg rooftop
    # kagu's flying! but position keywords like "left" assign ypos, so don't use them
    show child happy:
        xpos 0.50
        flip
        ypos ypos_textbox-0.1
        fx.hover
    show usagi postgrad happy 1 at right
    with fade
    # > 33       EXT. USAGI'S APARTMENT - ROOFTOP                                         33
    kagu @ happy 2 "... And then they summoned a bus using the metro card, but insted of hitting him, it revealed the driver, and it was his DAD! Ahh I can’t wait for next week’s episode!"
    usagi @ happy 2"Well, you don’t have to wait, Kagu. All of the episodes are online already."
    kagu "Yes, I understand, but I want to experience it the way you all experienced during its first run, ahhh!"
    usagi @ happy 3 "Fair enough. So, Kagu... what are you going to do next?"
    # > (MORE)
    ### page 66 ###
    show child neutral
    usagi "You’ve been staying here at my place for like... 2 weeks now. What’s next?"
    show usagi postgrad smug
    kagu "Oh, have I overstayed my welcome? Sorry about that. I should have seen this coming earlier but I just evolved to understand social cues."
    # > Holo-time rings
    pause
    show linda smile holo at right2, flip
    with dissolve
    show usagi postgrad happy 1
    usagi "Hey mom."
    linda "Hey Usagi. And how is Kagu doing?"
    show linda at noflip
    kagu @ happy "It’s just like you told me to say: “same old, same old.”"
    usagi "Same ol’ same ol’..."
    linda @ happy holo "I see. You remembered!"
    kagu "Yes! Remember! Wait, why do you accept it when she said it like that, should I say it like that instead?"
    show child unamused:
        noflip
        parallel:
            fx.ease_xpos(dur=0.5, x0=0.5, x1=0.33)
        parallel:
            fx.hover
    # > Kagu starts rehearsing the line over and over again.
    show linda neutral holo at flip
    linda "Usagi, listen... I wanted to let you know... I... this work you’re doing."
    usagi "With Kagu, yeah? What about it?"

    show bg at fx.glitch_lights
    call fx.glitch_child
    show child neutral:
        ypos ypos_textbox-0.1
    linda "You said Professor Jojo was behind it?"
    show child:
        fx.ease_ypos(dur=2, y0=ypos_textbox-0.1, y1=ypos_textbox)
        fx.bowdown(dur=3, a=60, y=-30)
    usagi "Yes, and the pope has a ‘vested interest’..."
    show linda worried holo
    show usagi postgrad neutral
    linda "Jojo and Barthandelus? Just... Be careful. I don’t-"
    usagi "Sorry mom, gotta go, I think Kagu froze up or something."
    linda "Oh, Of course. I’ll talk with you later."

    show linda:
        alpha 1.0
        linear 0.5 alpha 0.0
    show usagi postgrad worried:
        pause 0.5
        fx.ease_xpos(dur=0.5, x0=0.83, x1=0.55)
    usagi "Love you mom, bye. KAGU!"
    hide linda
    # > Kagu is standing still, looking up.
    kagu "I just got my memories back..."
    show usagi postgrad happy 1
    usagi "You evolved again? You remembered?"
    kagu @ sad "Yes... I.... It was up there, I came to... destroy everyone?"
    show usagi postgrad anxious
    usagi "Um..."
    show child:
        noflip
        fx.bowup(dur=0.3, a=60, y=-30)
        block:
            flip
            pause 0.2
            noflip
            pause 0.2
            repeat 2
        flip
    kagu "I... what? What did I do? WHAT DID I DO?"
    show child neutral
    show usagi postgrad sad
    usagi "Kagu! Get a hold of yourself. You’re ok... you’re here with me. Listen. That’s the past. It’s-"
    show child sad with dissolve
    kagu "And you... You knew... Why didn’t you tell me...."
    show child at noflip
    show usagi postgrad worried
    kagu "Oh... your father he... So that’s it? I... Usagi I’m sorry I didn’t mean to I, I -"
    show usagi behind child:
        parallel:
            fx.ease_xpos(dur=0.5, x0=0.55, x1=0.42)
        parallel:
            pause 0.2
            fx.bowdown(dur=0.3, a=-15, y=-35)
    usagi "Kagu, stop! I said, it’s O-K."
    ### page 68 ###
    show usagi postgrad shock:
            fx.bowup(dur=0.1, a=-15, y=-35)
    show child serious at flip:
        fx.ease_xpos(dur=0.15, x0=0.33, x1=0.16)
    kagu "Okay that I blew your dad up and doomed the entire human race to annihilation?? No! That’s NOT ok!"
    show usagi postgrad worried
    usagi "That wasn’t you! It was a past life, remember? We are NOT our pasts. We can only focus on who we are now and what we can do for the future."
    $ dur1 = 2
    $ dur2 = 0.5
    show child sad at flip:
        fx.stretch(1.0, 1.0)
        parallel:
            ease dur1 fx.stretch(1.2, 0.8)
        parallel:
            fx.bowdown(dur=dur1, a=15)
        pause 0
        parallel:
            ease dur2/3 fx.stretch(0.8, 1.2)
        parallel:
            fx.ease_yoffset(dur=dur2, y1=-1000)
        parallel:
            fx.ease_xoffset(dur=dur2, x1=300)
    kagu "WAAAAAH!"
    # > Kagu flies off into space, away from the moon, toward earth,
    # > and finds the spot where the Eden’s wreckage remains.
    return