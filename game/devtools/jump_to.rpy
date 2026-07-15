screen jump_to():
    frame:
        xalign 0.5 yalign 0.5
        # xsize 600 ysize 800
        vbox:
            text "Jump to Scene..."
            textbutton "exit":
                action Hide('jump_to')

            vpgrid:
                cols 2

                $ num_scenes = 29
                for n in range(1, 1+num_scenes):
                    $ s = f"scene{n:02d}"
                    textbutton s:
                        action Start(s)