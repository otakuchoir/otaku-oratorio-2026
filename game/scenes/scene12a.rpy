label scene12a: 
    scene bg earth tarmac
    with dissolve
    # https://drive.google.com/drive/folders/1dsZ4siMeRTHh7fJEdIaZy-hh1EWzfB-c
    # https://lyricstranslate.com/en/shang-hai-tan-shanghai-beach.html
    call say_song_line(song_shanghai, 0)
    call say_song_line(song_shanghai, 1)
    call say_song_line(song_shanghai, 2)
    call say_song_line(song_shanghai, 3)
    call say_song_line(song_shanghai, 4)
    call say_song_line(song_shanghai, 5)
    call say_song_line(song_shanghai, 6)
    call say_song_line(song_shanghai, 7)
    call say_song_line(song_shanghai, 8)
    call say_song_line(song_shanghai, 9)
    call say_song_line(song_shanghai, 10)
    call say_song_line(song_shanghai, 11)
    call say_song_line(song_shanghai, 12, last=True)
    return

define song_shanghai = Song(Character("Shanghai Tan (Shanghai Beach)"), [
    Line("The rushing water rhythms\nIt is a river stretching for thousands of miles,\nflowing continuously for eternity.",
        "long ban long lau maan leoi tou tou gong seoi wing bat jau",
        at_measure=7),
    Line("Rinse away the stories of the world\nThe strong currents that mix together\nIs it happiness or suffering?",
        "tou zeon liu sai gaan si wan zok tou tou jat pin ciu lau",
        at_measure=11),
    Line("It's tough to tell the difference between sadness and\nsuffering in the tides.",
        "si hei si sau long leoi fan bat cing fun siu bei jau",
        at_measure=15),
    Line("Success and defeat\nIt's difficult to see in the water",
        "sing gung sat baai long leoi hon bat ceot jau mei jau",
        at_measure=19),
    Line("Love you or hate you\nAsk you if you know\nLike great blissfulness, when it flows, it will not return.",
        "ngoi nei han nei man gwan zi fau ci daai gong jat faat bat sau",
        at_measure=23),
    Line("Flows through many banks of the seashore\nStill cannot cease this fray",
        "zyun cin waan zyun cin taan jik mei ping fuk ci zung zang dau",
        at_measure=27),
    Line("Both happiness and sorrow\nUnable to distinguish between the two",
        "jau jau hei jau jau sau zau syun fan bat cing fun siu bei jau",
        at_measure=31),
    Line("Still hoping to conquer this crashing wave\nMy heart is ready for these ups and downs.",
        "jing jyun faan baak cin long zoi ngo sam zung hei fuk gau",
        at_measure=35),
    Line("Love you or hate you\nAsk you if you know\nLike great blissfulness, when it flows, it will not return.",
        "ngoi nei han nei man gwan zi fau ci daai gong jat faat bat sau",
        at_measure=39),
    Line("Flows through many banks of the seashore\nStill cannot cease this fray",
        "zyun cin waan zyun cin taan jik mei ping fuk ci zung zang dau",
        at_measure=43),
    Line("Both happiness and sorrow\nUnable to distinguish between the two",
        "jau jau hei jau jau sau zau syun fan bat cing fun siu bei jau",
        at_measure=47),
    Line("Still hoping to conquer this crashing wave\nMy heart is ready for these ups and downs.",
        "jing jyun faan baak cin long zoi ngo sam zung hei fuk gau",
        at_measure=51),
    # repeats once more at 55, but no need to display that
], """
From: The Bund (TV series)
Music: Joseph Koo  
Arrangement: Cherie Chai
Translation from Cantonese:
https://lyricstranslate.com/en/shang-hai-tan-shanghai-beach.html
""", num_measures=60)