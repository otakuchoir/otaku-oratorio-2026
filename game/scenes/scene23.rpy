# https://otaku-oratorio-2026-gallery.netlify.app/?t=usagi+postgrad&t=child&t=jojo&t=bart
label scene23:
    scene bg research lab inside:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.45, 0.5)
    show jojo neutral at right2
    show usagi postgrad neutral at left2, flip:
        xoffset -800
        ease 1 xoffset 0
    # show child neutral at left
    # > 23       INT. DAY; CROWN MILITARY RESEARCH LAB.                                   23
    jojo "There you are... You’re late."
    usagi "I didn’t know you needed me for anything. After that first mission and all-"
    jojo "These things are sensitive Kitadani, but trust me, it has been for good reason, and it is for good reason now that I have summoned you back."
    ### page 40 ###
    usagi "Don’t get me wrong professor, I’ve actually quite enjoyed my time I-"
    show bart happy at right:
        xoffset 800
        ease 1 xoffset 0
    bart "A being, sent from Heaven. Sent here, to show us the way."
    show usagi postgrad confused
    usagi "I’m sorry... what? Where did you come from-?"
    bart "And the key to its mystery..."
    usagi "Um... I’m just trying to figure out why the pope is here..."
    jojo "The High Prelate has a vested interest in this research, Kitadani, and we believe you are a key factor in all of this."
    usagi "A key factor? How? What does this have to do with me, whatsoever."
    show bart peaceful
    bart "Your father."
    show usagi postgrad annoyed
    usagi "Oh GOD.. I’m sorry I probably shouldn’t say that in front of you like that.. in that manner. I just-"
    # > THE CHILD steps forward, silent.
    show child neutral focus at left:
        flip
        xoffset -800
        ease 1 xoffset 0
    jojo "This... is why we have brought you here."
    show child neutral
    show usagi postgrad shock at noflip:
        fx.hopN(dur=(0.0, 0.3), n=1, y=75, stretch=(0.1, 0.15))
    usagi "You... You were... you’re from that day."
    show usagi postgrad happy 1
    jojo "Yes, this is the being trapped in the crystal you discovered on your first mission 3 years ago."
    jojo "And since then. Since returning here..."
    # > Silence.
    ### page 41 ###
    jojo "It has not spoken a single word."
    usagi "Can it speak?"

    show usagi postgrad smug
    show jojo grin 1:
        fx.hopN(dur=(0.0, 0.3), n=1, y=75, stretch=(0.1, 0.15))
    show bart grin 1
    child "Can it speak?"

    show usagi postgrad happy 1
    jojo "Well I’ll be damned."
    call fx.play_music_in_dev("<from 44.7>bgm_015_bathhouse_morning__spirited_away.opus")
    bart "I TOLD you, the blood of Kitadani runs through this girl, she IS the key."
    show usagi postgrad confused at flip
    show child confused
    # > Professor Jojo and Barthandelus retreat to a side observation
    # > room behind glass.
    show jojo:
        flip
        xoffset 0
        ease 1 xoffset 800
    show bart:
        flip
        xoffset 0
        ease 1 xoffset 800
    usagi "Wait a minute what?"
    hide jojo
    hide bart
    show bg:
        xpos 0.45
        linear 1 xpos 0.55
    show usagi:
        linear 1 xpos 0.59
    show child:
        linear 1 xpos 0.41
    bart neutral focus "Go on then, continue."
    usagi ".... What??"

    # > She stands there, confused. The child is mirroring her. She
    # > realizes this and then focuses on, making slow movements, it
    # > follows, more and more, and then...
    call scene23.child_mirroring
    pause 1
    show usagi postgrad happy 1
    show child happy
    usagi "What is your name?"
    child "What is your name?"
    # > A glitch, the child glitches, energy glitches, lights
    # > flicker.
    show usagi at fx.glitch_lights
    show bg at fx.glitch_lights
    call fx.glitch_child
    show child happy focus at flip
    usagi "My name is Usagi. Usagi Kitadani. What is your name."
    show child happy
    child "My name is. My name is. I have no name. My name is No Name."
    show usagi postgrad neutral
    show child neutral
    usagi "You’ve been here for three years and you have no name?"
    ### page 42 ###
    jojo neutral "Specimen 1. You can call it that?"
    # > She says this with a smile, showing a big sister vibe. The
    # > child mimicks her mood, or is it genuine.
    show usagi postgrad happy 2
    show child happy 2
    usagi "Specimen one? Ok we’ll call you No Name, that’s much more mysterious and cool, don’t you think?"
    child "Haha, I like that. NoName."
    usagi "Pleased to meet you NoName!"
    child "Pleased to meet you NoName!"
    show usagi postgrad happy 1
    show child happy
    usagi "No... I’m Usagi, remember?"
    child "Remember? Ah! Please to meet you Usagi!"
    show usagi postgrad happy 2
    show child happy 2
    # > Quietly behind the glass.
    bart neutral "Wait... No... This is not."
    jojo neutral "Patience my friend... We waited 3 years for ANYthing to happen, and we’ve made it further in the past 3 minutes."
    bart angry 1 "But this is not-"
    jojo neutral "We can redirect later. For now, let her work."
    # > Usagi and NoName have been chatting and are in full blown fun
    # > conversation by now.
    stop music fadeout 2
    jojo neutral "Alright you two, time is up for today, but Usagi will be back tomorrow..."
    show child neutral
    jojo neutral "NoName. Back to your cage."
    show usagi postgrad happy 1
    show child neutral focus at flip
    pause 1.0
    show usagi postgrad neutral
    show child sad focus at flip
    pause 1.0
    # I don't know why the hell this is glitching out and not flipping properly, hide/show to reset
    hide child
    show child sad focus at noflip:
        ytextbox
        xpos 0.41
    show child:
        pause 1
        xoffset 0
        ease 10 xoffset -800
    ### page 43 ###
    # > NoName falls silent and exits. Almost as if a machine
    # > suddenly switched off.
    show usagi postgrad worried
    usagi "Cage?"
    show usagi postgrad serious 1 at flip
    usagi "What do you mean cage? If you’re keeping them in a cage then maybe THAT’S the reason why they hadn’t spoken to you in three-"
    bart shock "While you ARE the key to ALL of this, you MUST not show that thing... you must-"
    jojo "The High Prelate has a vested interest in this research, and while time is important, we do have some to spare."
    jojo "Kitadani, you are to report here tomorrow at the same time. That will be all for now."
    # > Barthandelus looks, but says nothing. Stone faced.
    usagi "Barthandelus- what was that about Kitadani blood? And what about my father?"
    jojo serious "That will be all for now Kitadani. Mind your position."
    # > Usagi exits.
    show usagi:
        xoffset 0
        ease 1 xoffset 800
    pause 1
    show bart angry 1 at left2:
        flip
        xoffset -1200
        ease 2 xoffset 0
    show jojo serious at right2:
        flip
        xoffset -1200
        ease 2 xoffset 0
        noflip
    bart angry 1 "She is the key, Joseph, but she cannot be allowed to..."
    jojo serious "Bart- listen to me. If you really want answers, then you need to let me work. I don’t want to mess this up either."
    jojo neutral "You were right. She has something to do with it because of Kohei. Because she’s Kohei’s daughter."
    bart neutral "Does Linda know?"
    ### page 44 ###
    jojo serious "No. And we don’t need to let her know."
    bart neutral "You’ve made mistakes before Joseph..."
    jojo serious "I have. But experience is the best teacher. We’re not children anymore Bart."
    # > 
    # >          SONG: SILHOUETTE    # > 
    scene bg black with dissolve
    return

label scene23.child_mirroring:
    show usagi postgrad confused focus at noflip
    show child confused focus at flip
    pause 1

    show usagi postgrad neutral focus at noflip
    show child neutral focus at flip
    pause 1

    show usagi postgrad happy 1 focus at noflip
    show child happy focus at flip
    pause 1

    show usagi:
        xoffset 0
        ease 1 xoffset 200
    show child:
        xoffset 0
        ease 1 xoffset -200
    pause 1

    show usagi postgrad serious 1 focus
    show child serious focus
    pause 1

    show usagi postgrad happy 1 focus:
        fx.bowdown(dur=0.5, a=-15)
        pause 0.5
        fx.bowup(dur=0.5, a=-15)
    show child happy focus:
        fx.bowdown(dur=0.5, a=15)
        pause 0.5
        fx.bowup(dur=0.5, a=15)
    pause 2.5

    show usagi postgrad happy 1 focus:
        fx.hopN(n=1, y=70)
    show child happy focus at flip:
        fx.hopN(n=1, y=120)
    pause 1
    show usagi postgrad happy 2 focus at noflip:
        parallel:
            fx.hopN(n=3, y=100)
        parallel:
            xoffset 200
            ease 0.4 xoffset 300
            ease 0.4 xoffset 150
            ease 0.4 xoffset 0
    show child happy 2 focus at flip:
        parallel:
            fx.hopN(n=3, y=300)
        parallel:
            xoffset -200
            ease 0.4 xoffset -300
            ease 0.4 xoffset -150
            ease 0.4 xoffset -0
    pause 1.5
    return