# https://otaku-oratorio-2026-gallery.netlify.app/?t=usagi+postgrad&t=sanders+postgrad
label scene20:
    # play music bgm_014_anxious_fart__ff7 if_changed
    scene bg cubicles:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.55, 0.5)
    show usagi postgrad sad at center
    # > 20       INT. DAY; CROWN MILITARY HQ OFFICES                                      20
    # > Usagi is sitting in her cubicle, quietly working. Her phone
    # > buzzes, she looks at it and then ignores it.
    # > Phone buzzes again. She ignores it again.
    usagi "It has been three years since that day. My first... and last deployment."
    show usagi postgrad neutral
    usagi "They took us off the mission and split us up."
    usagi "Takeshi works in another office. Sanders went on to be with the Elites, and I’m stuck here..."
    usagi @ postgrad happy 1 "No... I actually like it here. Away from everything."
    worker "Kitadani, you have a visitor."

    # > Sanders walks in.
    show bg:
        ease 1 pos (0.45, 0.5)
    show usagi:
        xpos 0.5
        ease 1 xpos 0.67
    show sanders postgrad neutral at left2, flip:
        xoffset -800
        ease 1 xoffset 0
    pause 0.5
    show usagi postgrad annoyed
    usagi "So then it’s you calling me from a private number."
    sanders "No, it’s someone much higher up, and you’ve been ignoring it."
    usagi "Sorry, I don’t answer private numbers."
    ### page 38 ###
    sanders "Well, that’s why I’m here. You are to report to The Crown Research facility with me as your... assistant."
    usagi "You? My assistant? You mean, Me your prisoner."
    sanders "Kitadani... I don’t know why you immediately go to that dark place."
    sanders "In 3 years there has been nothing... The Crown has kept you employed... You didn’t do anything so why do you act like-"
    usagi "Cut the crap Sanders. We both know I don’t have a choice, so let’s go."
    show sanders postgrad angry 1
    sanders "No, answer the question. Why do you act like you’re always being watched or that you can’t do what you want when you want?"
    usagi "George... Stop playing in my face."
    return