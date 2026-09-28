# https://otaku-oratorio-2026-gallery.netlify.app/?t=child&t=usagi+postgrad
label scene34:
    scene bg black hole:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    show child mech sad at fx.hover(dur=1.9), center:
        ypos ypos_textbox-0.2
        parallel:
            fx.ease_xoffset(dur=1, x0=-400)
        parallel:
            fx.ease_yoffset(dur=1, y0=800)
    with fade
    pause 1.0
    show bg black as mangabg
    show bg scene34 as manga:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    with dissolve
    # > 34       EXT. SPACE                                                               34
    # > Kagu searches their memory and sees a crystal floating
    # > through the cosmos, then various scenes of Kagu destroying
    # > entire civilizations, including Earth with the Great Flood,
    # > and then again Earth in 2100, the great cataclysm.
    kagu "I’m responsible for this. I... What AM I really. Past lives? Regeneration..."
    kagu "I’m a monster..."
    hide mangabg
    hide manga
    with dissolve
    show bg black hole:
        zoom 1.1
        linear 0.5 zoom 1.0
    show child at fx.hover(1.9):
        ypos ypos_textbox-0.2
        zoom 1.0
        linear 0.5 zoom 0.7
    show usagi mech postgrad worried at right behind child:
        ypos ypos_textbox-0.1
        parallel:
            fx.ease_xoffset(dur=2, x0=-400)
        parallel:
            fx.ease_yoffset(dur=2, y0=1200)
        fx.hover(dur=2.3)

    # > She has followed Kagu in her own mech.
    usagi "Kagu!"
    show child flip at fx.hover(1.9):
        ypos ypos_textbox-0.2
    kagu "Usagi, I-"
    usagi "It’s like I said, you can always change who you were born to be. I have always believed that, trust me."
    usagi "I know how it feels to be labeled. DON’T label yourself. YOU are not a monster."
    show child -flip at fx.hover(dur=1.9):
        ypos ypos_textbox-0.2
    kagu "I only exist for one purpose."
    show usagi mech postgrad cry 1:
        parallel:
            fx.hover(dur=2.3)
        parallel:
            fx.ease_xpos(dur=1.5, x0=0.83, x1=0.16)
        parallel:
            # in general, we should not use the flip transforms for mechs, instead using flip attributes -
            # because mechs have different flipped images.
            # but renpy chokes on the image change here and I don't know why. 
            # usagi specifically has no special flipped mech image, so this is fine. What a pain, renpy...
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