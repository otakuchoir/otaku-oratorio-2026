label start(i=0):
    $ quick_menu = False
    while i < len_scenes:
        call expression scenes[i].label
        $ i += 1