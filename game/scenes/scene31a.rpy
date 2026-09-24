label scene31a:
    # scene bg black
    scene bg research lab inside
    with dissolve
    # TODO compare genius TL to sheet music
    # https://genius.com/Genius-english-translations-hakushi-hasegawa-outside-soto-english-translation-lyrics
    # https://drive.google.com/drive/folders/1YfW1BESusTIj58PYCd7fJaNTQko4uopv
    call timed_lyrics(Character("Soto (Outside)"), LyricsTimer.parse(60*3 + 26, """
    0.01 Ga waratte inaito yoku iwa reta monoda | I was told many times, my smile didn't reach\nDidn't reach my eyes

    0.02 ā susukigiminowarui kodomodattadarou \\ ashi no ura o jimen kara hanasenakatta | Yeah, I'm sure I was a creepy child\nI couldn't lift the bottoms of my feet off the ground

    0.03 Soto ga daisukidakara soto ni detai noda \\ soto wa iro ga kawatte daisukida | I love the outdoors and want to go outside\nThe colors change outside and I love it

    0.04 Chōdo yoi yugami made ima wa kita yōda nomikuchi ni made haeta kuchibiru o miru to omou | The distortion is just right\nI think when I see lips around the bottle's throat

    0.05 Ā boku no susukigiminowarui kurōzetto ni wa teion no nai bakemono-tachi ya DJ ga iru | Yeah, in my creepy closet were\nMonsters without bass\nAnd DJs

    0.06 Soto ga daisukidakara soto ni detai noda soto wa totemo hirokute daisukida | I love the outdoors and want to go outside\nThe outdoors is so spacious and I love it

    0.07 Soto ga daisukidakara soto ni detai noda soto wa iro ga kawatte daisukida | I love the outdoors and want to go outside\nThe colors change outside and I love it

    0.08 Soto ga daisukida soto ni detai | I love the outdoors\nI want to go outside

    0.09 Soto ga daisukida soto ni detai soto wa iro ga kawatte daisukida | I love the outdoors\nI want to go outside\nThe colors change outside and I love it
    """))
    #title "Soto"
    #intro "I was told many times, my smile didn't reach\nDidn't reach my eyes\nYeah, I'm sure I was a creepy child\nI couldn't lift the bottoms of my feet off the ground"
    #chorus "I love the outdoors and want to go outside\nThe colors change outside and I love it"
    #verse1 "The distortion is just right\nI think when I see lips around the bottle's throat\n\nYeah, in my creepy closet were\nMonsters without bass\nAnd DJs"
    #prechorus "I love the outdoors and want to go outside\nThe outdoors is so spacious and I love it"
    #chorus "I love the outdoors and want to go outside\nThe colors change outside and I love it\nI love the outdoors\nI want to go outside\nI love the outdoors\nI want to go outside\nThe colors change outside and I love it"
    return