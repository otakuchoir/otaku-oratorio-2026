# scene 16 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi+postgrad&t=usagi+postgrad&t=sanders+postgrad&t=jojo&t=kelisha&t=bart
label scene16a: 
    # too much clutter with sprites after this, show just the manga panel...?
    # we have to show at least the speaker, though!
    # renpy has a nice solution to that: side images
    scene bg scene16a nofg with dissolve
    pause
    show bg scene16a with dissolve

    # no characters are showing - the attributes here control the side images
    takeshi postgrad neutral "The readings align... This is the wave pattern... I’m pinging the squad."
    # > A deafening sound rings over comms, this isn’t a ping. It’s
    # > something else.
    "PLACEHOLDER sfx" with vpunch
    usagi postgrad shock "Ahhhh what the..."
    sanders postgrad angry 3 "UGHHH MY HEAD.... Stop it WILLIAMSON"
    # > The ringing stops. The crystal stucture is glowing.
    takeshi postgrad panic 1 "It wasn’t me... I don’t know what..."
    # > 
    # > SONG: RAGNAROK    # > 
    # > We start hearing sounds, but they do not make sense. It’s all
    # > dialogue from when Planet Destroyer announced that the Earth
    # > was doomed, to Kitadani attacking planet destroyer, and
    # > everything that ever happened on earth and the moon from then
    # > until right now.
    # > The crystal’s glowing intensifies and reveals the shaped of a
    # > human inside.
    show bg scene16b with dissolve
    sanders postgrad panic "Is that... A person???"
    # > Usagi moves forward.
    takeshi postgrad worried 2 "The planet destroyer."

    # > The crstayl makes a LOUD crack noise, and then another. The
    # > human figure’s eyes open and look directly at Usagi Kitadani.
    window hide 
    window auto
    pause 0
    show bg scene16c with dissolve
    pause 1
    takeshi postgrad panic 2 "No! Usagi, don’t!"
    show bg black # deliberately no transition
    pause 0.5
    # show the sprites over the textbox
    show usagi postgrad worried focus at flip, left2
    show child unamused focus at right2
    # with deliberately no transition
    pause 1
    show child neutral focus at right2
    with dissolve
    # show usagi postgrad shock focus
    pause 2
    show bg black # deliberately no transition, again
    hide usagi
    hide child
    pause 0.5
    # show
    show bg scene16c with dissolve
    bart scheming "At last!"

    ### page 32 ###
    # > FADE TO DARK as the Usagi, Takeshi, and Sanders stand still
    # > in shock, The Planet Destroyer’s gaze locked on Usagi, she
    # > returns the glare without blinking, the soldiers slowly move
    # > in, Jojo, Kelisha and Barthandelus watch in anticipation.
    # > END OF ACT 1
    ### page 33 ###
    # > ACT 2
    jojo grin 1 "Move in and secure the specimen."

    show bg black with dissolve
    return

image side takeshi postgrad neutral focus = Transform(flip(renpy.get_registered_image('takeshi postgrad neutral focus')), crop=(150, 10, 200, 200))
image side takeshi postgrad panic 1 focus = Transform(flip(renpy.get_registered_image('takeshi postgrad panic 1 focus')), crop=(150, 10, 200, 200))
image side takeshi postgrad panic 2 focus = Transform(flip(renpy.get_registered_image('takeshi postgrad panic 2 focus')), crop=(150, 10, 200, 200))
image side takeshi postgrad worried 2 focus = Transform(flip(renpy.get_registered_image('takeshi postgrad worried 2 focus')), crop=(150, 10, 200, 200))
image side usagi postgrad shock focus = Transform(flip(renpy.get_registered_image('usagi postgrad shock focus')), crop=(95, 30, 200, 200))
image side sanders postgrad angry 3 focus = Transform(flip(renpy.get_registered_image('sanders postgrad angry 3 focus')), crop=(130, 0, 200, 280))
image side sanders postgrad panic focus = Transform(flip(renpy.get_registered_image('sanders postgrad panic focus')), crop=(130, 0, 200, 280))
image side bart grin 2 focus = Transform(flip(renpy.get_registered_image('bart grin 2 focus')), crop=(50, 0, 200, 360))
image side bart scheming focus = Transform(flip(renpy.get_registered_image('bart scheming focus')), crop=(50, 0, 200, 360))
image side jojo grin 1 focus = Transform(flip(renpy.get_registered_image('jojo grin 1 focus')), crop=(150, 20, 200, 200))