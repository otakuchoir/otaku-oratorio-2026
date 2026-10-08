label scene15a: 
    scene bg black with dissolve
    # https://genius.com/Keiichi-okabe-weight-of-the-world-english-ver-lyrics
    # https://drive.google.com/drive/folders/1eGwHAIeJT8nH7Ggvhry5DIf327qB5GDx
    call say_song_line(song_weight, 0)
    call say_song_line(song_weight, 1)
    call say_song_line(song_weight, 2)
    call say_song_line(song_weight, 3)
    call say_song_line(song_weight, 4)
    call say_song_line(song_weight, 5)
    call say_song_line(song_weight, 6)
    call say_song_line(song_weight, 7)
    call say_song_line(song_weight, 8)
    call say_song_line(song_weight, 9)
    call say_song_line(song_weight, 10)
    call say_song_line(song_weight, 11)
    call say_song_line(song_weight, 12)
    call say_song_line(song_weight, 13)
    call say_song_line(song_weight, 14)
    call say_song_line(song_weight, 15)
    call say_song_line(song_weight, 16)
    call say_song_line(song_weight, 17)
    call say_song_line(song_weight, 18)
    call say_song_line(song_weight, 19, last=True)
    return

define song_weight = Song(Character("Weight of the World"), [
    Line("I feel like I'm losing hope\nIn my body and my soul\nAnd the sky, it looks so ominous",
        at_measure=9),
    Line("And as time comes to a halt\nSilence starts to overflow\nMy cries are inconspicuous",
        at_measure=13),
    Line("Tell me God, are you punishing me?\nIs this the price I'm paying for my past mistakes?",
        at_measure=17),
    Line("This is my redemption song\nI need you more than ever right now\nCan you hear me now?",
        at_measure=21),
    Line("Cause we're gonna shout it loud\nEven if our words seem meaningless\nIt's like I'm carrying the weight of the world",
        at_measure=26),
    Line("I wish that someway, somehow\nThat I could save every one of us\nBut the truth is that I'm only one girl",
        at_measure=30),
    Line("Maybe if I keep believing\nMy dreams will come to life\nCome to life",
        at_measure=34),
    Line("After all the laughter fades\nSigns of life all washed away\nI can still, still feel a gentle breeze",
        "(Repeat from m.9, DS al Coda)",
        at_measure=9),
    Line("No matter how hard I pray,\nSigns of warning still remain\nAnd life has become my enemy",
        at_measure=13),
    Line("Tell me God, are you punishing me?\nIs this the price I'm paying for my past mistakes?",
        at_measure=17),
    Line("This is my redemption song\nI need you more than ever right now\nCan you hear me now?",
        at_measure=21),
    Line("Cause we're gonna shout it loud\nEven if our words seem meaningless\nIt's like I'm carrying the weight of the world",
        at_measure=26),
    Line("I wish that someway, somehow\nThat I could save every one of us\nBut the truth is that I'm only one girl",
        at_measure=30),
    Line("Maybe if I keep believing\nMy dreams will come to life\nCome to life",
        at_measure=34),
    Line("Cause we're gonna shout it loud\nEven if our words seem meaningless\nIt's like I'm carrying the weight of the world",
        "(Skip from m.36 to m.42, Coda)",
        at_measure=53),
    Line("I wish that someway, somehow\nThat I could save every one of us\nBut the truth is that I'm only one girl",
        at_measure=57),
    Line("Still, we're gonna shout it loud\nEven if our words seem meaningless\nIt's like I'm carrying the weight of the world",
        at_measure=61),
    Line("I hope that someway, somehow\nThat I could save every one of us\nBut the truth is that I'm only one girl",
        at_measure=65),
    Line("Maybe if I keep believing\nMy dreams will come to life\nCome to life",
        at_measure=69),
], """
From: Nier: Automata
Composer: Keiichi Okabe
Lyrics: Keiichi Okabe and J'Nique Nicole
Arrangement: Sophia Chan (NYC Otaku Choir)
""", num_measures=77)