define jump_to_scene_n = 0
label jump_to_scene:
    call start_at(jump_to_scene_n)

screen jump_to():
    frame:
        xalign 0.5 yalign 0.5
        xsize 1000 ysize 1000
        vbox:
            text "Jump to Scene..."
            textbutton "exit":
                action Hide()

            vpgrid:
                scrollbars "vertical"
                mousewheel True
                draggable True
                cols 1
                # spacing 15

                for i, scene in enumerate(scenes):
                    textbutton str(scene):
                        xminimum 1000
                        action [SetVariable('jump_to_scene_n', i), Start('jump_to_scene')]