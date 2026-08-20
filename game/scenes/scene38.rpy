
label scene38:
    scene bg church interior:
        zoom 1.1
        anchor (0.5, 1.0)
        pos (0.45, 1.0)
    show child neutral at left, flip
    show jojo sad at left2, flip
    show usagi postgrad serious 1 at center
    show bart neutral at right
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
    show bart neutral at flip, fx.ease_xpos(dur, x0=0.83, x1=0.23)
    show sanders postgrad angry 1 at right2, fx.ease_xpos(dur, x0=1.27, x1=0.67)
    show usagi at fx.ease_xoffset(dur, x1=-800)
    show child at fx.ease_xoffset(dur, x1=-800)
    show jojo at fx.ease_xoffset(dur, x1=-800)
    bart "...Speak of the devil."
    show bart grin 1
    sanders "Barthandelus, I am here by order of the King. You are to come with me. You are under arrest for tampering with Crown Military assets and trespassing on Crown Military facilities."
    show bart grin 2 at flip:
        pause 0.5
        fx.ease_xoffset(1, x1=1500)
    show sanders:
        pause 1
        flip
    bart "Unfortunately I won’t be able to come with you, commander Sanders."
    $ dur = 1
    show bg:
        zoom 1.1
        linear 1 zoom 1.0
        # parallel:
            # fx.ease_xpos(dur, x0=0.50, x1=0.55)
    show sanders postgrad shock:
        parallel:
            fx.ease_xoffset(dur, x1=-700)
        parallel:
            zoom 1
            linear 1 zoom 0.5
    show bart grin 2 at right2, noflip:
        zoom 1.5
        fx.ease_xoffset(dur, x0=700)
    bart "You see... I’m currently aboard The Alexander. I will have a front row seat to the end of the world."
    show bart at flip:
        parallel:
            fx.ease_xpos(3, x0=0.6, x1=1.3)
        parallel:
            yoffset 0
            pause 0.5
            easeout 2.5 yoffset -1000
        parallel:
            hvibrate(n=100)
    "PLACEHOLDER kaiju bart - waiting for mech assets. Also, very unsure about how I've staged this. Does bart retreat to his mech at the last minute (like I've animated here), or was he in his mech this whole time, or something else?"
    return