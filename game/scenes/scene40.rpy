
label scene40:
    scene bg space battlefield
    "TODO the final battle, work in progress"

    # > 40       EXT. SPACE ABOVE THE MOON                                                40
    show jojo mech neutral at right, fx.hover(1.9)
    show sanders mech postgrad neutral at right2, fx.hover(2.3)
    show usagi mech postgrad neutral at center, fx.hover(1.7)
    sanders "I’ve gotta say, I never thought I’d ever see you piloting-"
    usagi "I’m not doing this for The Crown, I’m doing it for everyone."
    jojo "I need to get control of the Ultima Cannon. The Alexander is acting as a blockade, though..."
    sanders "We’ll get you through, right Usagi?"
    jojo "If we don’t make it through... That’s it. Luckily, the moon hasn’t crossed the gravitational threshold yet, but we were cutting it close."

    show kelisha mech neutral at left, flip, fx.hover(2.1), fx.ease_xoffset(dur=0.5, x0=-500)
    kelisha "This is Crown Officer Kelisha Alvarez. Pilots, identify yourself."
    usagi "Professor Kelisha?"
    kelisha "Ok, so it IS you... Joseph, Commander Sanders?"
    ### page 76 ###
    jojo "Copy copy"
    sanders "10-4... It’s us Officer Kelisha."
    kelisha "Anyone care to tell me what’s going on here?"
    jojo "Barthandelus... he has gone mad. He’s using the Ultima Cannon to push the Moon into the Earth."
    kelisha "What!?"
    sanders "We’re on an escort mission, we’ve got to get Professor Chen here to the Ultima Cannon."
    kelisha "Then you’ll have my support from the Bahamut. Godspeed."
    jojo "There it is... The Alexander... and just beyond, the Ultima Cannon."

    # camera shifts to kelisha soloing as jojo/sanders/usagi run for the goal
    # scene bg space battlefield
    $ dur = 2.0
    show jojo at fx.hover(1.9), fx.ease_xoffset(dur=dur, x1=-2000)
    show sanders at fx.hover(2.3), fx.ease_xoffset(dur=dur, x1=-2000)
    show usagi at fx.hover(1.7), fx.ease_xoffset(dur=dur, x1=-2000)
    show kelisha at noflip, fx.hover(2.1), fx.ease_xpos(dur=dur, x0=0.15, x1=0.85)
    pause 2.0

    kelisha "Barthandelus pilots the Alexander as a high level defensive heal class. I’m debuffing his systems now."
    show bart mech neutral at left, flip, fx.hover(3.7), fx.ease_xoffset(dur=1.5, x0=-500)
    bart "So... you have come to challenge the will of god..."
    kelisha "Barthandelus! Stand down and let’s stop this insanity."
    ### page 77 ###
    bart "The only insanity I see is a traitor to the Crown who not so secretly peruses with the Rebellion, now coming to stop the demise of the very system she swore to take down from the shadows. Have you lost your nerve?"
    kelisha "I can’t believe I’m telling YOU this, of all people, Bart, but burning it all down is not the way-"

    ###################################
    $ dur = 1.0
    show bart mech neutral at right, noflip, fx.hover(3.7), fx.ease_xpos(dur=dur, x0=0.15, x1=0.85)
    show sanders mech postgrad neutral at left2, noflip, fx.hover(2.3), fx.ease_xoffset(dur=dur, x0=-2000)
    show usagi mech postgrad neutral at left, noflip, fx.hover(1.7), fx.ease_xoffset(dur=dur, x0=-2000)
    show jojo mech neutral at center, noflip, fx.hover(1.9), fx.ease_xoffset(dur=dur, x0=-2000)
    show kelisha mech neutral at right, fx.hover(2.1), fx.ease_xoffset(dur=dur, x1=1000)
    sanders "We’re approaching the Alexander now. We’ll rush past it and put Jojo in position. Follow me everyone-"
    show bart:
        # TODO I want this to transition from wherever the hover puts him, but it seems to teleport abruptly instead...?
        linear 0.25 yoffset 0
    pause 0.25
    show bart mech as bartglow at right, noflip behind bart:
        blur 12
        matrixcolor ColorizeMatrix(color_bart, color_bart)
        alpha 0.0
        linear 0.5 alpha 1.0
    pause 0.5
    show sanders mech postgrad neutral at left2, noflip, fx.hover(2 * 2.3):
        matrixcolor TintMatrix('#fff')
        linear 0.5 matrixcolor TintMatrix(color_bart)
    show usagi at left, noflip, fx.hover(2 * 1.7):
        matrixcolor TintMatrix('#fff')
        linear 0.5 matrixcolor TintMatrix(color_bart)
    show jojo mech neutral at center, noflip, fx.hover(2 * 1.9):
        matrixcolor TintMatrix('#fff')
        linear 0.5 matrixcolor TintMatrix(color_bart)
    usagi "Guys... I’m losing power... We’re slowing down?"
    jojo "The Alexander has a magnetic tractor beam."
    bart "That’s right. I don’t need you getting any closer. Just sit still while-"
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
    show bart mech neutral at left, noflip, fx.hover(3.7), fx.ease_xpos(dur=1.0, x0=0.85, x1=0.15)
    show kelisha mech neutral at right, noflip, fx.hover(2.1), fx.ease_xoffset(dur=1.0, x0=1000)
    kelisha "That wasn’t me."
    hide usagi
    hide sanders
    hide jojo

    show linda mech neutral at center, fx.hover(1.3), fx.ease_xoffset(dur=1.0, x0=1000), fx.ease_yoffset(dur=1.0, y0=500)
    linda "Ace Unit Shiva here, Carbunkle, Sanders, Usagi, you should be good to go again."
    usagi postgrad neutral "Mom??"
    ### page 78 ###
    linda "I came as soon as I saw the news. No time for shock and surprise. You already knew I was the best Ace there was. Now go, little rabbit! I’ll keep The Alexander busy."
    usagi postgrad neutral "Thanks mom!"

    ###################################
    # > Usagi, Professor Jojo and Sanders rush to the Ultima Cannon
    # scene bg space battlefield
    show bart at fx.hover(3.7), fx.ease_xoffset(dur=0.5, x1=1500)
    show kelisha at fx.hover(2.1), fx.ease_xoffset(dur=0.5, x1=1500)
    show linda at fx.hover(1.3), fx.ease_xoffset(dur=0.5, x1=1500)
    pause 0.5
    hide bart
    hide kelisha
    hide linda
    show usagi mech postgrad neutral at center, fx.hover(1.7), fx.ease_xoffset(dur=0.5, x0=-1500)
    show sanders mech postgrad neutral at left2, fx.hover(2.3), fx.ease_xoffset(dur=0.5, x0=-1500)
    show jojo mech neutral at left, fx.hover(1.9), fx.ease_xoffset(dur=0.5, x0=-1500)
    jojo "Thanks Linda. I won’t let you down."
    usagi "Kagu, buckle up!"
    sanders "Little Rabbit?"
    usagi "Careful... you’re the one who took her cousin away."
    sanders ".... Yeah about that."
    usagi "What do you have to say for yourself and why shouldn’t I blow you up along with Barthandelus."
    sanders "We... never found her, the Queen of New Jersey. It was another cover up. The place that we blew up... just innocent people... The Crown made up a story and we were told to keep quiet...."
    jojo "We’re closing in on the Ultima Cannon now."

    ###################################
    show bart mech neutral at fx.hover(3.7), right, fx.ease_xoffset(dur=1.0, x0=500), fx.ease_ypos(dur=1.0, y0=1.0, y1=ypos_textbox)
    show bg bart hits as barthits behind bart:
        alpha 0.0
        pause 0.5
        linear 1.5 alpha 0.4
    show usagi behind barthits
    show sanders behind barthits
    show jojo behind barthits
    bart "Insolent fools! Alexander primary burst weapon load out."

    # > Linda slices the primary weapon barrel, disabling The
    # > Alexander’s main weapon.
    $ dur = 0.8
    show linda mech neutral at center, flip:
        rotate -15
        fx.ease_pos(dur=dur, xy0=(0.5, 1.5), xy1=(1.0, 0.0))
        rotate 15
        fx.ease_pos(dur=dur, xy0=(0.5, 0.0), xy1=(1.0, 1.5))
    show bg bart hits as barthits:
        pause 0.5
        linear 0.1 alpha 0.0
    show bg linda hits as lindahits behind linda, sanders, usagi, jojo:
        alpha 0.0
        pause 0.5
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.0
        pause 0.1
        pause 0.5
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.0
        pause 0.1
    show bart behind lindahits
        # pause 0.5
        # yshake(5, 10, 0.02)
        # pause 0.1
        # pause 0.5
        # yshake(5, 10, 0.02)
        # pause 0.1
    pause 0.5
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
    show bart:
        flip
        pause 0.7
        noflip
    show bart mech as bartglow at right, behind bart:
        flip
        blur 12
        matrixcolor ColorizeMatrix(color_bart, color_bart)
        alpha 0.0
        linear 0.2 alpha 1.0
        pause 0.5
        noflip
    show linda:
        noflip
        xoffset 0
        yoffset 0
        matrixcolor TintMatrix(color_bart)
        pos (1.5, 1.0)
        ease 1.0 pos (0.67, ypos_textbox)
    pause 1.0

    bart "And so your story ends here."
    ### page 79 ###
    computer "INCOMING BEAM ATTACK"
    bart "What?"
    show queen mech neutral at left, flip, fx.hover(3.1), fx.ease_xoffset(dur=1.0, x0=-1000), fx.ease_yoffset(dur=1.0, y0=-500) behind linda
    show bg queen hits as queenhits behind linda, queen:
        alpha 0.0
        linear 0.08 alpha 0.6
        linear 0.08 alpha 0.0
        pause 0.1
        repeat 3
    show linda:
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
    linda "LIZZY!"
    show linda:
        parallel:
            fx.ease_xoffset(dur=1.0, x1=-500)
        parallel:
            fx.ease_yoffset(dur=0.3, y1=200)
            fx.ease_yoffset(dur=0.7, y0=200, y1=-1200)
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

    kelisha "Already on it, Mega Flare Pierce Rifle, Activate!"
    # > The Bahamut shoots a blast that break’s The Alexander’s
    # > shields.
    bart "No!"

    show queen at flip, fx.hover(3.1), fx.ease_xoffset(dur=2.0, x1=-1000)
    show kelisha at flip, fx.hover(2.1), fx.ease_xoffset(dur=2.0, x1=-1000)
    $ dur = 0.6
    show bart:
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
    show linda mech neutral:
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
    "TODO from here"

    scene bg space battlefield
    show sanders mech postgrad neutral at left2, flip, fx.hover(2.3)
    show usagi mech postgrad neutral at left, flip, fx.hover(1.7)
    show jojo mech neutral at center, flip, fx.hover(1.9)
    jojo "We’re in range, let’s park it right here. I’m taking control of the system now...."
    show bart mech neutral at right2, fx.hover(3.7)
    bart "I may be defeated here... but I WILL NOT LOSE! JUDGEMENT LANCE!"
    # > The Alexander launches a golden lance toward Professor Jojo.
    kelisha neutral "JOSEPH!"
    # > The lance makes impact with Jojo, causing a huge explosion.
    # > He’s gone in an instant.
    ### page 80 ###
    bart "My... friend.... AHHHHHH!"
    hide jojo
    hide bart
    # > Barthandelus and the Alexander go up in a ball of flame and
    # > explosion.
    linda neutral "Joseph.... Bart...."

    sanders "Shit. What do we do now??"
    show takeshi mech neutral at right2, fx.hover(2.5)
    takeshi "Support unit B-100 reporting... Sounds like you need someone who knows how to hack."
    usagi "Takeshi!"
    takeshi "Sorry I couldn’t be here sooner guys. Sanders..."
    sanders "... Well can you stop this thing or not?"
    # > Takeshi begins hacking the Ultima Cannon.
    takeshi "Can I stop this thing, ha!"
    takeshi "Oh... shit."
    sanders "What!? What is it?"
    takeshi "We’ve got a few minutes until the moon crosses Earth’s gravitational threshold."
    sanders "Yeah, and? You can stop the Ultima Cannon right?"
    takeshi "Its been sabotaged. If we disable the tractor beam function... The cannon self destruct. We’ll lose the Ultima Cannon."
    ### page 81 ###
    sanders "Isn’t that what you want? An end to the mining? The Crown’s weapon?"
    takeshi "The self destruct would be instant..."
    sanders "...."
    usagi "...."
    sanders "Well we only have a few minutes. We need to make a decision now. I’ll do it."
    sanders "Save me the shock ok? I know you both hate me. The things I’ve done in the name of the Crown... I realized too late what I had become. Let me redeem myself with this-"

    show child neutral at right, fx.hover(1.3)
    kagu "I can do it. It won’t hurt. I can’t be destroyed."
    usagi "Are you serious Kagu?"
    kagu "Yeah. It’s just..."
    usagi "What?"
    kagu "Well... this will be goodbye."
    kagu "The blast... That will be super heated Ultima Ore. It will be enough energy to complete my evolution instantly..."
    kagu "Look we don’t have time, get out of here. Sorry we didn’t have time for introductions you two."
    sanders "Oh I know who you are."
    takeshi "Me too... part of the intel. It was nice to meet you Sabik."
    kagu "Actually, my name is Kagu. Short for Kaguya, but we don’t have time. Go, now! I’ll see you in a bit."
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