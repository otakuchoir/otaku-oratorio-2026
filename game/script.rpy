define usagi = Character("Usagi", color="#fd7979", image="usagi")
define takeshi = Character("Takeshi", color="#44bbff", image="takeshi")
define sanders = Character("Sanders", color="#00ff00", image="sanders")
define kelisha = Character("Kelisha", color="#0000ff", image="kelisha")

label start:
    scene bg room

    show usagi-hello at center
    # show usagi-hello at center:
        # matrixcolor TintMatrix("#888888") * SaturationMatrix(0.1)
    # show usagi-frog at top
    show takeshi-happy-1 at right
    show sanders-neutral at left

    usagi "hello..."
    takeshi "...world!"

    return
