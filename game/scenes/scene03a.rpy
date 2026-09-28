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
    call fx.log("Butter-fly is 5 minutes long. We have 17 actor intros = 16-ish seconds per intro")
    call fx.log("0/17 intros")
    call op.trio
    call fx.log("3/17 intros")
    # call op.usagi
    # call op.sanders
    # call op.takeshi
    call op.kagu
    call fx.log("4/17 intros")
    call op.kohei
    call fx.log("5/17 intros")
    call op.linda
    call fx.log("6/17 intros")
    call op.jojo
    call fx.log("7/17 intros")
    call op.bart
    call fx.log("8/17 intros")
    call op.kelisha
    call fx.log("9/17 intros")
    call op.queen
    call fx.log("10/17 intros")
    call op.huxtable
    call fx.log("11/17 intros")
    call op.destroyer
    call fx.log("11/17 intros")
    call op.gunner
    call fx.log("12/17 intros")
    call op.wellington
    call fx.log("13/17 intros")
    call op.reporters
    call fx.log("14/17 intros")
    call op.choir
    call fx.log("17/17 intros")
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
    call fx.log("1/17 intros")
    show usagi at op.trio_run_2
    pause 0.0

    # scene bg countryside
    show sanders angry 1 focus at bottom, op.trio_run_1
    show op_text "\n\n{=op_actor}Chomp Yamile Martine Cuevas{/}\n{=op_as}as{/}\n{=op_char}George Sanders{/}" at top
    with dissolve
    pause op.intro_dur
    call fx.log("2/17 intros")
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
    show child happy focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Jalisha Paz{/}\n{=op_as}as{/}\n{=op_char}The Child{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.kohei:
    scene bg spaceship window
    show kohei panic 2 focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Erin-Marquise Watson{/}\n{=op_as}as{/}\n{=op_char}Kohei Kitadani{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.linda:
    scene bg training room
    show linda happy 2 focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Rahanna Brown{/}\n{=op_as}as{/}\n{=op_char}Linda Kitadani{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.jojo:
    scene bg research lab inside
    show jojo fervent focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Abraham \"AJ\" Rogers Lopez{/}\n{=op_as}as{/}\n{=op_char}Professor Joseph \"Jojo\" Chen{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.bart:
    scene bg church interior
    show bart worried focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Connor \"Bear\" Barre{/}\n{=op_as}as{/}\n{=op_char}Bartholomew Barthandelus{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.kelisha:
    scene bg classroom
    show kelisha stinkeye focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Ashley Foster{/}\n{=op_as}as{/}\n{=op_char}Professor Kelisha Alvarez{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.queen:
    scene bg jersey city cityscape
    show queen smug 1 focus at bottom:
        zoom 1.5
    show op_text "\n\n{=op_actor}Ariana Osmanzai{/}\n{=op_as}as{/}\n{=op_char}Queen Elizabeth Newark{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.huxtable:
    scene bg great hall inside
    show huxtable angry 2 focus at bottom:
        zoom 2.0
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