label scene16: 
    scene black
    "PLACEHOLDER IRL scene16 first few lines only, until surface landing"

    # main dialogue
    # some of this generated dialogue will be cut: at the beginning for IRL, at the end for manga panels.
    # TODO: insert dialogue here
    call gen_scene16

    # manga panels: discovering the child
    window hide
    window auto
    show bg scene16a with dissolve
    pause
    show bg scene16b with dissolve
    pause
    show bg scene16c with dissolve
    pause
    show bg black behind act_end with dissolve
    show text "{color=#fff}{size=160}End of Act I{/size}{/color}" at truecenter as act_end with dissolve
    pause
    return