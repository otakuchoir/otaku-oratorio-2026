label scene31a:
    # scene bg black
    scene bg research lab inside
    with dissolve
    # https://genius.com/Genius-english-translations-hakushi-hasegawa-outside-soto-english-translation-lyrics
    # https://drive.google.com/drive/folders/1YfW1BESusTIj58PYCd7fJaNTQko4uopv
    call say_song_line(song_soto, 0)
    call say_song_line(song_soto, 1)
    call say_song_line(song_soto, 2)
    call say_song_line(song_soto, 3)
    call say_song_line(song_soto, 4)
    call say_song_line(song_soto, 5)
    call say_song_line(song_soto, 6)
    call say_song_line(song_soto, 7)
    call say_song_line(song_soto, 8)
    call say_song_line(song_soto, 9, last=True)
    return

define song_soto = Song(Character("Soto (Outside)"), [
    Line("I was told many times, my smile didn't reach\nDidn't reach my eyes",
        "Me no oku ga waratte inaito yoku iwa reta monoda",
        at_measure=5),
    Line("Yeah, I'm sure I was a creepy child\nI couldn't lift the bottoms of my feet off the ground",
        "ā susukigiminowarui kodomodattadarou \\ ashi no ura o jimen kara hanasenakatta",
        at_measure=13),
    Line("I love the outdoors and want to go outside\nThe colors change outside and I love it",
        "Soto ga daisukidakara soto ni detai noda\nsoto wa iro ga kawatte daisukida",
        at_measure=21),
    Line("The distortion is just right\nI think when I see lips around the bottle's throat",
        "Chōdo yoi yugami made ima wa kita yōda nomikuchi ni made haeta kuchibiru o miru to omou",
        at_measure=29),
    Line("Yeah, in my creepy closet were\nMonsters without bass\nAnd DJs",
        "Ā boku no susukigiminowarui kurōzetto ni wa teion no nai bakemono-tachi ya DJ ga iru",
        at_measure=37),
    Line("I love the outdoors and want to go outside\nThe outdoors is so spacious and I love it",
        "Soto ga daisukidakara soto ni detai noda soto wa totemo hirokute daisukida",
        at_measure=45),
    Line("I love the outdoors and want to go outside\nThe colors change outside and I love it",
        "Soto ga daisukidakara soto ni detai noda soto wa iro ga kawatte daisukida",
        at_measure=53),
    Line("I love the outdoors\nI want to go outside",
        "Soto ga daisukida soto ni detai",
        at_measure=61),
    Line("I love the outdoors\nI want to go outside\nThe colors change outside and I love it",
        "Soto ga daisukida soto ni detai soto wa iro ga kawatte daisukida",
        at_measure=69),
], num_measures=73)
