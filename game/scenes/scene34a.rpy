label scene34a: 
    scene bg black hole with dissolve
    # https://genius.com/Yoko-shimomura-destati-lyrics
    # https://www.khwiki.com/Destati#Lyrics
    # https://drive.google.com/drive/folders/1qbuS0UvviJtcyFygsFuIUzoqoiPrXxqs
    call say_song_line(song_destati, 0)
    call say_song_line(song_destati, 1)
    call say_song_line(song_destati, 2)
    call say_song_line(song_destati, 3)
    call say_song_line(song_destati, 4)
    call say_song_line(song_destati, 5)
    call say_song_line(song_destati, 6)
    call say_song_line(song_destati, 7)
    call say_song_line(song_destati, 8)
    call say_song_line(song_destati, 9)
    call say_song_line(song_destati, 10)
    call say_song_line(song_destati, 11)
    call say_song_line(song_destati, 12)
    call say_song_line(song_destati, 13)
    call say_song_line(song_destati, 14)
    call say_song_line(song_destati, 15)
    call say_song_line(song_destati, 16, last=True)
    return

define song_destati = Song(Character("Destati (Awaken)"), [
    Line("Awaken!\nHold out your hand!",
        "Destati!\nTendi la mano!",
        at_measure=1),
    Line("The time has come,\nAwaken",
        "È giunta l'ora,\nDestati",
        at_measure=11),
    Line("The doors will be parted\nAwaken, Awaken, Awaken",
        "Le porte verranno schiuse\nDestati, Destati, Destati",
        at_measure=15),
    Line("The closer you get to the light,\nthe greater your shadow becomes",
        "Piu ti avvicini alla luce,\npiu grande diventa la tua ombra",
        at_measure=21),
    Line("", "", at_measure=29),
    Line("Awaken! Awaken!\nThe time has come!",
        "Destati! Destati!\nÈ giunta l'ora!",
        at_measure=37),
    Line("Awaken! Awaken!\nCome on, hold out your hand!",
        "Destati! Destati!\nForza, tendi la mano!",
        at_measure=41),
    Line("Come on, remember, you who tremble!\nCome on, wake up! Oh, remember!",
        "Su rimembra tu trepida!\nSu sveglia! Ehi ricorda!",
        at_measure=45),
    Line("Awaken! Awaken!\nThe time has come!",
        "Destati! Destati!\nÈ giunta l'ora!",
        at_measure=53),
    Line("And once again\nThey will open the doors!",
        "E ancora una volta\nApriranno le porte!",
        at_measure=57),
    Line("Come on, remember, you who tremble!\nCome on, wake up! Oh, remember!",
        "Su rimembra tu trepida!\nSu sveglia! Ehi ricorda!",
        at_measure=69),
    Line("Eh? What? You do not want it!?\nStill it belongs to you",
        "Eh? Come? Non lo vuoi!?\nTuttavia t'appartiene",
        at_measure=73),
    Line("What you have lost\nWill become one!",
        "Ciò che hai perduto\nDiventerà uno solo!",
        at_measure=77),
    Line("But don't be afraid, and don't forget",
        "Ma non aver paura, e non dimenticare",
        at_measure=81),
    Line("Eh? What? You do not want it!?\nStill it belongs to you",
        "Eh? Come? Non lo vuoi!?\nTuttavia t'appartiene",
        at_measure=89),
    Line("What you have lost\nWill become one!",
        "Ciò che hai perduto\nDiventerà uno solo!",
        at_measure=93),
], num_measures=101)