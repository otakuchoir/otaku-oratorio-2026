label scene25a: 
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

    scene bg black with dissolve
    # https://genius.com/Genius-english-translations-yakuza-baka-mitai-english-translation-lyrics
    # https://yakuza.fandom.com/wiki/Baka_Mitai_(I've_Been_a_Fool)#Literal_English_Lyrics
    # https://drive.google.com/drive/folders/12Prt24uo9QsDzge6yTZqS_DSEirzdUoB
    nvl clear
    title "Baka Mitai (I've been a fool)"
    verse1 "I've been a fool; how childish\nWent chasing a dream and got hurt\nPoorly disguised behind a joyless smile"
    prechorus "\"I love you\" is hardly ever said\nTongue-tied and downright self-conscious\nBut even so, even so, why is it\n\"Goodbye\" came so naturally?"
    chorus "It's no use, no use, no use at all\nI love you, I love you far too much\nNo matter how strong the drink\nThe memories don't fade—what a fool"

    nvl clear
    verse2 "I've been a fool; honestly, what a fool\nFilled to the brim with faith in you\nI play the part of the strong woman and bathe in the suffocating night air"
    prechorus "Since I've been alone, three years have passed\nEven the city streets have changed\nBut even so, even so, why is it\nI'm still left behind in the past?"
    chorus "Really, you're a no-good man, no good at all\nMy matching ring, I take it off\nServes you right! I'm relieved\nYet naively I still wait—what a fool"

    nvl clear
    chorus "It's no use, no use, no use at all\nI love you, I love you far too much\nNo matter how strong the drink\nThe memories don't fade—what a fool"
    chorus "Really, you're a no-good man, no good at all\nMy matching ring, I take it off\nServes you right! I'm relieved\nSo then what are they, these tears—what a fool"
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
