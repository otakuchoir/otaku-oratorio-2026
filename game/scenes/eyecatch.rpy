# eyecatch direction: https://discord.com/channels/1307031043915911278/1308533742209335336/1544806536621064283
# copied into the comments/placeholders below
init python:
    for i in [2, 4, 6, 9, 11, 13, 15, 23, 26, 29, 38]:
        load_image(f'eyecatch scene{i:02d}', f'assets/Eyecatches/eyecatch-scene{i:02d}-{i+1:02d}.png') # type: ignore

label eyecatch_scene02:
    scene black with fade
    show eyecatch scene02 at truecenter, screen_size
    with fade
    pause
    scene black with fade
    return
label eyecatch_scene04:
    scene black with fade
    show eyecatch scene04 at truecenter, screen_size
    with fade
    pause
    scene black with fade
    return
label eyecatch_scene06:
    scene black with fade
    show eyecatch scene06 at truecenter, screen_size
    with fade
    scene black with fade
    return
label eyecatch_scene09:
    scene black with fade
    show eyecatch scene09 at truecenter, screen_size
    with fade
    pause
    scene black with fade
    return
label eyecatch_scene11:
    scene black with fade
    show eyecatch scene11 at truecenter, screen_size
    with fade
    pause
    scene black with fade
    return

label eyecatch_scene13:
    # Between 13/14 - completely silent Black canvas white line, Ultima Canon photo. 
    # it's the wrong aspect ratio, so we take a little extra trouble here to display it right
    scene black
    show eyecatch scene13 at truecenter, screen_size
    with fade
    pause
    scene black with fade
    return
    
label eyecatch_scene15:
    scene black with fade
    show eyecatch scene15 at truecenter, screen_size
    with fade
    scene black with fade
    return

label eyecatch_scene23:
    scene black with fade
    show eyecatch scene23 at truecenter, screen_size
    with fade
    pause
    scene black with fade
    return
label eyecatch_scene25:
    scene black with fade
    "PLACEHOLDER 25/26 - class portrait of the young version of the older cast (adults: Jojo, Barthandelus, Linda, Elizabeth, Huxtable, Kohei)"
    scene black with fade
    return
label eyecatch_scene26:
    scene black with fade
    show eyecatch scene26 at truecenter, screen_size
    with fade
    scene black with fade
    return
label eyecatch_scene29:
    # Between 29/30 - something about Sabik, the Great Resetter, destroys planets when humanity does too much. 
    scene eyecatch scene29 at screen_size with fade
    pause
    scene black with fade
    return

label eyecatch_scene38:
    scene black with fade
    show eyecatch scene38 at truecenter, screen_size
    with fade
    scene black with fade
    return

label eyecatch_scene40:
    scene black with fade
    "PLACEHOLDER 40/41 - Linda, Usagi and Elizabeth something nice even if it's just a portrait no words needed. "
    scene black with fade
    return