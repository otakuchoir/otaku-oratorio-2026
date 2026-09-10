
label scene27:
    scene bg research lab inside
    show jojo neutral at right2
    show usagi postgrad neutral at left2, flip, fx.ease_xoffset(dur=1, x0=-800)
    with fade
    # > 27       INT. DAY; CROWN MILITARY RESEARCH LAB.                                   27
    jojo "You’re late... again."
    usagi "Train traffic. Sorry for the inconvenience."
    show jojo serious
    jojo "You have a personal escort."
    usagi @ postgrad angry "I won’t be needing commander Sanders’s help further."
    show jojo neutral
    jojo ".... Right... Well then, let’s begin."
    show bart peaceful at right, fx.ease_xoffset(dur=1.5, x0=500)
    show usagi postgrad serious 1 
    bart "A word, Kitadani."
    show usagi:
        flip
        fx.bowdown(dur=0.5, a=30)
        pause 0.5
        fx.bowup(dur=0.5, a=30)
    usagi "Yes, your holiness? How may I entertain your vested interests."
    ### page 52 ###
    show usagi postgrad worried
    bart @ worried "I am sorry for your loss."
    usagi "I... Thank you-"
    show usagi postgrad annoyed
    show bart neutral
    bart "I must also insist that you NOT treat Specimen 1, as a human because it is not a human it is a weapon, and one that we have worked tirelessly to procure."
    show jojo serious:
        flip
        pause 0.3
        noflip
        pause 0.3
        repeat 2
    jojo "What our friend here means to say is that..."
    usagi "A weapon?"
    jojo "An asset. And one that is not of this world Kitadani. One that changes its form to match its surroundings."
    jojo "It only appears as a humanoid child because that is how we can perceive it best."
    usagi "NoName understands me, though."
    bart "Specimen 1... does understand you, more than you realize. Kitadani, Do not treat it as human. Learn everything you can from it, by any- means-necessary."
    usagi "Maybe you two should do a little more explaining. Like what is NoName and what do they have to do with my father? You said they emit a wave pattern that-"
    show bart angry 1
    bart "The Specimen is the thing that killed your father 19 years ago."
    ### page 53 ###
    jojo "Bart-"
    show bart at fx.ease_xpos(dur=1, x0=0.83, x1=0.5)
    bart "There, are you happy now? The specimen is the planet destroyer, a divine manifestation of the Universe’s judgement on our human race. It came from deep space to destroy us all."
    show usagi at noflip
    usagi "Sunday school stories..."
    show bart angry 2 focus:
        fx.hopN(n=1, dur=(0, 0.3), stretch=(0.1, 0.15))
        pause 0.5
        "bart neutral focus"
    bart "Blasphe-.... You can mock it all you want, the proof is there before you, just as it was for us when it appeared all those years ago. It is a weapon, and we need to understand it."
    show bart neutral at flip, fx.ease_xoffset(dur=1.5, x1=1000)
    show jojo at flip, fx.ease_xoffset(dur=1.5, x1=1000)
    pause 2
    hide bart
    hide jojo
    show usagi postgrad happy 1:
        pause 0.8
        flip
    # channeling a hyperactive child...! very animated, lots of running and jumping around.
    # flip + hopN are not compatible - both use xzoom. some animations below are
    # coded a bit awkwardly to work around this, but I think the result looks okay.
    show child happy 2 at right2:
        parallel:
            fx.ease_xoffset(dur=1.5, x0=-1200)
        parallel:
            fx.hopN(dur=(0.0, 0.5), n=3, y=150, flip=True)
        noflip

    # > Barthandelus and Jojo retreat to their observation room.
    # > NoNAME ENTERS
    noname "Hello Usagi."
    usagi "Hello NoName. How are you?"
    show child happy
    noname "I’m NoName."
    usagi "No... HOW are you, not who."
    show child happy 2 at right:
        noflip
        parallel:
            pause 0.8
            flip
        parallel:
            fx.ease_xpos(dur=0.9, x0=0.67, x1=0.16)
            fx.ease_xpos(dur=1.2, x0=0.16, x1=0.83)
        parallel:
            fx.hopN(dur=(0, 0.30), n=3, y=180)
            fx.hopN(dur=(0, 0.30), n=4, y=180, flip=True)
            noflip
    show usagi postgrad happy 2:
        flip
        pause 0.5
        noflip
        pause 1
        flip
    noname "Who are how not you are who."
    show usagi postgrad happy 1
    usagi "Uh oh... That’s ok. Let’s slow down."
    show child happy at right2:
        parallel:
            fx.ease_xpos(dur=3, x0=0.83, x1=0.67)
        parallel:
            fx.hopN(dur=(0.5, 2), n=1, y=250)
    noname "{cps=10}Yes... let’s... slow... down....{/cps}"
    # > NoName sits still.
    ### page 54 ###
    usagi "No, that’s not what I- ... NoName... just listen. Today I’m going to tell you the story of Princess Kaguya."

    show usagi focus at left, fx.ease_xpos(dur=1.0, x0=0.33, x1=-0.15)
    show child neutral focus at right, fx.ease_xpos(dur=1.0, x0=0.67, x1=1.15)
    # > Time lapse
    show kaguya behind usagi, child:
        xsize 1440
        xalign 0.5
        yalign 1.30
        alpha 0.0
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            pause 2.0
            linear 30.0 yalign 0.0
    show bg black as kaguyabg behind kaguya:
        alpha 0.0
        linear 1.0 alpha 1.0
    usagi "Once, an old bamboo cutter found a tiny princess glowing inside a stalk of bamboo."

    # > Time lapse
    show kaguya:
        linear 24.0 yalign 0.0
    #show child: 
    #    parallel:
    #        fx.hopN(n=1, dur=(0.1, 0.2), stretch=(0.05, 0.1))
    #    parallel:
    #        fx.ease_xpos(dur=0.3, x0=0.67, x1=0.62)
    usagi "He and his wife raised her as their own. She grew into someone beautiful and strange, and everyone wanted something from her."

    show kaguya:
        linear 16.0 yalign 0.0
    #show child: 
    #    parallel:
    #        fx.hopN(n=1, dur=(0.1, 0.2), stretch=(0.05, 0.1))
    #    parallel:
    #        fx.ease_xpos(dur=0.3, x0=0.62, x1=0.56)
    usagi "But Princess Kaguya was not from Earth. She had come from the Moon, and one day, the Moon people came to take her home."

    show kaguya:
        linear 8.0 yalign 0.0
    #show child: 
    #    parallel:
    #        fx.hopN(n=1, dur=(0.1, 0.2), stretch=(0.05, 0.1))
    #    parallel:
    #        fx.ease_xpos(dur=0.3, x0=0.56, x1=0.50)
    usagi "And even though the people who loved her begged her to stay, she could not. She belonged to the sky before she ever belonged to them."

    show usagi at left2, fx.ease_xpos(dur=1.0, x0=-0.15, x1=0.33)
    show child neutral at center, fx.ease_xpos(dur=1.0, x0=1.15, x1=0.50)
    hide kaguyabg
    show kaguya:
        alpha 1.0
        linear 1.0 alpha 0.0
    noname "Wooooowwwww.... So where is Princess Kaguya now?"
    usagi "It’s just a story but... Well you know, we found you here on the moon."
    hide kaguya
    show child at center, fx.hopN(n=1, dur=(0, 0.3), y=75, stretch=(0.1, 0.15))
    noname "Me? So I’m like Princess Kaguya?"
    usagi "In a way, I guess so. Only... well, where do you come from? Do you have a mom?"
    show child confused:
        fx.bowdown(dur=1, y=-15, a=15)
        pause 0.5
        fx.bowup(dur=1, y=-15, a=15)
    noname "Where I’m from? A mom.... Mother?"
    usagi "Yes! Exactly."

    jojo grin 1 "I told you... Let her work."
    ### page 55 ###
    bart eyebrow raised "Absolutely profound...."

    show child happy
    noname "I... Guess I’m from the moon. This moon."
    show child happy 2
    noname "You woke me up. You are my mom!"
    bart worried "Its vocabulary... It has increased substantially simply by listening..."
    jojo grin 2 "Intelligence growth is exponential."

    usagi "Well, I don’t think that’s how it works but OK! Call me mom! Since I’m your mom for now... I think we should give you a REAL name."

    bart shock "WHAT?" with vpunch
    jojo serious "Shhhhh..."
    bart angry 2 "A name Joseph? A sense of identity??"
    jojo serious "Please Bart."

    usagi "Kagu. Just like in the story. Your name will be Kagu!"
    show child happy at center:
        fx.hopN(dur=(0.1, 0.2), n=2, y=100, stretch=(0.15, 0.2))
        pause 0.5
        "child happy 2 focus"
        parallel:
            fx.bowdown(dur=0.3, y=50, a=-15)
        parallel:
            fx.ease_xoffset(dur=0.3, x1=-100)
        pause 0.8
        parallel:
            fx.bowup(dur=0.3, y=50, a=-15)
        parallel:
            fx.ease_xoffset(dur=0.3, x0=-100)
        "child happy focus"
    show usagi postgrad happy 1:
        pause 1.2
        "usagi postgrad happy 2 focus"
        parallel:
            fx.bowdown(dur=0.3, y=-20, a=15)
        parallel:
            fx.ease_xoffset(dur=0.3, x1=70)
        pause 0.8
        parallel:
            fx.bowup(dur=0.3, y=-20, a=15)
        parallel:
            fx.ease_xoffset(dur=0.3, x0=70)
        "usagi postgrad happy 1"
    call fx.log("don't click through too fast here. Let them finish their hug!")
    kagu "I like that name! Kagu. I am Kagu. Thanks Mom!"

    # > BARTHANDELUS AND JOJO EMERGE FROM THEIR OBSERVATION ROOM
    show bart angry 1 at right, fx.ease_xoffset(dur=1, x0=800) behind usagi
    show jojo serious at right2, fx.ease_xoffset(dur=1, x0=800) behind usagi
    show child neutral at flip
    show usagi postgrad neutral
    jojo "That will be all for today."

    show jojo serious 2
    show usagi postgrad happy 3 at flip
    show child unamused at flip
    kagu "(mocking) That will be all for today."
    show usagi postgrad happy 1 at flip
    show child happy at noflip
    usagi "Kagu, you’re funny."
    ### page 56 ###
    show jojo serious
    show bart stern
    bart "Kitadani, might I remind you-"
    show usagi at fx.ease_xoffset(dur=2, x1=1200)
    show child neutral:
        parallel:
            fx.ease_xoffset(dur=1.5, x1=-1200)
        parallel:
            fx.hopN(dur=(0, 0.30), n=5, y=150, stretch=(0.15, 0.2))
    show bart:
        pause 1
        flip
        "bart angry 2"
    kagu "Thank you, Mom! Good night!"
    return