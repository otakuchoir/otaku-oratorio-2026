
screen sound_test():
    frame:
        xalign 0.5 yalign 0.5
        xsize 1000 ysize 1000
        vbox:
            text "Sound test"
            textbutton "exit":
                action [Stop('sound'), Stop('music'), Hide()]
            textbutton "stop all sounds":
                action [Stop('sound'), Stop('music')]

            vpgrid:
                scrollbars "vertical"
                mousewheel True
                draggable True
                cols 1
                # spacing 15

                $ audio_list = [f for f in fs if re.match(r"^audio\/(?P<basename>.*).(opus|ogg|mp3|flac|wav)$", f)]
                for audio in audio_list:
                    textbutton audio:
                        xminimum 1000
                        action [Play("sound", audio)]