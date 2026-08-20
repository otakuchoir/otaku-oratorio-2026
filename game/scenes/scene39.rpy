
label scene39:
    scene bg black
    show bg breaking news as bg2:
        top
        zoom 0.0
        alpha 0.0

        ease 0.5 alpha 1.0 zoom 1.0
    with fade
    pause 1.0
    $ y = 0.48
    scene bg news studio:
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
    hide bg2
    with dissolve
    # > 39       INT. NEWS STUDIO                                                         39
    ### page 75 ###
    reporter1 "Breaking news... the Moon is on a collision course for Earth."
    reporter1 "We’re getting reports that someone has hijacked and reverse engineered the Ultima Cannon..."
    reporter1 "Now, instead of blowing things to smithereens with the power of Ultima... it’s bending gravity to send the moon hurtling into the earth, like a giant meteor that would spell absolute doom for everyone."
    reporter2 "We’re getting reports that a group of Crown Military mechs are in pursuit of the Ultima Cannon, perhaps to stop whatever is unfolding on board..."
    reporter3 "Folks... if you’ve got vacation plans, move them up or get a refund, because if this conflict doesn’t clear up..."
    reporter3 "It doesn’t look like we’ll have a planet or a moon left to visit."
    return