
label scene31:
    scene bg research lab inside
    show usagi postgrad serious 2 at left, flip
    show sanders postgrad angry 1 at center
    show jojo serious at right2
    show bart peaceful at right
    with fade
    # show child neutral at right
    # > 31       INT. DAY; CROWN MILITARY RESEARCH LAB.                                   31
    sanders "And that’s the recording we retrieved."
    usagi "I can’t believe you’ve been spying on me."
    jojo @ serious 2 "Everywhere you turn these days... traitors to the crown."
    show bart grin 1
    jojo "Kitadani, the work we’re doing here is too important to bungle... and messing up could mean the end of everyone."
    show bart peaceful
    sanders "... which is exactly what we’re trying to prevent. But it can’t happen if people like... him... are running around trying to undermine the crown-"
    usagi @ angry "Just admit it George. You never liked Takeshi because he’s a colony born. A Lunar."
    show sanders postgrad angry 2
    show bart shock
    sanders "... It’s them and their WACKY beliefs that got us here in the first place."
    show bart stern
    show sanders postgrad eyeroll at flip
    bart "Watch your mouth. Those are the scriptures you’re talking about."
    show bart neutral
    show sanders postgrad angry 1 at noflip
    ### page 62 ###
    show usagi postgrad worried
    jojo "Usagi, if you do not follow directions for... Project Kaguya... then we will be forced to send Sanders here after your friend."
    usagi @ postgrad sad ".... Fine. I’ll do what you say. Just leave Takeshi out of it."
    jojo "Then shall we begin for today?"
    show jojo at flip, fx.ease_xoffset(dur=1, x1=800)
    show bart at flip, fx.ease_xoffset(dur=1, x1=800)
    show sanders postgrad neutral:
        flip
        fx.ease_xpos(dur=0.8, x0=0.5, x1=0.83)
        noflip
    show usagi at fx.ease_xpos(dur=0.5, x0=0.16, x1=0.33)
    usagi "Sanders. You remember our first summer together, when we visited Earth? Takeshi’s first time?"
    sanders @ postgrad happy "Yeah. He was freaking out about cars. Really loved the idea of a road trip.... He wouldn’t stop talking about it for the rest of the year."
    usagi @ postgrad sad "Takeshi never hated Earth, Sanders. Remember that."
    hide bart
    hide jojo
    show sanders at flip, fx.ease_xoffset(dur=1, x1=800)
    pause 0.5
    show usagi postgrad happy 1:
        noflip
        pause 0.8
        flip
    show child happy at right2:
        parallel:
            flip
            pause 0.8
            noflip
        parallel:
            fx.ease_xoffset(dur=1.3, x0=-1100, x1=200)
            fx.ease_xoffset(dur=0.7, x0=200)
        parallel:
            fx.hover(dur=0.6, loops=3)
        parallel:
            fx.ease_ypos(dur=1.5, y0=0.3, y1=0.6)
            fx.ease_ypos(dur=0.5, y0=0.6, y1=ypos_textbox)
    kagu "Hey mom, what’s up?"
    usagi "Oh, hey Kagu... Wow... you’re pretty fluent. Its only been a few days since I last saw-"
    show child neutral
    kagu "That’s right. But after all, I AM a sentient cosmic being that alters its appearance to fit the confines of your human mind."
    usagi "Oh wow."
    kagu @ happy 2 "Yeah, pretty impressive, huh? My development is awfully fast by your standards."
    kagu @ happy "When you found me in the crystal, I had been regenerating for almost 17 years. But now that I’m out? Time to learn everything I can about you humans. You’re really interesting."
    ### page 63 ###
    show usagi postgrad confused
    usagi "Regenerating?"
    show usagi postgrad worried
    kagu "Yeah, after my past life ended. I regenerate. I’ve been watching dramas. I think you humans don’t regenerate when your life leaves you."
    usagi "Yeah... no. Hey Kagu, so you don’t remember anything from before? From... your past life?"
    kagu "It’s kind of... how would you say...? Foggy? I can kind of remember some things, but it’s all a blur right now."

    hide sanders
    bart grin 2 "This is exactly the right path Joseph, soon it will remember its true purpose."
    jojo sad "That would be a BAD thing, Bart... Let her work, she’s probably the only one who can... repurpose it."
    bart grin 1 "..."
    usagi "How can I help you remember?"
    kagu "Well, the story you told me really helped expand my mind. From there, I was able to piece a whole bunch of things together."
    show usagi postgrad happy 1
    show child happy
    kagu "Then Professor Jojo back there, he gave me a holo device. That’s how I watch the dramas."
    kagu @ happy 2 "Have you seen the series, I Got Hit By a Bus and Now My Love Triangle of Friends are RPG Heroes? That one cracks me up!"
    show usagi postgrad happy 2
    usagi "Actually... I do know that one. It’s pretty good. The part with the pirate cats was hilarious."
    ### page 64 ###
    # > A glitch
    show usagi postgrad shock
    show bg at fx.glitch_lights
    call fx.glitch_child
    show child happy 2
    kagu "THE PIRATE CATS! HAHA!"
    show usagi postgrad worried
    usagi "What was that?"
    show usagi postgrad neutral
    show child happy
    kagu "That was.... When a part of me evolves, that happens. Laughter... with... another person. Camaraderie."
    show usagi postgrad happy 1
    show child neutral
    kagu "First... Wonder... when you read me the story, remember? And now... Camaraderie. Wow... Thank you Mom."
    usagi "I see...."
    bart angry 1 "No, Joseph this is not right-"
    jojo serious 2 "Bart! How many times do I have to tell you!? Let-Her-Work!"
    bart worried "But she’s doing it wrong, she’s..."
    usagi ".... Kagu... what do you desire? What do you... want? What are your hopes, and dreams?"

    show child confused
    kagu "Hopes... and... dreams?"
    # > Glitch glitch glitch
    show bg at fx.glitch_lights
    call fx.glitch_child
    show child neutral

    bart angry 2 "No! She knows what she is doing! She’s HUMANIZING IT!"
    # > Glitch glitch glitch
    show bg at fx.glitch_lights
    call fx.glitch_child

    kagu "Hopes.... And .... Dreams..... What do I want?"
    # > 
    # > SONG: SOTO    # > 
    # > BLACKOUT
    ### page 65 ###
    # scene bg black with fade
    return