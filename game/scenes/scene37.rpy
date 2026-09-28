# https://otaku-oratorio-2026-gallery.netlify.app/?t=bart&t=linda&t=jojo&t=queen
label scene37:
    scene bg black hole
    show layer master at fx.flashback
    show bart mech neutral at right, fx.yoffset(-50), fx.hover(dur=2.9)
    show jojo mech neutral at right2, fx.yoffset(-150), fx.hover(dur=1.9)
    show linda mech worried at left2, fx.yoffset(-200), fx.hover(dur=1.7)
    show queen mech neutral at center, fx.yoffset(-0), fx.hover(dur=2.3)
    with fade

    # > 37       EXT. SPACE                                                               37
    queen "Not gonna lie, Bart... I never thought you’d partake in insubordination like this."
    bart @ mech peaceful "Technically I’m not with the Crown Military anymore, so this is me fulfilling my papal duties."
    show jojo mech sad
    jojo "Still... you could get in HUGE trouble along with the rest of us. The penatly for this kind of defiance is death."
    bart @ mech worried "I know what I’m getting myself into, and I know what I believe... but they can’t just take our best friend and throw him away like this, right?"
    linda "Bart... Thank you."
    show jojo mech serious
    jojo "I have eyes on the Eden. Eden, this is auxiliary unit Carbunkle, do you read me?"
    ### page 73 ###
    show queen mech serious 1
    queen "No use, the comms are jammed... But why?"
    show bart mech worried
    bart "They really sent him on a one way trip, huh..."
    jojo "What’s that? Scanning the space... The crystal is opening. It’s the Planet Destroyer."
    linda "We’re almost there."
    jojo "The Ultima Cannon is charging, it’s about to fire."
    show linda mech serious
    linda "Shiva, moving in."
    call fx.log("sound effects sync - wait 3 seconds; ultima cannon is about to fire")
    queen "Diabolos, right behind you."

    # narrating this is a little boring, but I don't have a better way to show who's firing.
    # > The Ultima Cannon Fires... The Planet Destoryer Counter
    # > Attacks and Blows up the Eden.
    show bg white as bg2:
        alpha 0.7
        easein 5 alpha 0.0
    with vpunch
    show linda mech worried
    show queen mech worried
    show bart mech worried
    show jojo mech sad
    "The ultima cannon fires."
    # sabik's boom is so intense it skips the flashback discoloration ("on layer screens")
    show bg neongreen onlayer screens as bg2:
        alpha 0.8
        easein 5 alpha 0.3
    with vpunch
    show linda mech scared
    show queen mech serious 2
    show bart mech anxious
    show jojo mech crying
    "The Planet Destroyer counter-attacks, and the Eden explodes."
    bart "NO!"
    linda "NO!"
    jojo "ABORT ABORT! THE BLAST RADIUS IT-"

    show linda flip at fx.ease_ypos(dur=2, y1=0.0), fx.ease_xoffset(dur=2, x1=1000)
    show queen flip at fx.ease_ypos(dur=4, y1=2.0), fx.ease_xoffset(dur=2, x1=1300)
    show bart flip at fx.ease_ypos(dur=5, y1=0.0), fx.ease_xoffset(dur=2, x1=1000)
    show jojo flip at fx.ease_ypos(dur=3, y1=2.0), fx.ease_xoffset(dur=2, x1=1000)
    queen "Everyone get the hell outta dodge RIGHT NOW!"
    scene bg black with dissolve
    hide bg2 onlayer screens
    return