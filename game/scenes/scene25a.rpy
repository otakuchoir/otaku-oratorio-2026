define lyrics_baka = "Baka Mitai (I've Been a Fool)"
define baka_slide_dur = 30.0
label scene25a: 
    #scene bg training room
    #show layer master at fx.flashback
    #with dissolve
    # https://genius.com/Genius-english-translations-yakuza-baka-mitai-english-translation-lyrics
    # https://yakuza.fandom.com/wiki/Baka_Mitai_(I've_Been_a_Fool)#Literal_English_Lyrics
    # https://drive.google.com/drive/folders/12Prt24uo9QsDzge6yTZqS_DSEirzdUoB
    call scene25a.slide01
    lyrics_baka ""
    lyrics_baka """
    I've been a fool; how childish\nWent chasing a dream and got hurt\nPoorly disguised behind a joyless smile

    \"I love you\" is hardly ever said\nTongue-tied and downright self-conscious

    But even so, even so, why is it\n\"Goodbye\" came so naturally?
    """

    call scene25a.slide02
    lyrics_baka """
    It's no use, no use, no use at all\nI love you, I love you far too much

    No matter how strong the drink\nThe memories don't fade—what a fool

    I've been a fool; honestly, what a fool\nFilled to the brim with faith in you
    """

    call scene25a.slide03
    lyrics_baka """
    I play the part of the strong woman\nand bathe in the suffocating night air
    
    Since I've been alone, three years have passed\nEven the city streets have changed
    
    But even so, even so, why is it\nI'm still left behind in the past?
    """

    call scene25a.slide04a
    lyrics_baka """
    Really, you're a no-good man, no good at all\nMy matching ring, I take it off
    
    Serves you right! I'm relieved\nYet naively I still wait—what a fool
    """

    call scene25a.slide04b
    lyrics_baka """
    It's no use, no use, no use at all\nI love you, I love you far too much

    No matter how strong the drink\nThe memories don't fade—what a fool
    """

    call scene25a.slide05a
    lyrics_baka """
    Really, you're a no-good man, no good at all\nMy matching ring, I take it off
    """
    
    call scene25a.slide05b
    lyrics_baka """
    Serves you right! I'm relieved\nSo then what are they, these tears—what a fool
    """
    #scene bg training room with dissolve
    #show moba:
    #    zoom 0.3
    #    xalign 1.0
    #    yalign 1.0
    #show moba as moba_frame behind moba:
    #    zoom 0.31
    #    xalign 1.0
    #    yalign 1.0
    #    matrixcolor BrightnessMatrix(-1)
    #show linda moba:
    #    xalign 0.2
    #    yalign 0.5
    #show queen moba:
    #    xalign 0.4
    #    yalign 0.5
    #show huxtable moba:
    #    xalign 0.6
    #    yalign 0.5
    #show kohei moba:
    #    xalign 0.2
    #    yalign 0.2
    #show bart moba:
    #    xalign 0.4
    #    yalign 0.2
    #show jojo moba:
    #    xalign 0.6
    #    yalign 0.2
    ## show circle:
    #    # xalign 0.5
    #    # yalign 0.0
    #pause

    #title "Baka Mitai (I've been a fool)"
    #verse1 "I've been a fool; how childish\nWent chasing a dream and got hurt\nPoorly disguised behind a joyless smile"
    #prechorus "\"I love you\" is hardly ever said\nTongue-tied and downright self-conscious\nBut even so, even so, why is it\n\"Goodbye\" came so naturally?"
    #chorus "It's no use, no use, no use at all\nI love you, I love you far too much\nNo matter how strong the drink\nThe memories don't fade—what a fool"

    #nvl clear
    #verse2 "I've been a fool; honestly, what a fool\nFilled to the brim with faith in you\nI play the part of the strong woman and bathe in the suffocating night air"
    #prechorus "Since I've been alone, three years have passed\nEven the city streets have changed\nBut even so, even so, why is it\nI'm still left behind in the past?"
    #chorus "Really, you're a no-good man, no good at all\nMy matching ring, I take it off\nServes you right! I'm relieved\nYet naively I still wait—what a fool"

    #nvl clear
    #chorus "It's no use, no use, no use at all\nI love you, I love you far too much\nNo matter how strong the drink\nThe memories don't fade—what a fool"
    #chorus "Really, you're a no-good man, no good at all\nMy matching ring, I take it off\nServes you right! I'm relieved\nSo then what are they, these tears—what a fool"
    return

init python:
    import dataclasses
    class Circle(renpy.Displayable):
        def __init__(self, radius, color='#ffffff', **kwargs):
            super(Circle, self).__init__(**kwargs)
            self.radius = radius
            self.color = color

        def render(self, width, height, st, at):
            render = renpy.Render(self.radius*2, self.radius*2)
            canvas = render.canvas()
            canvas.circle(self.color, (self.radius, self.radius), self.radius)
            return render
    
    def moba_profile(name, color, crop, offset=(0, 0)):
        circle = Circle(radius=100, color=color)
        # print(crop, offset)
        face = Transform(renpy.get_registered_image(name), crop=crop)
        profile = AlphaMask(child=face, mask=circle)
        return Composite((200, 200), (0, 0), circle, offset, profile)

# scene 25 - these are cropped into moba sprites
image linda moba = moba_profile('linda young neutral focus', '#8888ff', (20, 0, 200, 200))
image queen moba = moba_profile('princess neutral focus', '#8888ff', (250, 90, 200, 200))
image huxtable moba = moba_profile('huxtable young neutral focus', '#8888ff', (150, 70, 200, 200))
image kohei moba = moba_profile('kohei young neutral focus', '#ff8888', (150, 0, 200, 200))
image bart moba = moba_profile('bart young neutral focus', '#ff8888', (40, 150, 200, 200))
image jojo moba = moba_profile('jojo young neutral focus', '#ff8888', (170, 30, 200, 200))


label scene25a.slide01:
    # opening faceoff - linda confidently charging in, kohei looking a bit worried
    scene black
    show layer master at fx.flashback
    show bg training room:
        zoom 1.2
        anchor (0.5, 0.5)
        pos (0.5, 0.60)
        fx.ease_yoffset(baka_slide_dur, y1=-200)
    show kohei young mech worried focus at left, flip, fx.ease_yoffset(baka_slide_dur, y1=-200)
    show linda young mech serious focus at right, fx.ease_yoffset(baka_slide_dur, y1=-200):
        rotate -15
    with dissolve
    return

label scene25a.slide02:
    # linda kicking kohei's ass, bart looking worried in the background
    # (deliberately not showing queen + huxtable fighting, linda's the star in this scene)
    scene black
    show layer master at fx.flashback
    show bg training room:
        zoom 1.2
        anchor (0.5, 0.5)
        pos (0.4, 0.50)
        fx.ease_xoffset(baka_slide_dur, x1=200)
    show bart young mech anxious behind kohei:
        zoom 0.5
        flip
        pos (-0.1, 0.7)
        rotate 0
        fx.ease_xoffset(baka_slide_dur, x1=200)
    show kohei young mech panic 2 focus:
        flip
        pos (0.35, ypos_textbox+0.05)
        rotate -45
        fx.ease_xoffset(baka_slide_dur, x1=200)
    show linda young mech serious focus:
        pos (0.5, 0.6)
        rotate 45
        fx.ease_xoffset(baka_slide_dur, x1=200)
    with dissolve
    return

label scene25a.slide03:
    # now it's bart's turn, linda's hitting him from behind. kohei's down for the count
    scene black
    show layer master at fx.flashback
    show bg training room:
        zoom 1.2
        anchor (0.5, 0.5)
        pos (0.6, 0.50)
        fx.ease_xoffset(baka_slide_dur, x1=-200)
    show kohei young mech panic 1:
        flip
        pos (1.15, ypos_textbox+0.25)
        rotate -105
        fx.ease_xoffset(baka_slide_dur, x1=-200)
    show linda young mech serious focus:
        flip
        pos (0.40, 0.6)
        rotate -15
        fx.ease_xoffset(baka_slide_dur, x1=-200)
    # show bart young mech shock focus as b2:
    show bart young shock focus as bart_pilot:
        zoom 0.5
        pos (0.635, 0.355)
        rotate 15
        fx.ease_xoffset(baka_slide_dur, x1=-200)
    show bart mech focus:
        flip
        pos (0.6, ypos_textbox+0.15)
        rotate 15
        fx.ease_xoffset(baka_slide_dur, x1=-200)
    with dissolve
    return

label scene25a.slide04a:
    # jojo's next to die. his mech's jammed, he's doomed
    # linda blinks behind him, and a few seconds later his mech's sliced in half, as per the meme
    scene black
    show layer master at fx.flashback
    show bg training room:
        zoom 1.2
        anchor (0.5, 0.5)
        pos (0.4, 0.50)
        fx.ease_xoffset(baka_slide_dur, x1=200)
    show linda young mech serious focus:
        pos (0.70, ypos_textbox+0.1)
        fx.ease_xoffset(baka_slide_dur, x1=200)
        # the slice!
        # fx.ease_xoffset(0.10, x1=-800)
    show jojo young mech crying focus:
        anchor (0.5, 1.0)
        flip
        pos (0.30, ypos_textbox+0.3)
        fx.ease_xoffset(baka_slide_dur, x1=200)
    with dissolve
    # pause baka_slide_dur + 2.0
    return

label scene25a.slide04b:
    show bg training room:
        xoffset 200
    show linda young mech serious focus:
        pos (0.70, ypos_textbox+0.1)
        # the slice!
        linear 0.1 xoffset -800
        pause 1.9
        # alpha 0.0
        # "linda young mech smile focus" # omg why doesn't this work wtf
    # workaround because changing the expression above didn't work
    show linda young mech smile focus as linda2:
        # pos (0.70, ypos_textbox+0.04)
        pos (0.70, ypos_textbox+0.1)
        xoffset -800
        alpha 0.0
        pause 2.0
        alpha 1.0
    show jojo young mech crying focus:
        anchor (0.5, 1.0)
        flip
        pos (0.30, ypos_textbox+0.3)
        xoffset 200
        alpha 1.0
        pause 2.0
        linear 0.5 alpha 0.0
    show jojo young mech crying focus as jojo_head:
        crop (0, -0.5, 1.0, 1.0)
        anchor (0.5, 1.0)
        flip
        rotate 90
        pos (0.68, ypos_textbox+0.5)
        xoffset 200
        alpha 0.0
        pause 2.0
        linear 0.5 alpha 1.0
    show jojo young mech crying focus as jojo_legs:
        crop (0, 0.5, 1.0, 0.5)
        anchor (0.5, 1.0)
        flip
        pos (0.30, ypos_textbox+0.3)
        xoffset 200
        alpha 0.0
        pause 2.0
        linear 0.5 alpha 1.0
    return

label scene25a.slide05a:
    # linda's team celebrates their win
    scene black
    show layer master at fx.flashback
    show bg training room:
        zoom 1.2
        anchor (0.5, 0.5)
        pos (0.4, 0.50)
    show princess mech smug 2 focus:
        pos (0.80, ypos_textbox+0.1)
    show huxtable young mech wink focus:
        flip
        pos (0.15, ypos_textbox+0.1)
    show linda young mech happy 2 focus:
        flip
        pos (0.50, ypos_textbox+0.1)
    with dissolve
    return

label scene25a.slide05b:
    # losers pouting
    scene black
    show layer master at fx.flashback
    show bg training room:
        zoom 1.2
        anchor (0.5, 0.5)
        pos (0.6, 0.50)
    show jojo mech crying focus:
        pos (0.80, ypos_textbox+0.1)
    show bart young mech angry 2 focus:
        flip
        pos (0.15, ypos_textbox+0.1)
    show kohei young mech worried focus:
        flip
        pos (0.50, ypos_textbox+0.1)
    with dissolve
    return