label scene19: 
    scene bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    # scene bg spaceship window
    show layer master at fx.flashback
    show gunner at left, flip
    show officer at right, noflip
    show navigator at right2, noflip
    # show kohei neutral at left2:
        # matrixcolor BrightnessMatrix(0.1)
    show kohei neutral at left2
    with dissolve
    # > 19       INT. THE SPACESHIP EDEN MAIN DECK                                        19
    gunner "Captain, beam array at 60 percent and climbing; Firing window opens in 3 minutes and counting."
    kitadani "Copy that, thank you Gunner Chief, Navigation, a read on the firing zone."
    navigator "Target is in optimal range, blast zone is clear of any civilian ships. No satellites natural or otherwise."
    officer "Captain, I have the secure line ready."
    kitadani "Give me just a second."
    gunner "70 percent."
    navigator "We’re holding steady Captain. Go take your call."

    # > GUIDE US OH MIGHTY FURY...
    # side images: usagi's not visible on screen, so this shows her side image in the textbox
    usagi postgrad neutral focus "On that day, I remember my mom holding for him, our bags were packed and we were ready to go..."
    usagi postgrad neutral focus "Our society had decided that it was going to defy nature itself. We were about to learn a great lesson."

    gunner "80 percent! We’re closing in on the window."
    ### page 35 ###
    navigator "Holding steady."
    kitadani "I’ll take the call in my quarters. First officer, you have the conn."
    # > Rhos an kyn ala na...
    officer "Aye Captain. I have the conn."

    # kohei leaves the room for a moment...
    show kohei:
        xoffset 0
        ease 1 xoffset -800
    pause 1
    show officer:
        alpha 0
    show gunner:
        alpha 0
    show navigator:
        alpha 0
    show bg black
    with dissolve
    show bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    show bg spaceship window
    show kohei neutral at center, flip:
        xoffset -1000
        ease 1.5 xoffset 0
    with dissolve
    kitadani "Just listen to me. I want you and Usagi to take move to our spot in the moon barracks-"
    kitadani "I know it was supposed to be a few more years, but... But this doesn’t look good. If what Barry said is true..."
    kitadani "Just go... I have to get back now. I love you."
    show kohei neutral at center, noflip:
        xoffset 0
        ease 1.5 xoffset -1000
    pause 1
    show bg black
    with dissolve
    show bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    show gunner:
        alpha 1
    show officer:
        alpha 1
    show navigator:
        alpha 1
    with dissolve
    show kohei neutral at left2, flip:
        xoffset -800
        ease 1 xoffset 0

    officer "Captain on Deck"
    gunner "90 percent!"
    navigator "Captain, a development, the Crystal is... opening."
    kitadani "Then this is our chance. That... thing... is coming out again and this time it means to kill us all."
    gunner "100 percent the firing window is open."

    # > Gunner Chief locks and loads the Ultima Canon.
    kitadani "Ready the Ultima Cannon!"
    # > Ecce venio
    kitadani "Today we stand ready to defend all that we hold dear. Our families, our friends, our neighbors and our planet."

    ### page 36 ###
    ### <manga-panels> ###
    # manga panels: fighting the planet destroyer
    window hide
    window auto
    scene bg white with dissolve
    show bg white as bg2 behind bg
    show bg scene19 1 with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    pause
    show bg scene19 2 with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    pause
    show bg scene19 3 with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    pause
    show bg scene19 4 with dissolve:
        # TODO different bg on this one
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.0
        #linear 10 zoom 1.0
    pause
    show bg:
        yshake(5, 1000, 0.02)
    show bg neongreen as boom:
        alpha 0.0
        # pause 0.5
        linear 2.0 alpha 1.0
    pause 2.5
    #destroyer "Behold, I am come, I am the Beginning, And the End."
    #officer "Captain!"
    #kitadani "Steady!"
    #navigator "The PLANET DESTROYER is emerging from the crystal"
    #gunner "Captain on your command!"
    ## > Ecce venio
    #kitadani "FIRE!"
    #gunner "Impact!"
    #navigator "The field is NOT CLEAR, the planet destroyer it-"
    #officer "It absorbed the blast..."
    #gunner "Brace for counter attack!"
    #kitadani "Ready another blast!"
    ### </manga-panels> ###
    # > et principia!

    # > BLACK OUT, SCREEN REVEALS SHOW TITLE/ LOGO “OTAKU ORATORIO 2:
    # > I set out to save the world, but it turns out the world’s
    # > greatest threat is a kid who calls me mom.”
    scene bg beige
    show logo:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.5
    with fade
    pause

    window hide
    window auto
    $ y = 0.48
    scene bg news studio:
        noflip
        anchor (0.5,1.0)
        pos (0.5,1.0)
        zoom 1.15
    show layer master at fx.flashback
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
    # show bg breaking news as bg2:
        # ease 0.5 zoom 1.0
    # show fx_crt_scanlines
    with dissolve
    reporter1 "It is unclear whether or not the crew of the Eden are responding after that...."
    reporter1 "Wait... I’m getting word."
    ### page 37 ###
    reporter2 "It is confirmed, the planet destroyer has been neutralized completely."
    reporter3 "But the Space shuttle Eden and its crew has been decimated in the blast fall out."
    reporter3 "Folks at home, I think now is a time for a moment of silence as we think about the Eden and their sacrifice..."
    # > BARTHANDELUS STOPS THE FOOTAGE. HE HAS BEEN WATCHING THIS OLD
    # > CLASSIFIED RECORDING FOR SOME REASON....

    # transition to bart and tv in a dark room
    scene bg black
    show bg news studio as tv:
        anchor (0.5, 1.0)
        zoom 0.2
        left2
    show fx_crt_scanlines as tv2:
        anchor (0.5, 1.0)
        zoom 0.2
        left2
    show bart neutral focus at right2
    with irisin
    pause 2

    # bart turns off the tv
    show bg news studio as tv:
        linear 1 alpha 0
    show fx_crt_scanlines as tv2:
        linear 1 alpha 0
    pause 2

    # bart leaves
    show bart:
        flip
        xoffset 0
        easeout 2 xoffset 800
    pause 2

    return