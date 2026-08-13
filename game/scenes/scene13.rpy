# scene 13 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi&t=linda
label scene13: 
    scene bg great hall inside with dissolve:
        zoom 1.1
        xpos -0.1
    play music bgm_scene13_01
    show huxtable neutral at flip:
        ytextbox
        xpos 0.2
    show queen neutral:
        ytextbox
        xpos 0.7

    #scene bg great hall inside:
    #    zoom 1.1
    #    xpos 0.0
    show takeshi neutral:
        flip
        ytextbox
        xpos -0.55
    show usagi neutral:
        flip
        ytextbox
        xpos -0.4
    show sanders neutral:
        flip
        ytextbox
        xpos -0.25
    show kelisha neutral:
        flip
        ytextbox
        xpos -0.1
    # > 13       INT. KINGDOM OF NEW JERSEY GREAT HALL - DAY                              13
    huxtable "There is not much more to discuss. Our terms are more than clear. Return the miners to work and start Ultima production again."
    queen "And my question remains the same General Huxtable. Why would I do that?"
    huxtable "Because The Crown wills it. It shall be done-"
    queen "Oh my god... Robert please. Can you drop the act for just a-"
    huxtable "Her royal highness, will remind herself that she is speaking with-"
    queen "I’m speaking to you, Robert Huxtable. The loser that would keep talking in academy lectures when class was already over, keeping everyone overtime by at least 15 minutes every-single-day."
    queen "You know... It’s wild. You never really think about the fact that the DORKS you go to school with would retain their DORKINESS WELL into adulthood."
    ### page 23 ###
    huxtable "You always were less compliant with expectations, Queen Elizabeth."
    huxtable "Perhaps you should remind yourself that under our Crown Rule, such temperaments would not be permitted by anyone who were not heir to an Earth Dome Kingdom..."
    queen "Yeah I just didn’t think a colony born like you would be such a boot licker."
    huxtable ".... The Queen of New Jersey will mind her place...."
    queen "Let me make this easy for you Rob. You know what the funny thing about facts are?..."
    queen "They’re facts. And outside of the scientific process, they remain facts until proven otherwise."
    queen "And you know what hasn’t changed in 25 years, other than you being a little loser?"
    huxtable "This is your final-"
    queen "Remember that time you were talking so much that you accidently said the quiet part out loud?"
    queen "When you got old man Wellington to admit out loud in front of everyone what we all knew?"
    queen "That the domes aren’t real and there’s nothing wrong with Earth’s atmosphere AT ALL? That it’s all just population control and PROPAGANDA."
    huxtable "Guards."
    queen "Oh what? You’re going to detain me now? I know the playbook you idiots. And I’m always a step ahead."
    queen "You’ll attempt to get to me by threatening my people, and that’s why I’ve already evacuated the Kingdom of New Jersey."
    queen "Outside of the Domes, somewhere you’ll never find them because all of you aren’t smart enough to read a map."
    ### page 24 ###
    huxtable "What?"
    queen "So yeah. Do what you will, but even if I die by your pathetic hand. We’ll both know that I’m a badass, you’re a punk, and you talk too damn much."
    show queen neutral focus:
        transform_anchor True
        rotate 0
        easeout 0.2 rotate 15
        pause 0.3
        pause 0.15
        easeout 3 xoffset 1000
    show huxtable neutral at noflip:
        ytextbox
        xpos 0.2
    huxtable "...TAKE HER AWAY."
    show bg:
        zoom 1.1
        xpos -0.1
        linear 2 xpos 0.0
    show queen:
        linear 2 xpos 1.2
    show huxtable:
        linear 2 xpos 0.8
    show takeshi neutral:
        flip
        ytextbox
        linear 2 xpos 0.1
    show usagi neutral:
        flip
        ytextbox
        linear 2 xpos 0.25
    show sanders neutral:
        flip
        ytextbox
        linear 2 xpos 0.4
    show kelisha neutral:
        flip
        ytextbox
        linear 2 xpos 0.55
    huxtable "Well? What are you looking at? Negotiations are OVER."
    huxtable "The Queen of New Jersey defied The Crown, and her people incited a riot."
    takeshi "What?"
    kelisha "Shhhh."
    huxtable "Everyone is to evacuate the immediate region in NO LESS than 120 minutes. I am calling in a strike from the Ultima Cannon."
    huxtable "Yes... the people of New Jersey rioted... they destroyed their own dome, and the atmosphere consumed them all in a HELLFIRE."
    huxtable "YOU ARE ALL DISMISSED. I would suggest you make haste, unless you want to be caught in the blast."
    show huxtable:
        flip
        easeout 2 xoffset 800

    show kelisha at noflip
    kelisha "Repeat after me:"
    kelisha "Negotiations failed." 
    trio "Negotiations failed." 
    kelisha "The people of New Jersey rioted."
    trio "The people of New Jersey rioted."
    kelisha "They broke their dome and were consumed by earth’s violent atmosphere."
    trio "They broke their dome and were consumed by earth’s violent atmosphere."
    kelisha "This is why we build the domes."
    trio "This is why we build the domes."
    # > 
    # > SONG: Lillium    # > 
    # > Manga panel sequence of events: Ultima canon is fired,
    # > destroys new jersey.
    ### page 25 ###
    stop music
    # manga panels: the destruction of new jersey
    scene
    show bg white as bg2
    show bg scene13a:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    with dissolve
    "PLACEHOLDER Song: Lilium"
    window hide
    window auto
    pause
    show bg scene13b with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    pause
    show bg scene13c with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    pause
    show bg black as bg2
    show bg scene13d with dissolve:
        anchor (0.5, 0.5)
        pos (0.55, 0.45)
        zoom 1.1
        linear 10 xpos 0.45
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
    show bg black with dissolve
    return