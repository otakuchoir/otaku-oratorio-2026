define lyrics_destati = Character("Destati (Awaken)")
label scene34a: 
    scene bg black hole with dissolve
    # https://genius.com/Yoko-shimomura-destati-lyrics
    # https://www.khwiki.com/Destati#Lyrics
    # https://drive.google.com/drive/folders/1qbuS0UvviJtcyFygsFuIUzoqoiPrXxqs
    #nvl clear
    call timed_lyrics(Character("Destati (Awaken)"), LyricsTimer.parse(60*3 + 32, """
    0.01 Destati!\nTendi la mano! | Awaken!\nHold out your hand!

    0.02 È giunta l'ora,\nDestati | The time has come,\nAwaken

    0.03 Le porte verranno schiuse\nDestati, Destati, Destati | The doors will be parted\nAwaken, Awaken, Awaken

    0.04 Su rimembra tu trepida!\nSu sveglia! Ehi ricorda! | Come on, remember, you who tremble!\nCome on, wake up! Oh, remember!

    0.05 Destati! Destati!\nForza, tendi la mano! | Awaken! Awaken!\nCome on, hold out your hand!

    0.06 Destati! Destati!\nÈ giunta l'ora! | Awaken! Awaken!\nThe time has come!

    0.07 E ancora una volta\nApriranno le porte! | And once again\nThey will open the doors!

    0.08 Su rimembra tu trepida!\nSu sveglia! Ehi ricorda! | Come on, remember, you who tremble!\nCome on, wake up! Oh, remember!

    0.09 Eh? Come? Non lo vuoi!?\nTuttavia t'appartiene | Eh? What? You do not want it!?\nStill it belongs to you

    0.10 Ciò che hai perduto\nDiventerà uno solo! | What you have lost\nWill become one!
    """))
    #title "Destati (Awaken)"
    #lyrics "Awaken!\nHold out your hand!"
    #lyrics "The time has come,\nAwaken\nThe doors will be parted\nAwaken, Awaken, Awaken"
    #lyrics "Come on, remember, you who tremble!\nCome on, wake up! Oh, remember!"
    #lyrics "Awaken! Awaken!\nCome on, hold out your hand!\nAwaken! Awaken!\nThe time has come!"
    #nvl clear
    #lyrics "And once again\nThey will open the doors!"
    #lyrics "Come on, remember, you who tremble!\nCome on, wake up! Oh, remember!"
    #lyrics "Eh? What? You do not want it!?\nStill it belongs to you\nWhat you have lost\nWill become one!"
    return