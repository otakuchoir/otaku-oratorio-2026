label scene13b: 
    # post-destruction
    #show usagi neutral at topleft
    #show takeshi neutral at right2
    show usagi cry 1 at left, flip
    show takeshi worried 2 at left2, flip
    show sanders neutral at center, flip
    show kelisha neutral at right
    with dissolve
    kelisha "Repeat after me:"
    kelisha "Negotiations failed." 
    call trio_say("Negotiations failed.")
    show takeshi at hvibrate(n=2)
    kelisha "The people of New Jersey rioted."
    show usagi at hvibrate(n=2)
    call trio_say("The people of New Jersey rioted.")
    kelisha "They broke their dome and were consumed by earth’s violent atmosphere."
    call trio_say("They broke their dome and were consumed by earth’s violent atmosphere.")
    show takeshi at hvibrate(n=2)
    kelisha "This is why we build the domes."
    call trio_say("This is why we build the domes.")
    show usagi at hvibrate(n=2)
    hide usagi
    hide takeshi
    hide sanders
    hide kelisha
    with dissolve

    show linda neutral holo focus at center with dissolve
    linda "Usagi... there’s something I need to tell you. Call me back."
    hide linda with dissolve
    call fx.log("nathan: \"Basically there's a downward arpeggio and then when the piano goes \"DUUUN\" at the end of the arpeggio, it goes to black screen, and then when piano lets go of pedal and becomes silent, Takeshi's line appears\"")
    pause
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
    show bg black with dissolve
    call fx.log("nathan: \"same idea, let the piano finish echoing before opening scene 14\"")
    pause
    return