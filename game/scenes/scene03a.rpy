label scene03a: 
    window hide
    window auto

    call op.logo
    "TODO opening is work in progress. eventually everyone will have a short sprite animation, instead of an image. (or maybe we should keep the VN simple and focus on the IRL actor intros?) character order is very easy to change, except those with scenes together like the trio"
    window hide
    window auto
    call op.trio
    # call op.usagi
    # call op.sanders
    # call op.takeshi
    call op.kagu
    call op.bart
    call op.jojo
    call op.kelisha
    call op.linda
    call op.kohei
    call op.queen
    call op.huxtable
    call op.trio1
    call op.trio2
    call op.trio3
    call op.choir
    return

style op_text_s:
    # "Outlines only work when applied to an entire Text displayable. They do not work when applied to a hyperlink, text tag, or other method that applies to only a portion of the text."
    # https://www.renpy.org/doc/html/style_properties.html
    #
    # so we must apply this separately.
    size 20
    textalign 0.5
    outlines [(3, '#000', 0, 0)]
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
    show op_text "{=op_starring}Starring{/}\n{=op_actor}Sophia Chan{/}\n{=op_as}as{/}\n{=op_char}Usagi Kitadani{/}" at top
    with dissolve
    pause op.intro_dur
    show usagi at op.trio_run_2
    pause 0.0

    # scene bg countryside
    show sanders angry 1 focus at bottom, op.trio_run_1
    show op_text "\n\n{=op_actor}Chomp{/}\n{=op_as}as{/}\n{=op_char}George Sanders{/}" at top
    with dissolve
    pause op.intro_dur
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
    show op_text "\n\n{=op_actor}Jalisha Paz{/}\n{=op_as}as{/}\n{=op_char}The Child{/}\nwait, isn't this a spoiler?" at top
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

label op.jojo:
    scene bg research lab inside
    show jojo fervent focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}AJ{/}\n{=op_as}as{/}\n{=op_char}Professor Joseph \"Jojo\" Chen{/}" at top
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

label op.linda:
    scene bg training room
    show linda happy 2 focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}Rahanna{/}\n{=op_as}as{/}\n{=op_char}Linda Kitadani{/}" at top
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

label op.queen:
    scene bg jersey city cityscape
    show queen smug 1 focus at bottom:
        zoom 1.5
    show op_text "\n\n{=op_actor}Ariana Osmanzai{/}\n{=op_as}as{/}\n{=op_char}Queen Elizabeth Newark{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.huxtable:
    # TODO
    scene bg great hall inside
    show huxtable angry 2 focus at bottom:
        zoom 2.0
    show op_text "\n\n{=op_actor}(missing from credits doc!){/}\n{=op_as}as{/}\n{=op_char}General Robert Huxtable{/}" at top
    with dissolve
    pause op.intro_dur
    return

# TODO which one are we introducing?
label op.trio1:
    scene bg black
    show op_text "\n\n{=op_actor}Felicity Audet{/}\n{=op_as}as{/}\n{=op_char}several characters.\nwhich one are we introducing?{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.trio2:
    scene bg black
    show op_text "\n\n{=op_actor}Allison \"Illy\" Huang{/}\n{=op_as}as{/}\n{=op_char}several characters.\nwhich one are we introducing?{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.trio3:
    scene bg black
    show op_text "\n\n{=op_actor}Eiji Ren{/}\n{=op_as}as{/}\n{=op_char}several characters.\nwhich one are we introducing?{/}" at top
    with dissolve
    pause op.intro_dur
    return

label op.choir:
    scene bg beige
    show logo choir at truecenter:
        zoom 0.8
    with dissolve
    pause op.intro_dur
    return