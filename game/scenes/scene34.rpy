# https://otaku-oratorio-2026-gallery.netlify.app/?t=child&t=usagi+postgrad
label scene34:
    # TODO scaling is weird here, it's the only scene that shows both non-mechs and mechs.
    # but making child super-tiny looks bad, so let's not worry about it...?
    scene bg black hole:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    show child mech sad at center:
        ypos ypos_textbox-0.2
        parallel:
            fx.ease_xoffset(dur=1, x0=-400)
        parallel:
            fx.ease_yoffset(dur=1, y0=800)
        fx.hover(dur=1.9)
    with fade
    "PLACEHOLDER manga panels: kagu's memories"
    # > 34       EXT. SPACE                                                               34
    # > Kagu searches their memory and sees a crystal floating
    # > through the cosmos, then various scenes of Kagu destroying
    # > entire civilizations, including Earth with the Great Flood,
    # > and then again Earth in 2100, the great cataclysm.
    kagu "I’m responsible for this. I... What AM I really. Past lives? Regeneration..."
    kagu "I’m a monster..."
    show bg black hole:
        zoom 1.1
        linear 0.5 zoom 1.0
    show child:
        zoom 1.0
        linear 0.5 zoom 0.7
    show usagi mech postgrad worried at right behind child:
        ypos ypos_textbox-0.1
        parallel:
            fx.ease_xoffset(dur=2, x0=-400)
        parallel:
            fx.ease_yoffset(dur=2, y0=800)
        fx.hover(dur=2.3)
    # > She has followed Kagu in her own mech.
    usagi "Kagu!"
    show child:
        flip
        fx.hover(dur=1.9)
    kagu "Usagi, I-"
    usagi "It’s like I said, you can always change who you were born to be. I have always believed that, trust me."
    usagi "I know how it feels to be labeled. DON’T label yourself. YOU are not a monster."
    show child:
        noflip
        fx.hover(dur=1.9)
    kagu "I only exist for one purpose."
    show usagi mech postgrad cry 1:
        parallel:
            fx.hover(dur=2.3)
        parallel:
            fx.ease_xpos(dur=1.5, x0=0.83, x1=0.16)
        parallel:
            noflip
            pause 0.75
            flip
    usagi "No! That’s not true."
    kagu "It IS true. I have seen my past lives."
    # > (MORE)
    ### page 69 ###
    kagu "All of them. It’s all so clear now. I remember every-little-detail. I remember that I responded to your planet’s cries. I doomed the humans to their fate, and then I waited for the day of the eclipse to come back. I-"
    show child mech neutral:
        parallel:
            fx.hover(dur=1.9)
        parallel:
            noflip
            pause 0.3
            flip
            pause 0.3
            repeat 3
    show usagi mech postgrad worried
    usagi "Kagu?..... Kagu? What’s wrong."
    show child mech confused
    kagu "I remember every single detail. So why is this... different?"
    usagi "What? What’s different?"
    show child:
        noflip
        fx.hover(dur=1.9)
    kagu "The alignment of your Star, your Earth and your Earth’s moon."
    usagi "It has been almost 20 years... You’re a cosmic being, surely you know that these things move-"
    show child mech neutral
    kagu "It has been 19 year, 237 days, 16 hours, and 22 minutes. The positioning of everything is off."
    show child mech serious 
    kagu "No... NO!" 
    show child:
        flip
        parallel:
            fx.ease_xoffset(dur=1.0, x1=-100)
            fx.ease_xoffset(dur=1.0, x0=-100, x1=300)
        parallel:
            ease 1.0 yoffset -200
            fx.ease_yoffset(dur=1.0, y0=-200, y1=1200)
    show usagi:
        pause 1.0
        flip
        parallel:
            fx.ease_xoffset(dur=1.0, x1=-100)
            fx.ease_xoffset(dur=1.0, x0=-100, x1=300)
        parallel:
            ease 1.0 yoffset -200
            fx.ease_yoffset(dur=1.0, y0=-200, y1=1200)
    pause 3

    # > Kagu flies off toward the Moon. Usagi follows.
    return