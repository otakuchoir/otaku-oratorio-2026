label scene13a: 
    # https://drive.google.com/drive/folders/1i2WCwJ6NZUS7ksLT_hH0-8Tv0aV-9Y44
    # https://genius.com/Kumiko-noma-lilium-lyrics
    ### page 25 ###
    # > Manga panel sequence of events: Ultima canon is fired,
    # > destroys new jersey.
    scene bg white

    show bg white as bg2 behind bg
    show bg scene13 1:
        subpixel True
        textbox_screen_size
        yoffset -100
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 40 zoom 1.0
    with dissolve
    call say_song_line(song_lilium, 0)
    call say_song_line(song_lilium, 1)
    call say_song_line(song_lilium, 2)

    show bg scene13 2:
        subpixel True
        textbox_screen_size
        yoffset -100
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 40 zoom 1.0
    with dissolve
    call say_song_line(song_lilium, 3)
    call say_song_line(song_lilium, 4)

    show bg scene13 3:
        subpixel True
        textbox_screen_size
        yoffset -100
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 40 zoom 1.0
    with dissolve
    call say_song_line(song_lilium, 5)
    call say_song_line(song_lilium, 6)

    show bg black as bg2
    show bg scene13 4:
        subpixel True
        textbox_screen_size
        yoffset -200
        xalign 0.0
        yalign 1.0
        zoom 1.4
        linear 22 xalign 1.0
        pause 6
        linear 22 xalign 0.5 zoom 1
    with dissolve
    call say_song_line(song_lilium, 7)
    call say_song_line(song_lilium, 8)
    call say_song_line(song_lilium, 9, last=True)

    show bg black with dissolve
    return

define song_lilium = Song(Character("Lilium"), [
    Line("The mouth of the righteous speaketh wisdom\nAnd his tongue talketh of judgment",
        "Os iusti meditabitur sapientiam\nEt lingua eius loquetur indicium",
        at_measure=1),
    Line("Blessed is the man that endureth temptation\nFor when he is tried he shall receive the crown of life",
        "Beatus vir qui suffert tentationem\nQuoniam cum probates fuerit accipiet coronam vitae",
        at_measure=8),
    Line("O Lord, font of bountihood\nO Lord, fire divine, have mercy",
        "Kyrie, fons bonitatis\nKyrie, ignis divine, eleison",
        at_measure=13),
    Line("O how saintly, how serene\nHow benign, how amene is the Virgin credited as!",
        "O quam sancta, quam serena\nQuam benigma, quam amoena esse Virgo creditur",
        at_measure=19),
    Line("O how saintly, how serene, how benign, how amene\nO chastity's Lily",
        "O quam sancta, quam serena, quam benigma, quam amoena\nO castitatis lilium",
        at_measure=25),
    Line("", "(inst. break)", at_measure=31),
    Line("", "(inst. break, background change)", at_measure=39),
    Line("O Lord, font of bountihood\nO Lord, firе divine, have mercy",
        "Kyrie, fons bonitatis\nKyrie, ignis divine, eleison",
        at_measure=46),
    Line("O how saintly, how serene, how benign, how amene\nO chastity's Lily",
        "O quam sancta, quam serena, quam benigma, quam amoena\nO castitatis lilium",
        at_measure=51),
], """
From: Elfen Lied
Kayo Konishi & Yukio Kondo
Arrangement: Anthony Merolla (NYC Otaku Choir)
Translation from Japanese:
https://genius.com/Kumiko-noma-lilium-lyrics
""", num_measures=56, num_seconds=4*60+20)