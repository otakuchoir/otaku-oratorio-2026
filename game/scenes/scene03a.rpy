# actors blocking doc: https://docs.google.com/document/d/1TY9hcwGGRmYvBaMOoS-97qJit_nVjHjjL2uWjPJ6IAI/edit?tab=t.0
# VN intros must match this doc, because we're coordinating with IRL actor intros on stage
#
# butterfly (opening song): https://drive.google.com/drive/folders/1evUgNs8aIYA3xyqH5VKsJsvkrswmVLGP

label scene03a: 
    window hide
    window auto

    call op.logo
    window hide
    window auto
    call fx.log("Butter-fly is 5 minutes long. We have 18 actor intros = 16-ish seconds per intro")
    call fx.log("0/17 intros")
    call op.trio
    call fx.log("3/17 intros (takeshi)")
    # call op.usagi
    # call op.sanders
    # call op.takeshi
    call op.kagu
    call fx.log("4/17 intros (kagu)")
    call op.kohei_linda_jojo_bart
    call fx.log("8/17 intros (bart)")
    call op.kelisha
    call fx.log("9/17 intros (kelisha)")
    call op.queen_huxtable
    call fx.log("11/17 intros (huxtable)")
    call op.destroyer
    call fx.log("12/17 intros (destroyer)")
    call op.gunner
    call fx.log("13/17 intros (gunner)")
    call op.wellington
    call fx.log("14/17 intros (wellington)")
    call op.reporters
    call fx.log("17/17 intros (reporters)")
    call op.choir
    return

style op_text_s:
    # "Outlines only work when applied to an entire Text displayable. They do not work when applied to a hyperlink, text tag, or other method that applies to only a portion of the text."
    # https://www.renpy.org/doc/html/style_properties.html
    #
    # so we must apply this separately.
    size 20
    textalign 0.5
    outlines [(5, '#000', 0, 0)]
image op_text = ParameterizedText(style='op_text_s')
style op_starring:
    size 50
style op_actor:
    size 80
style op_as:
    size 30
style op_char:
    size 80

# define op.intro_dur = 5
define op.intro_dur = None

#################################################################

label op.logo:
    scene bg black
    show bg beige as bglogo:
        anchor (0.5, 0.0)
        pos (0.5, 0.0)
    show logo:
        zoom 0.5
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with dissolve
    pause op.intro_dur
    return

transform op.trio_run_1:
    zoom 1.5
    xoffset 1200
    parallel:
        easein 1.0 xoffset 300
    parallel:
        # interrupt the easing above, so there's no dead stop, just a slowdown
        pause 0.6
        easein 7.4 xoffset -300

transform op.trio_run_2:
    easeout 1.0 xoffset -1200

label op.trio:
    scene black
    call fx.bgloop_x('bg countryside', dur=3.0)

    # scene bg usagi dorm night
    show usagi happy 2 focus at bottom, op.trio_run_1
    show op_text "\n\n{=op_actor}Sophia Chan{/}\n{=op_as}as{/}\n{=op_char}Usagi Kitadani{/}" at top
    with dissolve
    pause op.intro_dur
    call fx.log("1/17 intros (usagi)")
    show usagi at op.trio_run_2
    pause 0.0

    # scene bg countryside
    show sanders angry 1 focus at bottom, op.trio_run_1
    show op_text "\n\n{=op_actor}Chomp{/}\n{=op_as}as{/}\n{=op_char}George Sanders{/}" at top
    with dissolve
    pause op.intro_dur
    call fx.log("2/17 intros (sanders)")
    show sanders at op.trio_run_2
    pause 0.0

    # scene bg cubicles
    show takeshi worried 2 focus at bottom, op.trio_run_1
    show op_text "\n\n{=op_actor}Geoffery Shlapak{/}\n{=op_as}as{/}\n{=op_char}Takeshi Williamson{/}" at top
    with dissolve
    pause op.intro_dur
    show takeshi at op.trio_run_2
    pause 1.0
    return

label op.kagu:
    scene bg lunar surface
    show op_text "\n\n{=op_actor}Jalisha Paz{/}\n{=op_as}as{/}\n{=op_char}The Child{/}" at top
    show child mech neutral focus flip at bottom behind op_text:
        zoom 1.5
        pos (-0.1, 1.2)
        rotate 0
        ease 1.0 rotate 30
    with dissolve
    pause 1.0
    show child mech happy 2 focus flip:
        parallel:
            fx.hopN(dur=(0.05, 0.3), n=4, stretch=(0.1, 0.1), y=300)
        parallel:
            ease 0.8 rotate 0
        parallel:
            ease (0.4*3) pos (0.5, 1.2)
    pause 2.0
    show child mech happy 2 focus flip:
        rotate 0
        pos (0.5, 1.2)
    pause 1.0
    pause op.intro_dur
    show child mech happy focus flip:
        parallel:
            fx.hopN(dur=(0.2, 2.0), n=1, stretch=(0.2, 0.3), y=3000)
        parallel:
            rotate 0
            ease 0.4 rotate 15
        parallel:
            xoffset 0
            pause 0.1
            ease 2.0 xoffset 2400
    pause 1.0
    return

label op.kohei_linda_jojo_bart:
    scene bg black
    # call fx.bgloop_x(Transform('bg moon and earth', zoom=1440.0/1280.0), dur=30)
    call fx.bgloop_x(Transform('bg black hole', zoom=1440.0/1280.0), dur=30)
    show bg spaceship window transparent as bg2
    show kohei panic 1 focus at left2:
        zoom 2.0
        pos (0.35, 1.0)
        fx.ease_xoffset(dur=2.0, x0=1400)
    show op_text "\n\n{=op_actor}Erin-Marquise Watson{/}\n{=op_as}as{/}\n{=op_char}Kohei Kitadani{/}":
        anchor (0.5, 0.0)
        pos (0.35, 0.0)
    with dissolve
    pause 1.8
    show kohei panic 2 focus at flip
    pause 0.2
    show kohei panic 1 focus
    pause 0.2
    show kohei panic 2 focus
    pause 0.2
    show kohei panic 1 focus
    pause 0.2
    show kohei panic 2 focus at noflip
    pause 0.2
    show kohei panic 1 focus
    pause 0.2
    show kohei panic 2 focus
    pause 0.2
    show kohei panic 1 focus
    pause 0.2
    pause 3.0
    show kohei:
        fx.ease_xoffset(dur=2.0, x1=-1400)
    pause 1.5

    scene bg campus
    show kohei young kyaa focus:
        transform_anchor True
        flip
        zoom 2.0
        pos (0.38, 1.0)
        parallel:
            fx.ease_xoffset(2.0, x0=-1400)
        parallel:
            rotate 0
            yoffset 0
            pause 1.5
            ease 0.5 rotate 15 yoffset 0
    show linda young happy:
        transform_anchor True
        zoom 2.0
        pos (0.65, 1.0)
        parallel:
            fx.ease_xoffset(2.0, x0=1400)
        parallel:
            rotate 0
            yoffset 0
            pause 1.5
            ease 0.5 rotate -15 yoffset 100
    show op_text "\n\n{=op_actor}Erin-Marquise Watson{/}\n{=op_as}as{/}\n{=op_char}Kohei Kitadani{/}":
        anchor (0.5, 0.0)
        pos (0.35, 0.0)
    with dissolve
    pause 1.0
    show kohei young kyaa focus
    show linda young kyaa
    pause op.intro_dur

    call fx.log("5/17 intros (kohei)")
    show kohei young kyaa
    show linda young kyaa focus
    show op_text "\n\n{=op_actor}Rahanna Brown{/}\n{=op_as}as{/}\n{=op_char}Linda Kitadani{/}":
        anchor (0.5, 0.0)
        pos (0.65, 0.0)
    with dissolve
    pause 4.0
    show kohei:
        ease 0.5 rotate 0
        fx.ease_xoffset(2.5, x1=1400)
    show linda:
        ease 0.5 rotate 0
        flip
        fx.ease_xoffset(2.5, x1=1400)
    pause 2.0

    scene bg training room:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.45, 0.55)
    show linda mech serious focus flip:
        zoom 0.95
        pos (-0.3, 0.72)
        linear 3.0 xpos 1.3
    show jojo mech sad flip:
        zoom 1.5
        pos (0.3, 1.3)
        linear 4.5 xpos 0.5
    show op_text "\n\n{=op_actor}Rahanna Brown{/}\n{=op_as}as{/}\n{=op_char}Linda Kitadani{/}":
        anchor (0.5, 0.0)
        pos (0.65, 0.0)
    with dissolve
    pause 0.7
    show jojo mech sad -flip
    pause 0.2
    show linda mech serious focus -flip
    pause 2.0
    show linda:
        zoom 1.5
        pos (1.5, 1.2)
        rotate 45
        parallel:
            easein 0.7/2 ypos 0.4
            easeout 0.7/2 ypos 1.2
        parallel:
            pause 0.4
            ease 0.7/2 rotate 0
        parallel:
            linear 0.7 xpos 0.5
    show jojo behind linda
    pause 0.5
    show jojo mech crying:
        rotate 0
        ypos 1.3
        easein 0.20 rotate -90 ypos 1.4 xpos 0.3
    pause 1.0
    show linda mech smile focus

    pause op.intro_dur
    call fx.log("6/17 intros (linda)")
    show op_text "\n\n{=op_actor}Abraham \"AJ\" Rogers Lopez{/}\n{=op_as}as{/}\n{=op_char}Professor Joseph \"Jojo\" Chen{/}":
        anchor (0.5, 0.0)
        pos (0.5, 0.0)
    # with dissolve
    show linda -focus:
        ease 1.0 xoffset 800 yoffset -400
    show jojo focus:
        ease 1.0 xoffset 800 yoffset -400
    show bg training room:
        pos (0.45, 0.55)
        ease 1.0 pos (0.55, 0.45)
    pause 3.0

    scene bg classroom:
        zoom 1.1
        yalign 1.0
        xalign 1.0
        linear 6.0 xalign 0.0
    show sanders neutral at flip:
        zoom 0.5
        pos (0.32, 0.58)
        linear 6.0 xpos 0.42
    show usagi neutral at flip:
        zoom 0.5
        pos (0.23, 0.6)
        linear 6.0 xpos 0.33
    show takeshi neutral at flip:
        zoom 0.5
        pos (0.09, 0.62)
        linear 6.0 xpos 0.19
    show jojo neutral focus:
        zoom 2.0
        pos (0.7, 1.0)
        linear 6.0 xpos 0.8
    show op_text "\n\n{=op_actor}Abraham \"AJ\" Rogers Lopez{/}\n{=op_as}as{/}\n{=op_char}Professor Joseph \"Jojo\" Chen{/}" at top
    with dissolve
    pause 6.0

    scene bg research lab inside:
        zoom 1.1
        xalign 1.0
        yalign 1.0
    show bart happy:
        flip
        pos (0.15, 1.0)
        zoom 1.8
    show jojo fervent focus:
        pos (0.65, 1.0)
        zoom 1.8
        fx.hopN(n=10, stretch=(0.05, 0.08))
    show op_text "\n\n{=op_actor}Abraham \"AJ\" Rogers Lopez{/}\n{=op_as}as{/}\n{=op_char}Professor Joseph \"Jojo\" Chen{/}" at top
    with dissolve
    pause op.intro_dur

    call fx.log("7/17 intros (jojo)")
    show bg research lab inside:
        xalign 1.0
        ease 2.0 xalign 0.0
    show bart happy focus
    show jojo fervent -focus
    show op_text "\n\n{=op_actor}Connor \"Bear\" Barre{/}\n{=op_as}as{/}\n{=op_char}Bartholomew Barthandelus{/}":
        anchor (0.5, 0.0)
        pos (0.40, 0.0)
    with dissolve
    show bart:
        xpos 0.15
        ease 2.0 xpos 0.35
    show jojo:
        xpos 0.65
        ease 2.0 xpos 0.85
    pause 4.0
    show bart grin 1 focus at noflip
    pause 1.0

    scene bg church interior
    show bart worried focus:
        transform_anchor True
        pos (0.65, 1.0)
        zoom 2.0
        rotate 0
        parallel:
            easein 4.0 xpos 0.35
            pause 1.0
            flip
        parallel:
            pause 6.0
            ease 0.5 rotate 10
    # show bart faceless pray focus as barthands:
    show barthands:
        transform_anchor True
        anchor (0.5, 1.0)
        pos (0.65, 1.0)
        zoom 2.0
        rotate 0
        alpha 0.0
        parallel:
            easein 4.0 xpos 0.35
            pause 1.0
            flip
        parallel:
            pause 6.0
            ease 0.5 rotate 10
        parallel:
            pause 6.0
            linear 0.5 alpha 1.0
    show op_text "\n\n{=op_actor}Connor \"Bear\" Barre{/}\n{=op_as}as{/}\n{=op_char}Bartholomew Barthandelus{/}":
        anchor (0.5, 0.0)
        pos (0.40, 0.0)
    with dissolve
    pause 5.0
    with dissolve

    pause op.intro_dur
    return

image barthands:
    xysize (308, 475) # crop just the hands, but without changing image size so transforms match bart
    contains:
        "bart faceless pray focus"
        crop (0, 325, 308, 150)
        anchor (0.0, 0.0)
        pos (0, 325)

label op.kelisha:
    scene bg classroom:
        flip
        zoom 1.1
        yalign 1.0
        xalign 0.0
        linear 6.0 xalign 1.0
    show sanders eyeroll:
        zoom 0.5
        pos (1-0.32, 0.58)
        linear 6.0 xpos 1-0.42
    show usagi happy 2:
        zoom 0.5
        pos (1-0.23, 0.6)
        linear 6.0 xpos 1-0.33
    show takeshi happy 1:
        zoom 0.5
        pos (1-0.09, 0.62)
        linear 6.0 xpos 1-0.19
    show kelisha stinkeye focus at flip:
        zoom 2.0
        pos (1-0.7, 1.0)
        linear 6.0 xpos 1-0.8
    show op_text "\n\n{=op_actor}Ashley Foster{/}\n{=op_as}as{/}\n{=op_char}Professor Kelisha Alvarez{/}" at top
    with dissolve
    pause 6.0

    scene black
    call fx.bgloop_x('bg moon and earth', dur=-31.0)
    show bg kelisha office transparent windows:
        zoom 1.1
        yalign 0.5
        xalign 0.0
        easein 6.0 xalign 1.0
    show op_text "\n\n{=op_actor}Ashley Foster{/}\n{=op_as}as{/}\n{=op_char}Professor Kelisha Alvarez{/}" at top
    show takeshi postgrad worried 1:
        flip
        zoom 1.7
        pos (0.10, 1.0)
        easein 6.0 xpos 0.20
    show kelisha worried focus:
        zoom 1.7
        pos (0.55, 1.0)
        easein 6.0 xpos 0.65
    with dissolve

    pause op.intro_dur
    return

label op.queen_huxtable:
    scene bg jersey city cityscape:
        zoom 1.1
        yalign 0.5
        xalign 1.0
        easein 8.0 xalign 0.0
    show queen smug 1 focus:
        flip
        zoom 1.5
        pos (0.55, 1.0)
        easein 8.0 xpos 0.45
    show op_text "\n\n{=op_actor}Ariana Osmanzai{/}\n{=op_as}as{/}\n{=op_char}Queen Elizabeth Newark{/}" at top
    with dissolve
    pause 8.0

    scene bg great hall inside:
        zoom 1.1
        yalign 0.5
        xalign 0.0
        easein 8.0 xalign 1.0
    show huxtable angry 2:
        flip
        zoom 1.5
        pos (0.1, 1.0)
        easein 12.0 xpos 0.3
    show queen angry 1 focus:
        zoom 1.5
        pos (0.65, 1.0)
        easein 12.0 xpos 0.85
    show op_text "\n\n{=op_actor}Ariana Osmanzai{/}\n{=op_as}as{/}\n{=op_char}Queen Elizabeth Newark{/}" at top
    with dissolve
    pause op.intro_dur

    call fx.log("10/17 intros (queen)")
    show queen -focus
    show huxtable focus
    show op_text "\n\n{=op_actor}Pablo Giraldo{/}\n{=op_as}as{/}\n{=op_char}General Robert Huxtable{/}" at top
    with dissolve
    pause 4.0

    scene bg campus
        #zoom 1.1
        #yalign 0.5
        #xalign 0.0
        #easein 10.0 xalign 1.0
    show princess happy:
        flip
        pos (-0.3, 1.0)
        linear 5.0 xpos 1.3
    show linda young happy 2:
        flip
        pos (-0.3, 1.0)
        pause 0.5
        linear 5.0 xpos 1.3
    show jojo young grin 1:
        pos (1.3, 1.0)
        pause 2.0
        linear 5.0 xpos -0.3
    show bart young happy:
        pos (1.3, 1.0)
        pause 2.5
        linear 5.0 xpos -0.3
    show huxtable young worried focus:
        pos (0.5, 1.0)
        noflip
        pause 3.0
        flip
        pause 2.5
        noflip
    show op_text "\n\n{=op_actor}Pablo Giraldo{/}\n{=op_as}as{/}\n{=op_char}General Robert Huxtable{/}" at top
    with dissolve
    pause op.intro_dur

    return

label op.destroyer:
    scene bg black hole
    show destroyer:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
        ysize 700
        fit "contain"
        fx.hover
    show op_text "\n\n{=op_actor}Nina Pankova{/}\n{=op_as}as{/}\n{=op_char}The Planet Destroyer{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.gunner:
    scene bg spaceship window
    show gunner focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Allison \"Illy\" Huang{/}\n{=op_as}as{/}\n{=op_char}Gunner Chief{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.wellington:
    scene bg training room
    show layer master at fx.flashback
    show wellington focus at bottom:
        zoom 2.0
    # `onlayer` so this text doesn't get flashbacked
    show op_text "\n\n{=op_actor}Delaney R. Page{/}\n{=op_as}as{/}\n{=op_char}Professor Wellington{/}" at top onlayer roxbury
    with dissolve
    pause op.intro_dur
    hide op_text onlayer roxbury
    return

label op.reporters:
    $ y = 0.48
    show bg breaking news as bg2:
        top
        zoom 0.0
        alpha 0.0

        ease 0.5 alpha 1.0 zoom 1.0
    pause 1.0
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
    with dissolve
    show reporter1 focus
    show op_text "{=op_actor}Felicity Audet{/}\n{=op_as}as{/}\n{=op_char}Crown Reporter{/}":
        anchor (0.5, 1.0)
        pos (0.25, 0.8)
    # with dissolve
    pause op.intro_dur
    call fx.log("15/17 intros")

    show reporter1
    show reporter2 focus
    show op_text "{=op_actor}Ashley Mendez{/}\n{=op_as}as{/}\n{=op_char}Crown Reporter{/}":
        anchor (0.5, 1.0)
        pos (0.50, 0.8)
    # with dissolve
    pause op.intro_dur
    call fx.log("16/17 intros")

    show reporter2
    show reporter3 focus
    show op_text "{=op_actor}Eiji Ren{/}\n{=op_as}as{/}\n{=op_char}Crown Reporter{/}":
        anchor (0.5, 1.0)
        pos (0.75, 0.8)
    # with dissolve
    pause op.intro_dur
    return

label op.choir:
    scene bg beige
    show logo choir at truecenter:
        zoom 0.8
    with dissolve
    pause op.intro_dur
    return