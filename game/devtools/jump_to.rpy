define jump_to_scene_n = 0
label jump_to_scene:
    call start(i=jump_to_scene_n)

screen jump_to():
    frame:
        xalign 0.5 yalign 0.5
        # xsize 600 ysize 800
        vbox:
            text "Jump to Scene..."
            textbutton "exit":
                action Hide()

            vpgrid:
                cols 2
                for i, scene in enumerate(scenes):
                    textbutton scene:
                        action [SetVariable('jump_to_scene_n', i), Start('jump_to_scene')]