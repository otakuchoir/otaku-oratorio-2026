# scene 13 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi&t=linda
image bg black = Solid('#000000')
label scene13: 
    scene black
    play music bgm_scene13_01
    "PLACEHOLDER IRL scene13 (pre-destruction)"
    play music bgm_scene13_02 noloop
    "PLACEHOLDER IRL scene13 (pre-destruction)"
    stop music
    "PLACEHOLDER Song: Lilium"
    
    # manga panels: the destruction of new jersey
    window hide
    window auto
    show bg scene13a with dissolve
    pause
    show bg scene13b
    pause
    show bg scene13c
    pause
    show bg scene13d
    pause
    show bg black with dissolve

    # post-destruction
    #show usagi neutral at topleft
    #show takeshi neutral at right2
    show linda neutral holo focus at center with dissolve
    linda "Usagi... there’s something I need to tell you. Call me back."
    hide linda with dissolve
    show takeshi neutral focus at center with dissolve
    takeshi "Everyone processed that moment in their own way."
    hide takeshi with dissolve
    show sanders neutral focus at center with dissolve
    sanders "Some of us saw nothing wrong."
    hide sanders with dissolve
    show takeshi neutral focus at center with dissolve
    takeshi "Some of us knew it was wrong."
    hide takeshi with dissolve
    show usagi neutral focus at center
    show takeshi neutral at left
    show sanders neutral at right
    with dissolve
    usagi "And all of us stayed silent."
    hide takeshi
    hide sanders
    with dissolve
    usagi "After that mid term, none of us really spoke much. Finals came and went, and then graduation..."
    hide usagi with dissolve
    return