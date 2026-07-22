screen gallery():
    frame:
        xalign 0.5 yalign 0.5
        # xsize 600 ysize 800
        vbox:
            text "All Registered Images"
            textbutton "exit":
                action Hide()
            # viewport:
            vpgrid:
                scrollbars "vertical"
                mousewheel True
                draggable True
                cols 6
                spacing 15

                for img in renpy.list_images():
                    # not sure why these are listed, they're not images and they break things. ignore them
                    if img in ["text", "vtext"]:
                        continue
                    # tried to display image dimensions and failed. they'd take up too much screen space anyway
                    # python:
                        # (w,h) = renpy.image_size(img)
                        # (w,h) = renpy.render(Image(img), config.screen_width, config.screen_height, 0, 0).get_size()
                    vbox:
                        yminimum 280
                        align (0.5, 0.0)
                        # vbox stuff gets the alignment just right.
                        # there's probably a better/shorter way to do this, I'm not good at renpy styling yet
                        vbox:
                            yminimum 200
                            align (0.5, 0.0)
                            add img xalign 0.5 yalign 0.5 xysize (200, 200) fit 'contain'
                        vbox:
                            yminimum 60
                            align (0.5, 0.0)
                            text "[img]"
                            # it'd be convenient to copy-paste image names from this screen...
                            # but we can't select and copy text from the renpy ui, as far as I can tell.
                            # a button can do it, but it's too unclear to users what the button does.
                            # not yet worth the trouble to add an icon or a "copied to clipboard" toast to clarify it.
                            # textbutton img:
                                # action CopyToClipboard(img)