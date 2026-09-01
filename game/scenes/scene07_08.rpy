label scene07: 
    scene bg classroom:
        zoom 1.1
        anchor (0.0, 0.0)
        pos (-0.05, 0.0)
    call fx.play_music_in_dev("bgm_006_nonbiri_seikatsu__nichijou.opus")
    show jojo neutral at right2
    show takeshi neutral at left2, flip
    show sanders neutral at left, flip
    with dissolve
    # > 7        INT. CROWN MILITARY ACADEMY, CLASSROOM                                    7
    jojo "Listen up. I have 3 minutes left and we’re on the last chapter. This will be part of your midterm tomorrow. What do the Domes do?"
    takeshi "They are walls regulate atmosphere and temperature, filtering out the toxins in the air released after the Cataclysm Era, Sir."
    jojo "Good. But not walls, they are stabilizers. Language matters."
    jojo "And who can tell me about the Cataclysm Era? Sanders?"
    sanders "During the Cataclysm Era, there was chaos with widespread scarcity, conflict, and volatility, Sir."
    sanders "Existing governments failed to respond effectively. The Emergency Mandate reorganized the system into the Stabilized Democracy that we have today."
    # > PROJECTOR:
    # > “THE CATACLYSM ERA -> EMERGENCY MANDATE -> STABILIZED DEMOCRACY
    jojo "Excellent work, Sanders. Like biology, our institutions had to evolve to meet the needs of its environment."
    ### page 13 ###
    jojo "Today is the anniversary of the Eden Incident. Who could tell me what happened during the Eden Incident?"
    show usagi neutral at left, flip:
        xoffset -300
    pause 0
    show bg classroom:
        xpos 0.0
    show jojo neutral at right
    show takeshi neutral at center, flip
    show sanders neutral at left2, flip
    show usagi neutral at left, flip:
        xoffset 0
    with ease
    return

label scene08:
    show bg classroom
    show jojo neutral at right
    show takeshi neutral at center, noflip
    show sanders neutral at left2, noflip
    # > 8        EVERYONE TURNS TO LOOK AT USAGI                                           8
    jojo manic "Usagi, daughter of the hero Kitadani. Would you like to answer? What happened during Eden?"
    usagi "Eden was a tragedy that was a containment action that prevented the collapse of humanity."
    # > (claps, then the class follows)
    # > (voice cracks like he’s about to cry)
    show jojo fervent at fx.hopN(n=2, stretch=(0.1,0.15))
    show usagi annoyed
    jojo "Excellent! So beautiful. Your father would be so proud. Thank you for your service."
    usagi "It wasn’t my service... it was... my Father’s service."
    show usagi serious 2
    usagi "Please stop thanking me for things I haven’t done. I don’t speak for my father."
    jojo manic "One day you will appreciate what your father did for humanity..."
    jojo crying "Or perhaps... I am out of line. My apologies... Kitadani."
    show usagi annoyed
    jojo serious "Class dismissed."
    show jojo at right:
        flip
        xoffset 0
        ease 1 xoffset 500
    show takeshi neutral at center:
        noflip
        xoffset 0
        ease 2 xoffset -1000
    show sanders neutral at left2:
        noflip
        xoffset 0
        ease 2 xoffset -1000
    show usagi annoyed at left, noflip:
        xoffset 0
        ease 2 xoffset -1000
    pause 0.5
    scene bg black with dissolve
    return