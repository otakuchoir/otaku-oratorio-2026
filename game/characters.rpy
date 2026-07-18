define usagi = Character("Usagi", color="#fd7979", image="usagi")
define takeshi = Character("Takeshi", color="#44bbff", image="takeshi")
define sanders = Character("Sanders", color="#00ff00", image="sanders")
define kelisha = Character("Professor Kelisha", color="#0000ff", image="kelisha")
define child = Character("Child", color="#dddddd", image="child")
define bart = Character("Barthandelus", color="#6600dd", image="bart")
define jojo = Character("Professor Jojo", color="#666666", image="jojo")
define queen = Character("Queen Elizabeth Newark", color="#ffff00", image="queen")

define takeshis_console = Character(name="Takeshi's console", color="#aaaaaa")

# the background is not a character, but pretending it is is the easiest way to change backgrounds mid-scene
define bg = Character(image="bg")

# redefine builtin positions so the bottom edge of our sprites is sitting on top of the textbox.
transform ytextbox:
    ypos 880
    yanchor 1.0

transform offscreenleft:
    xalign -0.6
    ytextbox
transform left:
    xalign 0.0
    ytextbox
transform left2:
    xalign 0.25
    ytextbox
transform center:
    xalign 0.5
    ytextbox
transform right2:
    xalign 0.75
    ytextbox
transform right:
    xalign 1.0
    ytextbox
transform offscreenright:
    xalign 1.6
    ytextbox