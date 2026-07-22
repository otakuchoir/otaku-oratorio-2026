label start(i=0):
    while i < len_scenes:
        call expression scenes[i].label
        $ i += 1