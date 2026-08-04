define usagi = Character("Usagi", color="#fd7979", image="usagi")
define takeshi = Character("Takeshi", color="#44bbff", image="takeshi")
define sanders = Character("Sanders", color="#00ff00", image="sanders")
define kelisha = Character("Professor Kelisha", color="#4444ff", image="kelisha")
define takeshis_console = Character(name="Takeshi's console", color="#aaaaaa")
define bart = Character("Barthandelus", color="#6600dd", image="bart")
define jojo = Character("Professor Jojo", color="#666666", image="jojo")
define linda = Character("Linda Kitadani", color="#d68e8e", image="linda")
define kohei = Character("Kohei Kitadani", color="#00bb00", image="kohei")
# same character, using different names/titles in different parts of the script
define child = Character("Child", color="#dddddd", image="child")
define noname = Character("NoName", color="#dddddd", image="child")
define kagu = Character("Kagu", color="#dddddd", image="child")
# same character, using different names/titles in different parts of the script
define queen = Character("Queen Elizabeth Newark", color="#ffff00", image="queen")
define princess = Character("Princess Elizabeth Newark", color="#ffff00", image="queen")
# same character, using different names/titles in different parts of the script
define general = Character("Elite General", color="#c99e61", image="huxtable")
define huxtable = Character("Robert Huxtable", color="#c99e61", image="huxtable")
define reporter1 = Character("News Reporter 1", color="#aaaaaa", image="reporter1")
define reporter2 = Character("News Reporter 2", color="#aaaaaa", image="reporter2")
define reporter3 = Character("News Reporter 3", color="#aaaaaa", image="reporter3")

# the background is not a character, but pretending it is is the easiest way to change backgrounds mid-scene
define bg = Character(image="bg")

image bg default = Solid("#cccccc")

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

transform ytop:
    yanchor 0.0

transform topoffscreenleft:
    xalign -0.6
    ytop
transform topleft:
    xalign 0.0
    ytop
transform topleft2:
    xalign 0.25
    ytop
transform topcenter:
    xalign 0.5
    ytop
transform topright2:
    xalign 0.75
    ytop
transform topright:
    xalign 1.0
    ytop
transform topoffscreenright:
    xalign 1.6
    ytop