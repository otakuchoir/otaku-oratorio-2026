label scene09a: 
    scene bg usagi dorm night with dissolve
    # https://genius.com/Genius-english-translations-dali-moonlight-legend-english-translation-lyrics
    # https://drive.google.com/drive/folders/1DN1PKkUOmgE0XtfsA1OPBGLHYPE2UE14
    call say_song_line(song_sailormoon, 0)
    call say_song_line(song_sailormoon, 1)
    call say_song_line(song_sailormoon, 2)
    call say_song_line(song_sailormoon, 3)
    call say_song_line(song_sailormoon, 4)
    call say_song_line(song_sailormoon, 5)
    call say_song_line(song_sailormoon, 6)
    call say_song_line(song_sailormoon, 7)
    call say_song_line(song_sailormoon, 8)
    call say_song_line(song_sailormoon, 9)
    call say_song_line(song_sailormoon, 10)
    call say_song_line(song_sailormoon, 11)
    call say_song_line(song_sailormoon, 12)
    call say_song_line(song_sailormoon, 13)
    call say_song_line(song_sailormoon, 14)
    call say_song_line(song_sailormoon, 15)
    call say_song_line(song_sailormoon, 16, last=True)
    return

define song_sailormoon = Song(Character("Moonlight Densetsu (Moonlight Legend)"), [
    Line("I’m sorry, it’s hard for me to say\nAlthough it’s easy to say it in my dreams",
        "Gomen ne sunao janakute\nYume no naka nara ieru",
        at_measure=11),
    Line("My thought circuit is about to break down\nYou know right now, I want you with me",
        "Shikoukairo wa short sunzen\nIma sugu aitaiyo",
        at_measure=15),
    Line("It has me nearly in tears, this moonlight\nCan’t even call you because it’s midnight",
        "Nakitaku naru youna moonlight\nDenwa mo dekinai midnight",
        at_measure=19),
    Line("But my heart is sincere, what can I do?\nMy heart is a kaleidoscope",
        "Datte junjo doushiyou\nHaato wa mangekyou",
        at_measure=23),
    Line("The moonlight guides us to our destination dear\nTime and again, we’ll find each other",
        "Tsuki no hikari ni michibikare\nNando mo meguri au",
        at_measure=27),
    Line("Counting the sparkles of the constellations\nForetelling me the future of this romance",
        "Seiza no matataki kazoe\nUranau koi no yukue",
        at_measure=35),
    Line("We were born on the same planet\nThis is thе miracle of romance",
        "Onaji kuni ni umaretano\nMirakuru romansu",
        at_measure=39),
    Line("I wish that we could havе another weekend\nI wish upon a star for a happy end",
        "Moichido futari de weekend\nKamisama kanaete happy-end",
        at_measure=47),
    Line("Across the past, the present, and future\nI’ll always be in love with you",
        "Genzai kako miraimo\nAnatani kubittake",
        at_measure=51),
    Line("When we first met, I felt a sense of déjà vu\nYour eyes, your gaze, I’ll never forget",
        "Deatta toki no natsukashii\nManazashi wasure nai",
        at_measure=55),
    Line("From millions of stars in this universe,\nI’ll know the one that leads me to you",
        "Ikusenman no hoshi kara anata wo mitsukerareru",
        at_measure=63),
    Line("You can transform coincidences into chances\nI love the way you live your life",
        "Guuzen mo chansu ni kaeru\nIkikata ga sukiyo",
        at_measure=67),
    Line("", "", at_measure=71),
    Line("Our lives are entwined with wondrous miracles\nTime and again, we’ll find each other",
        "Fushigi na kiseki kurosu shite\nNando mo meguri au",
        at_measure=79),
    Line("Counting the sparkles of the constellations\nForetelling me the future of this romance",
        "Seiza no matataki kazoe\nUranau koi no yukue",
        at_measure=87),
    Line("We were born on the same planet\nThis is the miracle of romance\nI believe in it, this is the miracle of romance",
        "Onaji kuni ni umaretano\nMirakuru romansu\nShinjite iruno mirakuru romansu",
        at_measure=91),
], """
From: Sailor Moon (Opening)
Original: DALI
Choral Arrangement: Yulin Ni (NYC Otaku Choir)
Translation from Japanese:
https://genius.com/Dali-jpn-moonlight-legend-lyrics
""", num_measures=99)