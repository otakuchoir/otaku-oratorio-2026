screen devtools():
    frame:
        xalign 0.5 yalign 0.5
        # xsize 600 ysize 800
        vbox:
            text "Developer Tools"
            textbutton "exit":
                # action Return()
                action Hide('devtools')
            textbutton "gallery":
                action ShowMenu('gallery')
            textbutton "test scene":
                action Start('test_scene')