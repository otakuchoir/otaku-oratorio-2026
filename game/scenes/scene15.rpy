# https://otaku-oratorio-2026-gallery.netlify.app/?t=bart&t=jojo&t=sanders+postgrad&t=takeshi+postgrad&t=usagi+postgrad
label scene15: 
    scene bg briefing room
    show sanders postgrad neutral at flip
    show takeshi postgrad neutral at flip
    show bart neutral
    show jojo neutral
    show usagi postgrad derp at flip
    call scene15.camera_left(dur=0)
    with dissolve
    # > 15       INT. DAY; LUNAR ACADEMY BRIEFING ROOM.                                   15
    sanders "This is really weird to say but... Usagi, are you even paying attention?"
    show usagi at noflip
    usagi "Huh?"
    takeshi "Hey... pull yourself together."
    call scene15.camera_right(dur=0.5)
    pause 0.8
    show usagi:
        block:
            flip
            pause 0.05
            noflip
            pause 0.05
            repeat 5
        flip
        "usagi postgrad weary"

    jojo "You three... Since you’ve been graduated, I am not longer your mentor... I am your colleague..."
    jojo "However, I’m going to need you to pay attention, especially in the presence of... our esteemed guest."
    bart "It is understandable that Kitadani may have some questions, professor."

    hide usagi
    show usagi postgrad weary at noflip
    call scene15.camera_right(dur=0)
    call scene15.camera_left(dur=0.5)
    pause 0.5
    show usagi postgrad weary at noflip
    sanders "Sorry to interrupt... {b}{i}I{/i}{/b} don’t think I understand what you’re saying-"
    show takeshi at noflip
    takeshi "They’ve found an energy pattern."
    ### page 27 ###
    sanders "A signal?"
    takeshi "No, an energy pattern... one that matches the planet destroyer from when we were kids. The one that came and doomed the world until-"
    sanders "Until Usagi’s pops blew it away. So what does it mean? And why did it just pop up all of a sudden?"

    show takeshi at flip
    call scene15.camera_center(dur=0.5)
    jojo "We don’t know why, but that is of little consequence right now. We do not want to lose this opportunity, and given that you three are top of your class..."
    show usagi postgrad worried at flip
    jojo "And because Kitadani here is such a symbol of hope for everyone... It only makes sense to send you along with the research team."

    takeshi "So this is our first official mission as members of The Crown."

    # call scene15.camera_right(dur=0.5)
    show bart worried:
        linear 1.5 xpos 0.66
    bart "Yes. But also remember what this means to the people."
    show bart happy 
    bart "Hope, in a time of uncertainty. The daughter of a hero, stepping up to fill her father’s shoes. This is inspiration."

    usagi "I-..."
    # call scene15.camera_center(dur=0.5)
    show usagi at noflip
    takeshi "Listen, I know how you feel about this. But... isn’t it a chance for you to find answers? Maybe?"
    usagi @ confused "No.. I’m just wondering why the pope is here?"
    ### page 28 ###

    show usagi at flip
    jojo "The scientific potential is limitless... and yes, as we all know, the being was sentient."
    jojo "The energy pattern is identical. This may lead to answers for you, Kitadani."
    usagi "I just-"

    jojo "Do it for science."

    # until this moment, I've deliberately avoided having all five characters on screen. That's too many characters!
    # but here, I'm trying to emphasize the pressure Usagi feels from everyone else in the room,
    # so crowding the stage is now deliberate.
    show sanders:
        linear 1 xpos 0.33
    show usagi at noflip
    sanders "Do your duty as a soldier."
    takeshi "Do it for your dad."
    show usagi at flip

    bart neutral "You do want answers, do you not? For the greater good."
    # show usagi:
        # noflip
        # pause 0.3
        # flip
        # pause 0.3
        # repeat 2
        # noflip
        # "usagi postgrad sad"
    show bg black as bg2 behind bg
    $ dur = 3
    show bg:
        alpha 1
        linear dur alpha 0.0
    show sanders:
        alpha 1
        linear dur alpha 0.0
    show takeshi:
        alpha 1
        linear dur alpha 0.0
    show jojo:
        alpha 1
        linear dur alpha 0.0
    show bart:
        alpha 1
        linear dur alpha 0.0
    show usagi postgrad sad
    usagi "I just... I.. I-"
    # > 
    # >          SONG: WEIGHT OF THE WORLD    # > 
    scene bg black with dissolve
    return

# if we try to use these parameters directly in the call below, things break:
# for some reason, each line of dialogue sends us back here, with a "dx is not defined" error!
# no idea why. but assigning the params to globals and using the globals is an
# effective workaround, if a little messy.
init python:
    dx_ = None
    bgx_ = None
    dur_ = None
label scene15.camera(dx=0.0, bgx=0.0, dur=1):
    $ dx_ = dx
    $ bgx_ = bgx
    $ dur_ = dur
    show bg:
        zoom 1.1
        anchor (0.5, 0.5)
        ypos 0.5
        linear dur_ xpos (0.55+bgx_)
    show sanders:
        ytextbox
        linear dur_ xpos (0.2+dx_)
    show takeshi:
        ytextbox
        linear dur_ xpos (0.5+dx_)
    show usagi:
        ytextbox
        linear dur_ xpos (0.85+dx_)
    show jojo:
        ytextbox
        linear dur_ xpos (1.2+dx_)
    show bart:
        ytextbox
        linear dur_ xpos (1.5+dx_)
    return

label scene15.camera_left(dur=1):
    call scene15.camera(dx=0.0, bgx=0.0, dur=dur)
    return

label scene15.camera_right(dur=1):
    call scene15.camera(dx=-0.7, bgx=-0.1, dur=dur)
    return

label scene15.camera_center(dur=1):
    call scene15.camera(dx=-0.35, bgx=-0.05, dur=dur)
    return