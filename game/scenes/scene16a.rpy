# scene 16 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi+postgrad&t=usagi+postgrad&t=sanders+postgrad&t=jojo&t=kelisha&t=bart
label scene16a: 
    # too much clutter with sprites after this, show just the manga panel...?
    # we have to show at least the speaker, though!
    # renpy has a nice solution to that: side images
    scene bg scene16 1 nofg with dissolve
    # show bg scene16 1 with dissolve

    # no characters are showing - the attributes here control the side images
    takeshi postgrad neutral "The readings align... This is the wave pattern... I’m pinging the squad."
    # > A deafening sound rings over comms, this isn’t a ping. It’s
    # > something else.
    usagi postgrad shock "Ahhhh what the..." with vpunch
    sanders postgrad angry 3 "UGHHH MY HEAD.... Stop it WILLIAMSON"
    # > The ringing stops. The crystal stucture is glowing.
    takeshi postgrad panic 1 "It wasn’t me... I don’t know what..."
    # > 
    call scene16.credits
    # > SONG: RAGNAROK    # > 
    # > We start hearing sounds, but they do not make sense. It’s all
    # > dialogue from when Planet Destroyer announced that the Earth
    # > was doomed, to Kitadani attacking planet destroyer, and
    # > everything that ever happened on earth and the moon from then
    # > until right now.
    # > The crystal’s glowing intensifies and reveals the shaped of a
    # > human inside.
    show bg scene16 2 nofg with dissolve
    sanders postgrad panic "Is that... A person???"
    # > Usagi moves forward.
    takeshi postgrad worried 2 "The planet destroyer."

    # > The crstayl makes a LOUD crack noise, and then another. The
    # > human figure’s eyes open and look directly at Usagi Kitadani.
    window hide 
    window auto
    pause 0
    show bg scene16 3 nofg with dissolve
    pause
    show usagi mech postgrad neutral at left, flip, fx.ease_xoffset(2.0, x0=-800), fx.yoffset(300) behind scene16_credits01
        # zoom 0.10
        # pos (0.1, -0.3)
        # ease 3.0 zoom 0.4 pos (0.2, 0.26)
    takeshi postgrad panic 2 "No! Usagi, don’t!"
    hide usagi
    show bg black # deliberately no transition
    pause 0.5
    # show the sprites over the textbox
    define z = 1.3
    show usagi postgrad worried focus at flip, left2 behind scene16_credits01:
        zoom z
    show child unamused focus at right2 behind scene16_credits01:
        zoom z
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
    show bg scene16 3 nofg
    show usagi mech postgrad neutral at left, flip, fx.yoffset(300) behind scene16_credits01
    with dissolve

    bart scheming "At last!"
    # dim versions of these on purpose. focus on the crystal!
    show takeshi mech postgrad neutral behind scene16_credits01:
        flip
        zoom 0.2
        pos (0.20, 0.26)
        fx.ease_xyoffset(5.0, xy0=(-800, -100))
    show sanders mech postgrad neutral behind scene16_credits01:
        flip
        zoom 0.2
        pos (0.30, 0.23)
        fx.ease_xyoffset(5.0, xy0=(-800, -100))
    # alias these so we see their side images - they're too small and far away to emote here
    show jojo mech neutral as j behind scene16_credits01:
        zoom 0.2
        pos (0.7, 0.23)
        fx.ease_xyoffset(5.0, xy0=(800, -100))
    show bart mech neutral as b behind scene16_credits01:
        zoom 0.2
        pos (0.8, 0.29)
        fx.ease_xyoffset(5.0, xy0=(800, -100))
    show kelisha mech neutral behind scene16_credits01:
        zoom 0.2
        pos (0.9, 0.29)
        fx.ease_xyoffset(5.0, xy0=(800, -100))
    jojo grin 1 "Move in and secure the specimen."
    window hide
    window auto

    ### page 32 ###
    # > FADE TO DARK as the Usagi, Takeshi, and Sanders stand still
    # > in shock, The Planet Destroyer’s gaze locked on Usagi, she
    # > returns the glare without blinking, the soldiers slowly move
    # > in, Jojo, Kelisha and Barthandelus watch in anticipation.
    # > END OF ACT 1
    ### page 33 ###
    # > ACT 2

    # my usual trick of mirroring the background to get more space doesn't work well here...!
    #show bg scene16 1 nofg at truecenter:
    #    zoom 0.5
    #show bg scene16 1 nofg as bgright at truecenter:
    #    flip
    #    zoom 0.5
    #    xoffset 1440/2
    #show bg scene16 1 nofg as bgleft at truecenter:
    #    flip
    #    zoom 0.5
    #    xoffset -1440/2

    call fx.log("Next click is the end of act 1! Pause here until choir finishes singing.")
    call fx.log("Clicking will skip the credits, if they're not done.")
    call fx.log("ragnarok is 3:30, credits are about 3 minutes and start shortly after ragnarok")
    pause

    scene bg black with dissolve
    return

style ed_role:
    size 30
style ed_who:
    size 60

init python:
    scene16_credits_txt = [
        "",
        "\n\n{=ed_role}Writer{/}\n{=ed_who}Johnathan Gibbs{/}",
        "\n\n{=ed_role}Director{/}\n{=ed_who}Danny{/}",
        "\n\n{=ed_role}Assistant Director{/}\n{=ed_who}Silvia{/}",
        "\n\n{=ed_role}BGM Music Supervisor{/}\n{=ed_who}Nathan Li{/}",
        "\n\n{=ed_role}BGM Assistant Supervisor{/}\n{=ed_who}Abraham \"AJ\" Rogers Lopez{/}",
        "\n\n{=ed_role}Sound Effects Supervisors{/}\n{=ed_who}Ko Tanaka\nNathan Li{/}",
        "\n\n{=ed_role}Visual Novel Operator{/}\n{=ed_who}Kyle Navarro{/}",
        "\n\n{=ed_role}Visual Novel Engineer/Animator{/}\n{=ed_who}Evan Rosson{/}",
        "\n\n{=ed_role}Logo Design{/}\n{=ed_who}Abraham \"AJ\" Rogers Lopez{/}",
        "\n\n{=ed_role}Manga Panelist{/}\n{=ed_who}Alice{/}",
        "\n\n{=ed_role}Eyecatches{/}\n{=ed_who}Miffy\nAbraham \"AJ\" Rogers Lopez{/}",
        "\n\n{=ed_role}Scene Artists{/}\n{=ed_who}Shiana\nElaine\nConnor \"Bear\" Barre\nMiffy{/}",
        "\n\n{=ed_role}Sprite Artist{/}\n{=ed_who}Pierce{/}",
    ]
    for i, t in enumerate(scene16_credits_txt):
        renpy.image(f"scene16_credits{i:02d}", Text(t, style="op_text_s"))
    # credits should be about 2 minutes. ragnarok is 3:30ish, and credits start around 1:30
    scene16_credits_dur = 180.0 / len(scene16_credits_txt)

label scene16.credits:
    # call fx.log("Ragnarok is playing. Try to match the end of the credits to the end of the song. 13 more clicks until the end of these credits.")
    show scene16_credits01:
        xalign 0.5
        yalign 0.0
        # there must be a better way to do this, but hell if I know what it is. DynamicImage, I think - but where's the sleep() go?
        alpha 1.0
        "scene16_credits01"
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits02"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits03"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits04"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits05"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits06"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits07"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits08"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits09"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits10"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits11"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits12"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
        "scene16_credits13"
        linear 0.5 alpha 1.0
        pause scene16_credits_dur
        linear 0.5 alpha 0.0
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    ## call fx.log("10 more clicks until the end of these credits.")
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    ## call fx.log("5 more clicks until the end of these credits.")
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause
    #show op_text  at top
    #with dissolve
    #pause


