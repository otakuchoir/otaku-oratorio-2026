# https://otaku-oratorio-2026-gallery.netlify.app/?t=sanders&t=takeshi&t=usagi&t=kelisha
label scene11: 
    scene bg kelisha office transparent windows
    call scene11.space_background
    with dissolve

    call fx.play_music_if_changed_in_dev("bgm_010_ready_set_go__kirby_and_the_forgotten_land.opus")
    show kelisha neutral at left, flip
    show takeshi neutral at center:
        xoffset 500
        easein 1 xoffset 0
    show sanders neutral at right2:
        xoffset 500
        easein 1 xoffset 0
    show usagi neutral at right:
        xoffset 500
        easein 1 xoffset 0

    # > 11       INT. - SPACE SHUTTLE - KELISHA’S OFFICE THE ENVOY IS                     11
    # > TRAVELING TO EARTH.
    takeshi "You wanted to meet with us, Professor Kelisha?"
    kelisha "Ah yes, please, sit."
    show sanders anxious
    sanders "We’re not in trouble already, are we? I can’t afford to lose ANY points on this midterm..."
    show usagi annoyed
    usagi "She said she wanted to go over some intel. You literally never listen, do you? You don’t read battle briefs and you don’t listen."
    show sanders angry 1 at flip
    sanders "Hey!"
    show sanders angry 1 at noflip
    show takeshi at flip
    takeshi "She’s not wrong."

    stop music fadeout 2
    kelisha "If you’re ready, I’d like to begin."
    show takeshi at noflip
    show sanders neutral at noflip
    show usagi neutral at noflip

    # > THEY IMMEDIATELY SETTLE AND QUIET DOWN.
    kelisha "You three will have a front row seat at the negotiations."
    # > (MORE)
    ### page 18 ###
    # > EVERYONE SITS IN SILENCE...
    kelisha "You will see how The Crown and our leadership maintain order... Sanders, if the Kingdom of New Jersey refuses to return workers to the mines, what is your first path of escalation?"
    sanders "Non compliance means corrective action."
    usagi "I’d want to know why. Find the reason. Try to work toward a solution."
    kelisha "I know that is what you would do, that is why I was asking Sanders. But, Kitadani, what if the reason were one of religion? What if the New Jersians had some doctrine that forbade them from mining Ultima?"
    usagi "That’s highly unlikely... The New Jersians are a godless people."
    kelisha "It is a hypothetical question."
    call fx.play_music_in_dev("bgm_011_nightmares__full_metal_alchemist_brotherhood.opus")
    takeshi "The more likely reason is not religious, but environmental... No need for hypotheticals..."
    takeshi "Professor, the reason they protest is because they remember what happened 16 years ago."
    kelisha "You see... this is why I like the three of you. Straight to the point then..."
    kelisha "The negotiations will fail today, and our government, while we would like for it to think like you Williamson, or you Kitadani... is more like... Sanders."
    ### page 19 ###

    sanders @ angry 1 "... I feel like I should be offended?"
    # TODO zoom in on kelisha all dramatic-like
    show kelisha doom focus with dissolve
    kelisha "The negotiations will fail, and we will bear witness to the repercussions of defiance."
    kelisha "Today’s test is not one skill or merit, but of compliance and obedience."
    show kelisha neutral focus with dissolve
    show kelisha neutral
    kelisha "I wanted you to know this so that you would be prepared for... whatever may come."
    takeshi @ worried 1 "Should you be doing that?"
    kelisha "Sometimes, WE... fight from the inside."
    sanders "I’m lost."
    usagi "Come on guys, we have a lot of preparation to do... Professor Kelisha, thank you."
    sanders "Who is “we” in this situation?"
    show kelisha stinkeye
    show usagi angry sweat at fx.hopN(n=1, stretch=(0.1, 0.15)):
        xoffset 0
        linear 0.5 xoffset -150
        pause 0.3
        flip
        easeout 2 xoffset 1000
    show sanders neutral focus:
        transform_anchor True
        rotate 0
        pause 0.3
        "sanders shock focus"
        easeout 0.2 rotate 60
        pause 0.3
        pause 0.15
        easeout 2 xoffset 1000
    usagi "SANDERS!"
    show kelisha neutral
    # > USAGI DRAGS SANDERS OUT OF THE ROOM
    # > SHUTTLE LANDS IN NEW JERSEY.
    kelisha "Takeshi, whatever happens today, remember: the arc of the moral universe is long but it bends towards justice..."
    kelisha "Don’t be too loud and don’t move too fast. If you get caught, I will not be there to help you."
    stop music fadeout 2
    scene bg black with dissolve
    return

label scene11.space_background:
    # animate the space background outside the office window.
    # mirror the background horizontally + vertically, for a cleanish-looking loop point, since it doesn't loop well naturally
    $ bgvx = 23
    $ bgvy = 79
    # faster velocities, for testing the loop
    # $ bgvx = 3
    # $ bgvy = 7
    show bg space as bg2_00 behind bg:
        anchor (0, 0)
        pos (0, 0)
        parallel:
            xoffset 0
            linear bgvx xoffset -1280
            xoffset 1280
            linear bgvx xoffset 0
            repeat
        parallel:
            yoffset 0
            linear bgvy yoffset -1370
            yoffset 1370
            linear bgvy yoffset 0
            repeat
    show bg space as bg2_10 behind bg:
        anchor (0, 0)
        pos (0, 0)
        xzoom -1
        parallel:
            xoffset 1280
            linear bgvx xoffset 0
            linear bgvx xoffset -1280
            repeat
        parallel:
            yoffset 0
            linear bgvy yoffset -1370
            yoffset 1370
            linear bgvy yoffset 0
            repeat
    show bg space as bg2_01 behind bg:
        anchor (0, 0)
        pos (0, 0)
        yzoom -1
        parallel:
            xoffset 0
            linear bgvx xoffset -1280
            xoffset 1280
            linear bgvx xoffset 0
            repeat
        parallel:
            yoffset 1370
            linear bgvy yoffset 0
            linear bgvy yoffset -1370
            repeat
    show bg space as bg2_11 behind bg:
        anchor (0, 0)
        pos (0, 0)
        xzoom -1
        yzoom -1
        parallel:
            xoffset 1280
            linear bgvx xoffset 0
            linear bgvx xoffset -1280
            repeat
        parallel:
            yoffset 1370
            linear bgvy yoffset 0
            linear bgvy yoffset -1370
            repeat