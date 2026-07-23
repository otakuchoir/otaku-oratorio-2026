screen changelog():
    frame:
        xalign 0.5 yalign 0.5
        xsize 1000 ysize 1000
        vbox:
            text "Changelog"
            textbutton "exit":
                action Hide()

            vpgrid:
                scrollbars "vertical"
                mousewheel True
                draggable True
                cols 1
                xminimum 1000

                text changelog
