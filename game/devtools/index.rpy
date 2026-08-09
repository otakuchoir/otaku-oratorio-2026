screen devtools():
    frame:
        xalign 0.5 yalign 0.5
        # xsize 600 ysize 800
        vbox:
            text "Developer Tools"
            textbutton "exit":
                action Hide()
            textbutton "image gallery":
                action ShowMenu('image_gallery')
            textbutton "sound test":
                action ShowMenu('sound_test')