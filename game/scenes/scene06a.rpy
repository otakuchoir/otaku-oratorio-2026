label scene06a: 
    # https://drive.google.com/drive/folders/1rzd3U-TLuvn0hA2ehIClc1PZsiZVG7Oi
    # https://docs.google.com/document/d/1U2KybQi7-4mGWfG76CV5oPHkHJchMrdLj2ARfhD664k/edit?tab=t.0
    # https://genius.com/Ryokuoushoku-shakai-be-a-flower-lyrics
    # https://genius.com/Genius-english-translations-ryokuoushoku-shakai-be-a-flower-english-translation-lyrics
    # https://genius.com/Genius-romanizations-ryokuoushoku-shakai-be-a-flower-romanized-lyrics
    scene bg train station
    with dissolve
    call say_song_line(song_hana, 0)
    call say_song_line(song_hana, 1)
    call say_song_line(song_hana, 2)
    call say_song_line(song_hana, 3)
    call say_song_line(song_hana, 4)
    call say_song_line(song_hana, 5)
    call say_song_line(song_hana, 6)
    call say_song_line(song_hana, 7)
    call say_song_line(song_hana, 8)
    call say_song_line(song_hana, 9)
    call say_song_line(song_hana, 10)
    call say_song_line(song_hana, 11)
    call say_song_line(song_hana, 12)
    call say_song_line(song_hana, 13)
    call say_song_line(song_hana, 14)
    call say_song_line(song_hana, 15)
    call say_song_line(song_hana, 16, last=True)
    return

define song_hana = Song(Character("Hana ni Natte (Like a Flower)"), [
    Line("Isn’t it fine to hide quietly in the shadows?\nAren’t there flowers that are more like buds?",
        "Kage ni sotto kakureyou ga iin janai?\nTsubomi no you na hana datte an janai?",
        at_measure=13),
    Line("Isn’t it fine to protect in secret?\nUndisturbed by anyone, you bloom magnificently",
        "Himitsu ni shite mamoru no ga iin janai? Dare ni mo jama sarezu karei ni saiteru",
        at_measure=21),
    Line("You don’t get hooked on either sweetness or bitterness\nThat sort of decision-making is worthless",
        "Amai nigai ni hamannai\nSono handan ga kudannai",
        at_measure=29),
    Line("Don't let anything worry you, keep your head up\nNot used to love, not adorned excessively",
        "Ki ni yande shita wo mukanaide ite\nAi ni narechainai muda ni kazaranai",
        at_measure=33),
    Line("Don’t need a pretty vase, fertilizer, or anything\nYou’re beautiful just like that",
        "Kirei ni sareta kabin mo koyashi mo nanimo iranai\nSono sugata ga utsukushii",
        at_measure=41),
    Line("Be a flower, come on, smile wryly for me\nI get chills from the look on your face, I can’t look away",
        "Hana ni natte hora nihiru ni waratte\nSono kao ni zokuzoku shite me ga hanasenai",
        at_measure=48),
    Line("Have a taste - your poison is my medicine\nI’ll wrap you up nicely, so smile",
        "Ajimi shite kimi no doku wa watashi no kusuri tte\nTsutsunde ageru kara waratte",
        at_measure=56),
    Line("“Hey, I miss you”\n“I miss that smile of yours”\nIf I said that, would you smile for me?",
        "\"Nee aitai, aitai\"\n\"Sono egao ni aitai, aitai\"\nTte ieba waratte kureru ka na?",
        at_measure=69),
    Line("Isn’t it fine to just support from the shadows?\nSelfishly, I want to prove that I can make you bloom with my own hands",
        "Kage kara sasaeru kurai wa iin janai?\nYoku wo ieba kono te de sakasete misetai",
        at_measure=77),
    Line("You’re a flower that devours hearts like a disease\nAnd I don’t want to let you wither away",
        "Yamai no you ni kokoro wo kurau hana\nKarashitakunai no sa",
        at_measure=85),
    Line("Even if the light doesn’t reach you\nI’ll keep watering",
        "Hikari ga todokazu tomo\nMizu wo age tsuzukeru kara",
        at_measure=95),
    Line("Hurry up and realize it already - you’re wonderful\nBe proud and take better care of yourself",
        "Ii kagen ni kizuite kimi wa suteki ttе\nUnuborete motto odaiji ni",
        at_measure=105),
    Line("Obliviously accumulating love\nDon’t need a pretty vase, fertilizer, or anything\nJust like that, bloom in full glory",
        "Mujikaku na manma ai wo takuwaetе\nKirei ni sareta kabin mo koyashi mo nanimo iranai\nSono sugata de sakihokore",
        at_measure=113),
    Line("Be a flower, come on, smile wryly for me\nI get chills from the look on your face, I can’t look away",
        "Hana ni natte hora nihiru ni waratte\nSono kao ni zokuzoku shite me ga hanasenai",
        at_measure=126),
    Line("Have a taste - your poison is my medicine\nI’ll wrap you up nicely",
        "Ajimi shite kimi no doku wa watashi no kusuri tte\nTsutsunde ageru kara",
        at_measure=134),
    Line("Take it easy - your darkness is my light\nI’ll give you love, so smile",
        "Raku ni shite kimi no yami wa watashi no hikari tte\nAishite ageru kara waratte",
        at_measure=142),
], num_measures=157)