# scene 03 sprites: https://otaku-oratorio-2026-gallery.netlify.app/?t=takeshi&t=sanders&t=usagi 
label scene03: 
    scene bg training room with dissolve

    # they walk in from the right
    show sanders smug at offscreenright
    show takeshi neutral at offscreenright
    pause 0
    show sanders happy at right2
    show takeshi neutral at right
    with ease

    sanders @ smug "They’re sitting ducks."
    takeshi annoyed "Something’s not right. Performing field scan."

    # sanders steps forward, ready to engage...
    show sanders happy at center with ease
    # ...then turns around for a moment to talk to takeshi
    show sanders at center, flip
    sanders "Takeshi, watch my six, I’m going in."

    show sanders at center, noflip
    takeshi "We lost sight of their third... their support-"
    sanders eyeroll "The hell can a support do in this situation? I’m going in."

    # sanders steps all the way forward
    show takeshi worried 1 
    show sanders angry 1 at left with ease
    takeshi "NOT YET!"

    # sanders is hit! show this with background, screen shake, and tense music
    show bg red as bg2 behind takeshi, sanders:
        alpha 0.7
    show takeshi worried 2 
    show sanders shock focus at yshake(30, 4, 0.025) with vpunch
    pause 0.4
    hide bg2
    # no looping BGM unless the track is loopable! for most of these the track is much longer than the show, anyway
    play music "<from 1.6>bgm_003_hurry_ff7.opus" noloop
    sanders anxious "I’m hit!"
    takeshi worried 1 "Support unit B46 breaking formation and moving in to rescue Ace unit B100."

    # takeshi steps forward to (try to) rescue sanders
    show takeshi at center with ease
    sanders angry 1 "I didn’t need your help..."
    takeshi worried 1 "He’s right... I’m cooked"

    show takeshi panic 1 
    takeshis_console "SCAN COMPLETE; ENEMY SUPPORT MARKED; DEFENSIVE MISSILES INBOUND."
    takeshi "Dammit..."
    
    # > Usagi swoops in to save Takeshi, maneuvering to distract the
    # > missiles and guide them away. She then counter attacks the
    # > enemy team, taking them out herself one after the other.
    #
    # to show this, usagi's sprites fly around the screen. ff6 esper tech
    play music bgm_004_in_the_name_of_the_moon__sailor_moon noloop
    call scene03_usagi_swoops_in

    sanders prideful "That’s my duo!"
    takeshi happy 1 "Thanks Usagi..."

    # takeshi faces sanders to argue, while usagi's slowly getting pissed
    show usagi exasperated
    show takeshi neutral at noflip
    sanders angry 1 "What were you THINKING Takeshi??"
    takeshi angry 1 "I was saving YOU. If I HADN’T gone in, you would have been whining about me not doing my role as support!"
    sanders angry 2 "If you knew HOW to support, then you wouldn’t have gone IN..."

    # usagi steps forward to scold sanders
    show takeshi behind usagi
    show usagi exasperated 2 at right2 with ease
    show sanders shock
    usagi "SANDERS, WHAT THE HELL WAS THAT?" with vpunch
    usagi "IF YOU KNEW HOW TO ACE, THEN YOU WOULDN’T HAVE GONE IN WITH THE ENEMY SUPPORT MISSING..."
    usagi "THE DEFENSIVE MISSILES WERE IN THE BATTLE BRIEF."

    # > An aside, Usagi turns toward the audience, a complete 180 in
    # > personality.
    # music swaps, scroll takeshi/sanders off screen, spotlight's on usagi
    stop music fadeout 0.8
    pause 0.5
    show usagi happy 1 at center
    show sanders neutral at offscreenleft, flip
    show takeshi neutral at offscreenleft, flip
    with ease
    pause 0.3
    play music bgm_005_just_an_ordinary_girl__sailor_moon noloop #fadein 1.5
    show usagi hello
    usagi "My name is Usagi Kitadani and I’m a 4th year student at the Crown Military Academy."
    usagi "Yeah, the one on the Moon..."
    usagi "I love arts & crafts, small dogs, strawberries and parfaits."

    # introduce her friends: pan the camera towards them (scroll both usagi and her friends to the right)
    show usagi happy 1 at right
    show sanders happy at left
    with ease
    usagi "That’s Sanders, another 4th year. He’s an asshole. He’s good, but he’s an asshole."

    # scroll sanders offscreen, scroll takeshi onscreen
    show takeshi at offscreenleft
    pause 0
    show sanders at offscreenleft
    show takeshi happy 1 at left
    with ease
    usagi "And that’s Takeshi, a 3rd year but he’s graduating early, super sweet, super kind... super innocent."

    # usagi's back in the spotlight, at the center. friends leave the screen
    show usagi at center
    show takeshi at offscreenleft
    with ease
    usagi "I’d love to stick around and chat, but we’re late for class, and as you can see..."
    usagi weary "...we have a lot of work to do."

    # usagi walks off stage, making sure to face where she's walking
    show usagi weary at offscreenright, flip
    with ease
    show bg black with dissolve

    # > USAGI, SANDERS, AND TAKESHI TAKE OFF FOR CLASS, THE CHOIR
    # > EXEMPLIFIES SCHOOL LIFE, AND EVENTUALLY SETTLES INTO A
    # > CLASSROOM FORMATION.
    stop music fadeout 2
    return

label scene03_usagi_swoops_in:
    # pause after each animation for the length of that animation.
    # renpy's default (without any dialogue) is to show them for an instant and move on
    show sanders neutral at flip
    show takeshi neutral at flip
    show usagi shock focus at usagi_swoops_in_swoop1 behind takeshi, sanders
    with vpunch
    pause 0.8

    show sanders at noflip
    show takeshi at noflip
    show usagi happy 1 focus at usagi_swoops_in_swoop2
    with hpunch
    pause 0.8

    show sanders at flip
    show takeshi at flip
    show usagi shock focus at usagi_swoops_in_swoop3
    with vpunch
    pause 0.8

    show sanders happy at noflip
    show takeshi neutral at noflip
    show usagi happy 2 focus at usagi_swoops_in_landing
    # landing is 1.4 seconds total. sanders and takeshi both watch her land
    pause 0.4
    show sanders at flip
    pause 0.4
    show takeshi at flip
    pause 0.6  # landing is done here, 1.4 seconds

    # a small delay after the animation feels nice
    pause 0.3

    # reset animation transforms, in case we skipped the animation
    hide usagi 
    show usagi happy 1 at right
    return

# renpy coordinates: x=0 is left, y=0 is top
#
#  ___________________
# |        y=0        |
# | x=0           x=1 |
# |        y=1        |
#  ___________________

transform usagi_swoops_in_swoop1:
    parallel:
        noflip
        zoom 0.1 xalign 1.5 yalign 0.9
        linear 0.7 zoom 1 xalign -0.5 yalign 0.0 knot 1 knot 0.4 knot 0
    parallel:
        pause 0.1
        blink(n=2, dur=0.1)
        pause 0.2
    pause 0.1 

transform usagi_swoops_in_swoop2:
    parallel:
        flip
        zoom 1
        xalign -0.5 yalign 0.5
        easein 0.7 xalign 1.5 yalign 0.2 knot 0 knot 1.0
    parallel:
        pause 0.1
        blink(n=3, dur=0.1)
        pause 0.1
    parallel:
        pause 0.3
        yshake(n=10, dur=0.01, size=40)
    pause 0.1 

transform usagi_swoops_in_swoop3:
    parallel:
        noflip
        zoom 0.1 xalign 1.5 yalign 0.1 
        easeout 0.7 zoom 1 xalign -0.5 yalign 0.1   knot 5 knot 0.5 knot 0.9
    parallel:
        pause 0.1
        blink(n=1, dur=0.2)
        pause 0.2
    pause 0.1 

transform usagi_swoops_in_landing:
    parallel:
        # easein 1.4 right  # nope, this breaks for some reason
        yanchor 1.0
        easein 1.5 xalign 1.0 ypos ypos_textbox
    parallel:
        flip
        pause 0.9
        ease 0.3 noflip
        pause 0.2
