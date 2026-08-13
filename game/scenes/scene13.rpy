# scene 13 sprites:
# https://otaku-oratorio-2026-gallery.netlify.app/?t=huxtable&t=queen
# https://otaku-oratorio-2026-gallery.netlify.app/?t=kelisha&t=takeshi&t=usagi&t=sanders
# https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi&t=linda
label scene13: 
    play music bgm_012_anticipation__full_metal_alchemist_brotherhood
    scene bg great hall inside:
        zoom 1.1
        xpos -0.1
    show huxtable neutral at flip:
        ytextbox
        xpos 0.2
    show queen neutral:
        ytextbox
        xpos 0.7
    with dissolve

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
    queen "And my question remains the same, General Huxtable. Why would I do that?"
    huxtable "Because The Crown wills it. It shall be done-"
    show queen serious 1
    queen "Oh my god... Robert please. Can you drop the act for just a-"
    show huxtable angry 1
    huxtable "Her royal highness, will remind herself that she is speaking with-"
    # the queen walks a circle around huxtable. adds some motion to the scene, and shows the queen's dominance here.
    call queen_circles_the_room
    queen "I’m speaking to you, Robert Huxtable. The loser that would keep talking in academy lectures when class was already over, keeping everyone overtime by at least 15 minutes every-single-day."
    queen "You know... It’s wild. You never really think about the fact that the DORKS you go to school with would retain their DORKINESS WELL into adulthood."
    ### page 23 ###
    show huxtable angry 1 focus as fronthux
    huxtable "You always were less compliant with expectations, Queen Elizabeth."
    huxtable "Perhaps you should remind yourself that under our Crown Rule, such temperaments would not be permitted by anyone who were not heir to an Earth Dome Kingdom..."
    show huxtable angry 1 as fronthux
    queen "Yeah I just didn’t think a colony born like you would be such a boot licker."
    show huxtable angry 1 focus as fronthux
    huxtable "...The Queen of New Jersey will mind her place..."
    show huxtable angry 1 as fronthux
    show queen smug 1
    queen "Let me make this easy for you Rob. You know what the funny thing about facts are?..."
    queen "They’re facts. And outside of the scientific process, they remain facts until proven otherwise."
    queen "And you know what hasn’t changed in 25 years, other than you being a little loser?"

    # reset the long circling animation
    hide huxtable
    hide queen
    hide fronthux
    hide bg
    show bg great hall inside behind takeshi, sanders, usagi, kelisha:
        zoom 1.1
        xpos -0.1
    show huxtable angry 2 at flip, fx.hopN(n=1, y=65, stretch=(0.05,0.1)):
        ytextbox
        xpos 0.2
    show queen smug 1:
        ytextbox
        xpos 0.7
    huxtable "This is your final-"
    queen "Remember that time you were talking so much that you accidently said the quiet part out loud?"
    queen "When you got old man Wellington to admit out loud in front of everyone what we all knew?"
    queen "That the domes aren’t real and there’s nothing wrong with Earth’s atmosphere AT ALL?"
    queen "That it’s all just population control and PROPAGANDA."
    show huxtable angry 2 at noflip, fx.hopN(n=2, y=100, stretch=(0.05,0.1))
    huxtable "Guards."
    show train_security as guard1 behind queen:
        matrixcolor BrightnessMatrix(-1)
        center
        flip
        xoffset -1500
        linear 2 xoffset 0
        noflip
    show train_security as guard2:
        matrixcolor BrightnessMatrix(-1)
        right
        flip
        xoffset -1500
        linear 2 xoffset 0
        noflip
    show huxtable at flip
    show queen smug 2
    queen "Oh what? You’re going to detain me now? I know the playbook, you idiots. And I’m always a step ahead."
    queen "You’ll attempt to get to me by threatening my people, and that’s why I’ve already evacuated the Kingdom of New Jersey."
    queen @ smug 3 "Outside of the Domes, somewhere you’ll never find them, because all of you aren’t smart enough to read a map."
    ### page 24 ###
    huxtable "What?" with vpunch
    queen "So yeah. Do what you will, but even if I die by your pathetic hand. We’ll both know that I’m a badass, you’re a punk, and you talk too damn much."
    show queen smug 1 focus:
        transform_anchor True
        rotate 0
        easeout 0.2 rotate 15
        pause 0.3
        pause 0.15
        easeout 3 xoffset 1000
    show huxtable at noflip:
        ytextbox
        xpos 0.2
    show train_security as guard1:
        flip
        xoffset 0
        pause 0.2 + 0.3# + 0.15
        easeout 3 xoffset 1000
    show train_security as guard2:
        flip
        xoffset 0
        pause 0.2 + 0.3# + 0.15
        easeout 3 xoffset 1000
    stop music fadeout 2
    huxtable @ angry 3 "...TAKE HER AWAY."
    show bg:
        zoom 1.1
        xpos -0.1
        linear 2 xpos 0.0
    show queen:
        linear 2 xpos 1.2
    show huxtable:
        noflip
        linear 2 xpos 0.8
    show takeshi worried 2:
        flip
        ytextbox
        linear 2 xpos 0.1
    show usagi cry 1:
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
    huxtable "The Queen of New Jersey defied The Crown..."
    huxtable "...and her people incited a riot."
    show usagi shock
    show takeshi shock
    takeshi "What?"
    kelisha "Shhhh."
    show usagi cry 1
    show takeshi worried 2
    huxtable @ angry 3 "Everyone is to evacuate the immediate region in NO LESS than 120 minutes. I am calling in a strike from the Ultima Cannon."
    huxtable @ angry 1 "Yes... the people of New Jersey rioted... they destroyed their own dome, and the atmosphere consumed them all in a HELLFIRE."
    huxtable "YOU ARE ALL DISMISSED. I would suggest you make haste, unless you want to be caught in the blast."
    show huxtable:
        flip
        easeout 2 xoffset 800

    show kelisha at noflip
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

    # > 
    # > SONG: Lillium    # > 
    # > Manga panel sequence of events: Ultima canon is fired,
    # > destroys new jersey.
    ### page 25 ###
    # manga panels: the destruction of new jersey
    scene bg white with dissolve
    show bg white as bg2 behind bg
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
        linear 8 xpos 0.45
        pause 2
        linear 8 pos (0.5, 0.5) zoom 1
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

label trio_say(words):
    show usagi cry 1 focus
    show takeshi worried 2 focus
    show sanders neutral focus
    trio "[words]"
    show usagi cry 1
    show takeshi worried 2
    show sanders neutral
    return

label queen_circles_the_room:
    show bg:
        xpos -0.1
        ease 10 xpos 0.0
        pause 4
        ease 10 xpos -0.1
    show huxtable:
        flip
        xoffset 0
        easeout 5 xoffset 200
        noflip
        easein 5 xoffset 400
        pause 4
        easeout 5 xoffset 200
        flip
        easein 5 xoffset 0
    # So, I want to show the queen walking a circle around huxtable.
    # That means her sprite must be behind huxtable's for half the animation, and in front of it for the other half.
    # But... renpy doesn't let us change sprite order during an animation! And I don't want to tie this long
    # animation to dialogue, because I don't know how fast the actors will speak. So, to make it work we're a
    # little tricky: create an extra huxtable sprite, in front of the queen's sprite but otherwise with identical
    # position/etc to the "real" huxtable. Then, halfway through the animation, hide the extra huxtable.
    show huxtable angry 1 as fronthux at left:
        ytextbox
        xpos 0.2
        flip
        xoffset 0
        easeout 5 xoffset 200
        noflip
        easein 5 xoffset 400
        pause 2
        alpha 0.0
    show queen behind fronthux:
        noflip
        xoffset 0
        yoffset 0
        easeout 5 xoffset -400 yoffset -30
        easein 5 xoffset -800 yoffset 0
        pause 2
        flip
        pause 2
        easeout 5 xoffset -400 yoffset 30
        easein 5 xoffset 0 yoffset 0
        noflip
    return