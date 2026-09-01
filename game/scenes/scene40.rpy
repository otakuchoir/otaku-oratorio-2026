# define hover_bart = 3.7
# define hover_jojo = 1.9
# define hover_sanders = 2.3
# define hover_usagi = 1.7
# define hover_kelisha = 2.1
# define hover_kelisha = 2.1

# Nope, this is harder to compose than it looks...!
#image bg wide battlefield = Composite(
#    (screen_dim[0] * 2, screen_dim[1]),
#    (159, -180), Transform(renpy.get_registered_image("bg space"), xzoom=-1, matrixcolor=SaturationMatrix(0.8)), 
#    (screen_dim[0], 0), "bg space battlefield",
#)

label scene40:
    scene bg space battlefield:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.45, 0.45)

    # > 40       EXT. SPACE ABOVE THE MOON                                                40
    # https://otaku-oratorio-2026-gallery.netlify.app/?t=usagi+postgrad&t=sanders+postgrad&t=jojo&t=kelisha
    show jojo mech neutral at right, fx.hover(1.9), fx.ease_xoffset(dur=1.0, x0=1000)
    show sanders mech postgrad neutral at right2, fx.hover(2.3), fx.ease_xoffset(dur=1.0, x0=1000)
    show usagi mech postgrad neutral at center, fx.hover(1.7), fx.ease_xoffset(dur=1.0, x0=1000)
    call fx.play_music_in_dev("bgm_035_main_theme__star_fox_2026.opus")
    sanders "I’ve gotta say, I never thought I’d ever see you piloting-"
    usagi "I’m not doing this for The Crown, I’m doing it for everyone."
    jojo "I need to get control of the Ultima Cannon. The Alexander is acting as a blockade, though..."
    sanders "We’ll get you through, right Usagi?"
    jojo @ mech sad "If we don’t make it through... That’s it. Luckily, the moon hasn’t crossed the gravitational threshold yet, but we were cutting it close."

    show kelisha mech neutral at left, flip, fx.hover(2.1), fx.ease_xoffset(dur=0.5, x0=-500)
    kelisha "This is Crown Officer Kelisha Alvarez. Pilots, identify yourself."
    usagi "Professor Kelisha?"
    show kelisha mech happy
    kelisha "Ok, so it IS you... Joseph, Commander Sanders?"
    ### page 76 ###
    jojo "Copy copy"
    sanders "10-4... It’s us Officer Kelisha."
    kelisha mech stinkeye "Anyone care to tell me what’s going on here?"
    jojo mech sad "Barthandelus... he has gone mad. He’s using the Ultima Cannon to push the Moon into the Earth."
    kelisha mech worried "What!?"
    sanders "We’re on an escort mission, we’ve got to get Professor Chen here to the Ultima Cannon."
    kelisha mech serious "Then you’ll have my support from the Bahamut. Godspeed."
    show kelisha mech serious at left2, noflip, fx.hover(2.1), fx.ease_xpos(dur=1.0, x0=0.15, x1=0.85) behind usagi, sanders, jojo:
        noflip
        pause 0.8
        flip
    show bg space battlefield:
        pos (0.45, 0.45)
        linear 2.0 pos (0.55, 0.45)
    show jojo at right2, fx.hover(1.9), fx.ease_xpos(dur=1.0, x0=0.85, x1=0.66)
    show sanders at center, fx.hover(2.3), fx.ease_xpos(dur=1.0, x0=0.66, x1=0.50)
    show usagi at left2, fx.hover(1.7), fx.ease_xpos(dur=1.0, x0=0.50, x1=0.33)
    call fx.play_music_in_dev("bgm_036_weight_of_the_world_prelude.opus")
    pause 1.0
    jojo mech serious "There it is... The Alexander... and just beyond, the Ultima Cannon."

    $ dur = 2.0
    show jojo at fx.hover(1.9), fx.ease_xoffset(dur=dur, x1=-2000)
    show sanders at fx.hover(2.3), fx.ease_xoffset(dur=dur, x1=-2000)
    show usagi at fx.hover(1.7), fx.ease_xoffset(dur=dur, x1=-2000)
    # show kelisha at noflip, fx.hover(2.1), fx.ease_xpos(dur=dur, x0=0.15, x1=0.85)
    pause 2.0

    kelisha "Barthandelus pilots the Alexander as a high level defensive heal class. I’m debuffing his systems now."
    show bart mech neutral at left, flip, fx.hover(3.7), fx.ease_xoffset(dur=1.5, x0=-500)
    bart "So... you have come to challenge the will of god..."
    kelisha mech worried "Barthandelus! Stand down and let’s stop this insanity."
    ### page 77 ###
    bart mech angry 1 "The only insanity I see is a traitor to the Crown who not so secretly peruses with the Rebellion, now coming to stop the demise of the very system she swore to take down from the shadows. Have you lost your nerve?"
    kelisha "I can’t believe I’m telling YOU this, of all people, Bart, but burning it all down is not the way-"

    ###################################
    $ dur = 1.0
    show bg space battlefield:
        pos (0.55, 0.45)
        linear 1.0 pos (0.45, 0.45)
    show bart mech eyebrow raised at right, noflip, fx.hover(3.7), fx.ease_xpos(dur=dur, x0=0.15, x1=0.85)
    show sanders mech postgrad angry 1 at left2, noflip, fx.hover(2.3), fx.ease_xoffset(dur=dur, x0=-2000)
    show usagi mech postgrad serious 1 at left, noflip, fx.hover(1.7), fx.ease_xoffset(dur=dur, x0=-2000)
    show jojo mech serious at center, noflip, fx.hover(1.9), fx.ease_xoffset(dur=dur, x0=-2000)
    show kelisha mech serious at right, fx.hover(2.1), fx.ease_xoffset(dur=dur, x1=1000)
    sanders "We’re approaching the Alexander now. We’ll rush past it and put Jojo in position. Follow me everyone-"
    show bart mech grin 1:
        # TODO I want this to transition from wherever the hover puts him, but it seems to teleport abruptly instead...?
        linear 0.25 yoffset 0
    pause 0.25
    show bart mech as bartglow at right, noflip behind bart:
        blur 12
        matrixcolor ColorizeMatrix(color_bart, color_bart)
        alpha 0.0
        linear 0.5 alpha 1.0
    pause 0.5
    show sanders mech postgrad anxious at left2, noflip, fx.hover(4 * 2.3):
        matrixcolor TintMatrix('#fff')
        linear 0.5 matrixcolor TintMatrix(color_bart)
    show usagi mech postgrad anxious at left, noflip, fx.hover(4 * 1.7):
        matrixcolor TintMatrix('#fff')
        linear 0.5 matrixcolor TintMatrix(color_bart)
    show jojo mech sad at center, noflip, fx.hover(4 * 1.9):
        matrixcolor TintMatrix('#fff')
        linear 0.5 matrixcolor TintMatrix(color_bart)
    usagi "Guys... I’m losing power... We’re slowing down?"
    jojo "The Alexander has a magnetic tractor beam."
    bart "That’s right. I don’t need you getting any closer. Just sit still while-"
    show bart mech shock
    computer "INCOMING MISSILES"
    # > Missiles bombard the Alexander.
    show bg linda hits as lindahits behind linda, sanders, usagi, jojo:
        alpha 0.0
        linear 0.05 alpha 0.4
        linear 0.05 alpha 0.0
        pause 0.05
        repeat 5
    show bart:
        yshake(5, 6, 0.02)
        fx.hover(3.7)
    show bart mech as bartglow:
        parallel:
            alpha 1.0
            linear 0.5 alpha 0.0
        parallel:
            yshake(5, 10, 0.02)
    show sanders mech postgrad neutral at left2, noflip, fx.hover(2.3):
        matrixcolor TintMatrix(color_bart)
        linear 0.5 matrixcolor TintMatrix('#fff')
    show usagi at left, noflip, fx.hover(1.7):
        matrixcolor TintMatrix(color_bart)
        linear 0.5 matrixcolor TintMatrix('#fff')
    show jojo mech neutral at center, noflip, fx.hover(1.9):
        matrixcolor TintMatrix(color_bart)
        linear 0.5 matrixcolor TintMatrix('#fff')
    bart "What!?"
    show sanders at fx.hover(2.3), fx.ease_xoffset(dur=1.0, x1=-1000):
        ease 1.0 ypos 0.5
    show usagi at fx.hover(1.7), fx.ease_xoffset(dur=1.0, x1=-1000):
        ease 1.0 ypos 0.8
    show jojo at fx.hover(1.9), fx.ease_xoffset(dur=1.0, x1=-1000):
        ease 1.0 ypos 1.0
    jojo "We’re free. Good job Kelisha."

    ###################################
    show bg space battlefield:
        pos (0.45, 0.45)
        linear 1.0 pos (0.55, 0.45)
    hide kelisha
    show kelisha mech worried at right, noflip, fx.hover(2.1), fx.ease_xoffset(dur=1.0, x0=1000)
    show bart mech neutral at left, noflip, fx.hover(3.7), fx.ease_xpos(dur=1.0, x0=0.85, x1=0.15)
    kelisha "That wasn’t me."
    hide usagi
    hide sanders
    hide jojo

    show bart mech angry 1 at flip, fx.hover(3.7)
    show linda mech serious at center, fx.hover(1.3), fx.ease_xoffset(dur=1.0, x0=1000), fx.ease_yoffset(dur=1.0, y0=500)
    show kelisha mech happy
    linda "Ace Unit Shiva here, Carbunkle, Sanders, Usagi, you should be good to go again."
    usagi postgrad neutral "Mom??"
    ### page 78 ###
    show linda mech smile
    linda "I came as soon as I saw the news. No time for shock and surprise. You already knew I was the best Ace there was."
    linda @ mech happy "Now go, little rabbit! I’ll keep The Alexander busy."
    usagi postgrad neutral "Thanks mom!"
    show bart mech angry 1 at noflip, fx.hover(3.7)
    pause 0.3

    ###################################
    # > Usagi, Professor Jojo and Sanders rush to the Ultima Cannon
    show bg space battlefield: 
        pos (0.55, 0.45)
        linear 0.5 pos (0.45, 0.45)
    show bart at fx.hover(3.7), fx.ease_xoffset(dur=0.5, x1=1500)
    show kelisha at fx.hover(2.1), fx.ease_xoffset(dur=0.5, x1=1500)
    show linda at fx.hover(1.3), fx.ease_xoffset(dur=0.5, x1=1500)
    show bg black as bg2:
        alpha 0.0
        linear 0.5 alpha 1.0
    pause 0.5
    scene bg space battlefield:
        alpha 0.0
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.45, 0.45)
    call scene11.space_background(bgvx=7, bgvy=79, flip=True)
    show usagi mech postgrad happy 1 at center, fx.hover(1.7), fx.ease_xoffset(dur=0.5, x0=-1500)
    show sanders mech postgrad happy at left2, fx.hover(2.3), fx.ease_xoffset(dur=0.5, x0=-1500)
    show jojo mech sad at left, fx.hover(1.9), fx.ease_xoffset(dur=0.5, x0=-1500)
    with dissolve
    jojo "Thanks Linda. I won’t let you down."
    hide bg2
    usagi @ mech postgrad happy 3 "Kagu, buckle up!"
    sanders mech postgrad teasing "Little Rabbit?"
    usagi mech postgrad annoyed "Careful... you’re the one who took her cousin away."
    sanders mech postgrad deadpan ".... Yeah about that."
    usagi mech postgrad angry "What do you have to say for yourself and why shouldn’t I blow you up along with Barthandelus."
    show usagi mech postgrad shock
    sanders "We... never found her, the Queen of New Jersey. It was another cover up. The place that we blew up... just innocent people... The Crown made up a story and we were told to keep quiet...."
    show bg black as bg2 behind bg:
        alpha 0.0
        linear 0.5 alpha 1.0
    pause 0.5
    call scene11.space_background_hide
    show bg space battlefield:
        alpha 0.0
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.45, 0.45)
        parallel:
            linear 1.5 alpha 1.0
        parallel:
            easein 1.5 pos (0.55, 0.45)
    show usagi mech postgrad neutral
    show sanders mech postgrad neutral
    jojo mech grin 1 "We’re closing in on the Ultima Cannon now."
    hide bg2

    ###################################
    show bart mech stern at fx.hover(3.7), right, fx.ease_xoffset(dur=1.0, x0=500), fx.ease_ypos(dur=1.0, y0=1.0, y1=ypos_textbox)
    show bg bart hits as barthits behind bart:
        alpha 0.0
        pause 0.5
        linear 1.5 alpha 0.4
    show usagi mech postgrad shock behind barthits
    show sanders mech postgrad shock behind barthits
    show jojo mech serious behind barthits
    bart @ mech angry 2 "Insolent fools! Alexander primary burst weapon load out."

    # > Linda slices the primary weapon barrel, disabling The
    # > Alexander’s main weapon.
    $ dur = 0.8
    show linda mech serious at center, flip:
        rotate -15
        fx.ease_pos(dur=dur, xy0=(0.5, 1.5), xy1=(1.0, 0.0))
        rotate 15
        fx.ease_pos(dur=dur, xy0=(0.5, 0.0), xy1=(1.0, 1.5))
    show bg bart hits as barthits behind bart:
        pause 0.4
        linear 0.1 alpha 0.0
    pause 0.4
    show bg linda hits as lindahits behind linda, sanders, usagi, jojo:
        alpha 0.0
        pause 0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.0
        pause 0.1
        pause 0.5
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.0
        pause 0.1
    show bart mech angry 1 at fx.hover(dur=3.7) behind lindahits
    pause 0.1
    show bart mech shock
    show sanders at fx.hover(2.3), fx.ease_xoffset(dur=1.0, x1=-1200):
        ease 1.5 ypos 0.5
    show usagi at fx.hover(1.7), fx.ease_xoffset(dur=1.0, x1=-1200):
        ease 1.5 ypos 0.8
    show jojo at fx.hover(1.9), fx.ease_xoffset(dur=1.0, x1=-1200):
        ease 1.5 ypos 1.0
    linda "I don’t think so."

    # > Barthandelus activates the tractor
    # > beam again, catching Linda.
    hide lindahits
    show bart mech angry 2:
        flip
        linear 0.2 yoffset 0
        pause 0.5
        noflip
    show bart mech as bartglow at right, behind bart:
        flip
        blur 12
        matrixcolor ColorizeMatrix(color_bart, color_bart)
        alpha 0.0
        linear 0.2 alpha 1.0
        pause 0.5
        noflip
    show linda mech scared:
        noflip
        xoffset 0
        yoffset 0
        matrixcolor TintMatrix(color_bart)
        pos (1.5, 1.0)
        ease 1.0 pos (0.67, ypos_textbox)
        pause 0.5
        yshake(5, None, 0.025)
    pause 1.0
    show bart mech grin 2

    bart "And so your story ends here."
    ### page 79 ###
    show bart mech neutral
    computer "INCOMING BEAM ATTACK"
    show bart mech angry 1
    bart "What?"
    show bart mech shock
    show queen mech serious 1 at left, flip, fx.hover(3.1), fx.ease_xoffset(dur=1.0, x0=-1000), fx.ease_yoffset(dur=1.0, y0=-500) behind linda
    show bg queen hits as queenhits behind linda, queen:
        alpha 0.0
        linear 0.08 alpha 0.6
        linear 0.08 alpha 0.0
        pause 0.1
        repeat 3
    show linda mech worried:
        parallel:
            fx.hover(1.3)
        parallel:
            matrixcolor TintMatrix(color_bart)
            linear 0.5 matrixcolor TintMatrix('#fff')
        parallel:
            rotate 15
            ease 0.5 rotate 0
    show bart mech as bartglow:
        alpha 1.0
        linear 0.5 alpha 0.0
    show bart at yshake(5, 10, 0.02) behind queenhits

    queen "Diabolos Dark Laser Charge, Attack!"
    show linda mech happy 2
    linda "LIZZY!"
    show linda:
        parallel:
            fx.ease_xoffset(dur=1.0, x1=-500)
        parallel:
            fx.ease_yoffset(dur=0.3, y1=200)
            fx.ease_yoffset(dur=0.7, y0=200, y1=-1200)
    show queen mech smug 1
    queen "The one and only ;) Back away from his tractor beam. Kelisha, break his defenses!"
    show kelisha mech neutral at center, flip, fx.hover(2.1):
        parallel:
            fx.ease_xoffset(dur=1.3, x0=-500)
        parallel:
            fx.ease_yoffset(dur=1.0, y0=1200, y1=-200)
            fx.ease_yoffset(dur=0.3, y0=-200)
    hide queenhits
    show bg kelisha hits as kelishahits behind linda, queen, kelisha:
        alpha 0.0
        linear 1.0 alpha 0.9
        linear 1.0 alpha 0.0
    show bart:
        parallel:
            matrixcolor TintMatrix('#fff')
            linear 0.5 matrixcolor TintMatrix(color_kelisha)
        parallel:
            yshake(5, 6, 0.02)

    kelisha mech happy "Already on it, Mega Flare Pierce Rifle, Activate!"
    # > The Bahamut shoots a blast that break’s The Alexander’s
    # > shields.
    show bart mech angry 2
    bart "No!"

    show bg space battlefield:
        pos (0.55, 0.45)
        ease 2.0 pos (0.50, 0.45)
    show queen at flip, fx.hover(3.1), fx.ease_xoffset(dur=2.0, x1=-1000)
    show kelisha at flip, fx.hover(2.1), fx.ease_xoffset(dur=2.0, x1=-1000)
    $ dur = 0.6
    show bart mech anxious:
        parallel:
            fx.ease_xpos(dur=2.0, x0=0.85, x1=0.5)
        parallel:
            pause (dur-0.2)
            yshake(5, 4, 0.01)
            pause 0.04
            repeat 7
        pause 0.3
        parallel:
            fx.ease_pos(dur=4.0, xy0=(0.5, ypos_textbox), xy1=(0.8, -0.5))
        parallel:
            rotate 0.0
            linear 4.0 rotate 4 * -360
    show bg linda hits as lindahits behind linda, queen, kelisha:
        alpha 0.0
        pause (dur-0.3)
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.0
        pause 0.1
        repeat 8
    hide linda
    show linda mech doom:
        flip
        rotate -15
        fx.ease_pos(dur=dur, xy0=(0.5, 1.5), xy1=(1.0, 0.0))
        rotate 15
        fx.ease_pos(dur=dur, xy0=(0.5, 0.0), xy1=(1.0, 1.5))
        noflip
        rotate 15
        fx.ease_pos(dur=dur, xy0=(0.85, 1.5), xy1=(0.35, 0.0))
        rotate -15
        fx.ease_pos(dur=dur, xy0=(0.85, 0.0), xy1=(0.35, 1.5))
        flip
        rotate -15
        fx.ease_pos(dur=dur, xy0=(0.25, 1.5), xy1=(0.75, 0.0))
        rotate 15
        fx.ease_pos(dur=dur, xy0=(0.25, 0.0), xy1=(0.75, 1.5))
        noflip
        rotate 15
        fx.ease_pos(dur=dur, xy0=(0.75, 1.5), xy1=(0.25, 0.0))
        rotate -15
        fx.ease_pos(dur=dur, xy0=(0.75, 0.0), xy1=(0.25, 1.5))
    linda "I’m sorry, Bart... OVERDRIVE MARIPOOOOOSA!"
    # > Linda’s attack severely damages The Alexander

    scene bg space battlefield:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.50, 0.45)
        ease 1.0 pos (0.55, 0.45)
    show sanders mech postgrad happy at left2, noflip, fx.hover(2.3), fx.ease_xoffset(dur=1.0, x0=-1000)
    show usagi mech postgrad happy 1 at left, noflip, fx.hover(1.7), fx.ease_xoffset(dur=1.0, x0=-1000)
    show jojo mech grin 2 at center, noflip, fx.hover(1.9), fx.ease_xoffset(dur=1.0, x0=-1000)
    jojo "We’re in range, let’s park it right here."
    show sanders mech postgrad happy at left2, noflip, fx.hover(2.3), fx.ease_xoffset(dur=1.0, x0=-1000)
    show usagi mech postgrad happy 1 at left, noflip, fx.hover(1.7), fx.ease_xoffset(dur=1.0, x0=-1000)
    show jojo mech grin 2 at center, noflip, fx.hover(1.9), fx.ease_xoffset(dur=1.0, x0=-1000)
    jojo mech serious 2 "I’m taking control of the system now...."

    show bg space battlefield:
        pos (0.55, 0.45)
        ease 1.0 pos (0.50, 0.55)
    show bart mech angry 2 at center:
        parallel:
            fx.ease_xyoffset(dur=1.0, xy0=(500, 1500))
        parallel:
            rotate -270.0
            easein 1.5 rotate 45.0
            easein 1.0 rotate -60.0
        parallel:
            pause 2.0
            ease 1.0 fx.stretch(0.9, 1.15)
    show sanders at fx.ease_xyoffset(dur=1.0, xy1=(-500, 1500))
    show usagi at fx.ease_xyoffset(dur=1.0, xy1=(-500, 1500))
    show jojo at fx.ease_xyoffset(dur=1.0, xy1=(-500, 1500))

    bart "I may be defeated here... but I WILL NOT LOSE! JUDGEMENT LANCE!"

    # > The Alexander launches a golden lance toward Professor Jojo.
    call fx.play_music_in_dev("bgm_037_escape__xenosaga_episode_1.opus")
    show bg space battlefield:
        pos (0.50, 0.55)
        ease 1.0 pos (0.55, 0.45)
    show bg bart hits as barthits behind bart, jojo:
        alpha 0.0
        pause 0.5
        linear 0.1 alpha 0.8
        linear 2.0 alpha 0.3
    show bart mech angry 3:
        ease 0.2 fx.stretch(1.15, 0.9)
        pause 0.3
        ease 0.2 fx.stretch(1.0, 1.0)
    show sanders mech postgrad panic at fx.ease_xyoffset(dur=1.0, xy0=(-500, 1500), xy1=(500, -1500))
    show usagi mech postgrad shock at fx.ease_xyoffset(dur=1.0, xy0=(-500, 1500), xy1=(500, -1500))
    show jojo mech crying at fx.ease_xyoffset(dur=0.5, xy0=(-500, 1500))
    kelisha mech worried "JOSEPH!"
    # > The lance makes impact with Jojo, causing a huge explosion.
    # > He’s gone in an instant.
    ### page 80 ###
    hide jojo with dissolve
    show bart mech anxious
    bart "My... friend.... AHHHHHH!"
    show bg bart hits as barthits:
        linear 0.1 alpha 1.0
        pause 1.5
        easein 3.0 alpha 0.0
    hide bart with dissolve
    # > Barthandelus and the Alexander go up in a ball of flame and
    # > explosion.
    hide linda
    linda shock "Joseph.... Bart...."

    # hide barthits
    show bg space battlefield:
        pos (0.55, 0.45)
        ease 1.0 pos (0.50, 0.50)
    show sanders at flip, fx.hover(2.3), fx.ease_xyoffset(dur=1.0, xy0=(500, -1500))
    show usagi mech postgrad cry 1 at flip, fx.hover(1.7), fx.ease_xyoffset(dur=1.0, xy0=(500, -1500))
    pause 0.5
    sanders "Shit. What do we do now??"
    show sanders mech postgrad shock
    show usagi mech postgrad happy 1
    show takeshi mech postgrad happy 1 at right2, fx.hover(2.5), fx.ease_xyoffset(dur=2.0, xy0=(1500, -500))
    takeshi "Support unit B-100 reporting... Sounds like you need someone who knows how to hack."
    usagi @ mech postgrad happy 3 "Takeshi!"
    show sanders mech postgrad neutral
    takeshi "Sorry I couldn’t be here sooner guys. Sanders..."
    show sanders mech postgrad happy
    sanders "... Well can you stop this thing or not?"
    # > Takeshi begins hacking the Ultima Cannon.
    show takeshi mech postgrad happy 2 at left, fx.hover(2.5), fx.ease_xpos(dur=1.0, x0=0.66, x1=0.15)
    show usagi at right2, fx.hover(1.7), fx.ease_xpos(dur=1.0, x0=0.15, x1=0.66):
        noflip
        pause 0.5
        flip
    show sanders at center, fx.hover(2.3), fx.ease_xpos(dur=1.0, x0=0.33, x1=0.50):
        noflip
        pause 0.5
        flip
    takeshi "Can I stop this thing, ha!"
    pause 1.0
    show takeshi mech postgrad shock
    takeshi "Oh... shit."
    show takeshi mech postgrad worried 2
    show usagi mech postgrad anxious
    show sanders mech postgrad anxious
    sanders "What!? What is it?"
    takeshi "We’ve got a few minutes until the moon crosses Earth’s gravitational threshold."
    sanders "Yeah, and? You can stop the Ultima Cannon right?"
    takeshi "It's been sabotaged. If we disable the tractor beam function... The cannon self destructs. We’ll lose the Ultima Cannon."
    ### page 81 ###
    show sanders mech postgrad neutral
    show usagi mech postgrad neutral
    sanders "Isn’t that what you want? An end to the mining? The Crown’s weapon?"
    takeshi "The self destruct would be instant..."
    show sanders mech postgrad anxious
    sanders "...."
    show usagi mech postgrad anxious
    usagi "...."
    show sanders mech postgrad angry 1
    sanders "Well we only have a few minutes. We need to make a decision now. I’ll do it."
    show usagi mech postgrad worried
    show takeshi mech postgrad worried 1 at flip, fx.hover(2.5)
    show sanders mech postgrad angry 2
    sanders "Save me the shock ok? I know you both hate me."
    show sanders mech postgrad angry 1
    sanders "The things I’ve done in the name of the Crown... I realized too late what I had become. Let me redeem myself with this-"

    show takeshi mech postgrad neutral at flip, fx.hover(2.5)
    show usagi mech postgrad neutral at noflip, fx.hover(1.7)
    show sanders mech postgrad neutral at noflip, fx.hover(2.3)
    show child neutral at right, fx.hover(1.3), fx.ease_xyoffset(dur=1.0, xy0=(500, 1000))
    kagu "I can do it. It won’t hurt. I can’t be destroyed."
    usagi "Are you serious Kagu?"
    show child sad
    kagu "Yeah. It’s just..."
    usagi "What?"
    kagu "Well... this will be goodbye."
    kagu "The blast... That will be super heated Ultima Ore. It will be enough energy to complete my evolution instantly..."
    show child neutral
    kagu "Look we don’t have time, get out of here. Sorry we didn’t have time for introductions you two."
    sanders "Oh I know who you are."
    takeshi "Me too... part of the intel. It was nice to meet you Sabik."
    kagu "Actually, my name is Kagu. Short for Kaguya, but we don’t have time. Go, now! I’ll see you in a bit."
    stop music

    show sanders at flip, fx.hover(2.3), fx.ease_xyoffset(dur=1.0, xy1=(-1500, -500))
    show usagi at flip, fx.hover(1.7), fx.ease_xyoffset(dur=1.0, xy1=(-1500, -500))
    show takeshi at flip, fx.hover(2.5), fx.ease_xyoffset(dur=1.0, xy1=(-1500, -500))
    show child serious at fx.hover(1.3), fx.ease_xpos(dur=1.5, x0=0.85, x1=0.50)
    pause 1.0
    scene bg black with dissolve

    window hide
    window auto
    # > Usagi, Takeshi and Sanders rush away back to Linda, Kelisha
    # > and Elizabeth. Kagu floats near the Ultima Cannon and then
    # > a huge explosion.
    show bg scene40 explosion 1 at screen_size
    with Dissolve(0.5)
    pause 1.0
    show bg scene40 explosion 2 at screen_size
    with Dissolve(1.0)
    pause 1.0
    show bg scene40 explosion 3 at screen_size
    with Dissolve(1.0)
    pause 1.0
    show bg scene40 explosion 4 at screen_size
    with Dissolve(1.0)
    pause 1.0
    show bg black
    with Dissolve(4.0)

    # > When the picture comes back into view it is
    # > the adult planet destoryer, absorbing the last bits of the
    # > explosion. And staring... Then:
    show bg scene40 judgement 1:
        xsize 1440
        fit "contain"
    with fade
    show bg scene40 judgement 2
    with Dissolve(1.0)
    show bg scene40 judgement 3
    with Dissolve(1.0)
    destroyer "BEAR WITNESS NOW, FOR I AM THE MESSENGER OF THE HEAVENS, THE BEGINNING AND THE END, THE FIRST AND THE LAST. I AM THE GREAT RESETTER; SABIK." with vpunch
    usagi postgrad shock "Oh no... Kagu has fully evolved."
    window hide
    window auto
    show bg scene40 judgement 4
    with Dissolve(1.0)
    destroyer "... YOUR ENTIRE HUMAN RACE... OWES GREAT THANKS TO THE ONE YOU CALL USAGI KITADANI, FOR SHE HAS SHOWN US THE HUMAN POWER OF LOVE AND COMPASSION." with vpunch
    destroyer "THEREFORE, I -WILL- GIVE YOUR SOCIETY A SECOND CHANCE. PRAY THAT WE NEVER MEET AGAIN." with vpunch
    # > In an instant, Sabik is encased in a crystal and disappears
    # > in a flash.
    window hide
    window auto
    pause 0.7
    show bg scene40 judgement 5 with Dissolve(0.3)
    show bg scene40 judgement 6 with Dissolve(0.3)
    show bg scene40 judgement 7 with Dissolve(0.3)
    show bg scene40 judgement 8 with Dissolve(0.5)
    show bg scene40 judgement 9 with Dissolve(3.0)
    pause 1.0
    return