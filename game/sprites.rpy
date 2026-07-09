define usagi = Character("Usagi", color="#fd7979", image="usagi")
define takeshi = Character("Takeshi", color="#44bbff", image="takeshi")
define sanders = Character("Sanders", color="#00ff00", image="sanders")
define kelisha = Character("Kelisha", color="#0000ff", image="kelisha")

transform dim:
    matrixcolor BrightnessMatrix(-0.25)
    zoom 0.95
transform nodim:
    matrixcolor BrightnessMatrix(0)
    zoom 1

init python:
    # for name in ["usagi hello"]:
    # this loop changes the list of registered images, so expand the list first with list()
    for name in list(renpy.list_images()):
        if name in ["text", "vtext"]:
            continue
        img = renpy.get_registered_image(name)
        renpy.image(name+" dim", dim(img))