
label scene38:
    scene bg church interior:
        zoom 1.1
        anchor (0.5, 1.0)
        pos (0.45, 1.0)
    show child neutral at left, flip
    show jojo sad at left2, flip
    show usagi postgrad serious 1 at center
    show bart neutral at right
    with fade
    # show sanders neutral at left
    # > 38       INT. DAY; THE HIGH CHURCH                                                38
    ### page 74 ###
    jojo "After that, we were court martialed. But who is anyone kidding? The Crown is the controller of all things."
    jojo "And yet... by some miracle, we weren’t sentenced to death. Instead, we were were gagged... forbidden from talking to each other and forbidden from talking about that day."
    show usagi at flip
    bart "So there you have it. Your answer."
    show child serious
    show bart stern
    bart "For nearly 20 years I have searched for the great resetter not to fulfill divine prophecy, but to end all things. Humanity is not worth saving. Not in this state I-"
    usagi @ angry sweat "My father was one person, and you’re taking it out on billions."
    show bart angry 1
    bart "Billions who suffer daily under the same rule that has flattened you your entire life. That squashes those who would dare defy it like your friend Takeshi Williamson."
    show bart angry 1
    bart "That builds fanatics and warmongers like your friend Commander Sanders..."

    $ dur=1
    show bart sideeye
    pause 0.5
    show bg at fx.ease_xpos(dur, x0=0.45, x1=0.50)
    show bart neutral at flip, fx.ease_xpos(dur, x0=0.83, x1=0.33)
    show sanders postgrad angry 1 at right2, fx.ease_xpos(dur, x0=1.27, x1=0.67)
    show usagi at fx.ease_xoffset(dur, x1=-800)
    show child at fx.ease_xoffset(dur, x1=-800)
    show jojo at fx.ease_xoffset(dur, x1=-800)
    bart "...Speak of the devil."
    show bart grin 1
    sanders "Barthandelus, I am here by order of the King. You are to come with me. You are under arrest for tampering with Crown Military assets and trespassing on Crown Military facilities."

    show bart grin 2
    show bart grin 2 focus at left2, flip as holobart:
        alpha 0.7
    show sanders:
        parallel:
            fx.ease_xpos(dur=0.7, x0=0.67, x1=0.23)
        parallel:
            pause 0.5
            "sanders postgrad shock"
            pause 0.2
            flip
    bart "Unfortunately I won’t be able to come with you, commander Sanders."
    show bart at noflip as holobart
    show bart at noflip:
        alpha 1.0
        linear 1.0 alpha 0.0
    bart "You see... I’m currently aboard The Alexander. I will have a front row seat to the end of the world."
    show bart at noflip as holobart:
        alpha 0.7
        linear 1.0 alpha 0.0
    "Barthandelus's hologram fades."
    return