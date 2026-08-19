# https://otaku-oratorio-2026-gallery.netlify.app/?t=bg&t=jojo&t=takeshi&t=sanders&t=usagi
label scene14: 
    scene bg campus
    # scene bg rooftop with dissolve
    # play music bgm_013_route_26_27__pokemon_anime
    show jojo neutral at left, flip
    show takeshi angry 1:
        noflip
        right
    show sanders neutral:
        noflip
        ytextbox
        xpos 0.55
    show usagi serious 1 at right2, noflip
    with dissolve
    # > 14       EXT. DAY; LUNAR ACADEMY ROSE GARDEN                                      14
    jojo "Today you take your first steps into the a society that now, more than ever, needs its guardians to stand watch over our democracy."
    jojo "A tradition that has spanned over a millennia since the great cataclysm. We swore to never forget the second fall of humanity."
    show takeshi at flip
    takeshi @ angry 2 "This is such BS..."
    show takeshi at noflip
    sanders @ deadpan "Careful, Williamson."
    usagi "He’s right."
    show jojo grin 1
    jojo "I’m glad you agree, Kitadani. Yes, this year is special. As we all know, Kohei Kitadani, truly a savior among men, who sacrificed himself to prevent the third fall of humanity..."
    show usagi shock
    show jojo fervent at flip, fx.hopN(n=2, y=75, stretch=(0.05, 0.10))
    jojo "...has a daughter in this year’s graduating class. She now enters our society, a guiding light, walking in her father’s footsteps. We look forward to what you will accomplish."
    #show bg black as bg2 behind bg
    stop music fadeout 5
    #show bg:
    #    alpha 1
    #    linear 5 alpha 0.0
    #show jojo:
    #    flip
    #    alpha 1
    #    linear 5 alpha 0.0
    #show takeshi:
    #    alpha 1
    #    linear 5 alpha 0.0
    #show sanders:
    #    alpha 1
    #    linear 5 alpha 0.0
    show usagi anxious focus:
        flip
        pause 0.3
        noflip
        pause 0.3
        repeat 2
        flip
        pause 0.5
        noflip
    usagi "No... that’s not what I..."
    show usagi cry 1 focus
    usagi "Stop it... stop it... I am not my..."
    # > (MORE)
    ### page 26 ###
    # > Applause from the crowd.
    # > The applause drowns her out.
    # > CUT TO
    scene bg black with dissolve
    return