label scene02a: 
    # https://drive.google.com/drive/folders/13OOlvv-BOTt1b4r9VxmytgVwE475gNtl
    # https://animelyricsaz.com/artist/masaaki-endou/fumetsu-no-hero-seajetter-kaito/971-39227
    # https://www.uta-net.com/song/320519/
    # finally, one where I can't find an english translation! not thrilled about using machine translation, but no other options
    # translation credit: https://translate.google.com , based on https://animelyricsaz.com/artist/masaaki-endou/fumetsu-no-hero-seajetter-kaito/971-39227
    scene bg scene02 08 with dissolve
    call say_song_line(song_fumetsu, 0)
    call say_song_line(song_fumetsu, 1)
    call say_song_line(song_fumetsu, 2)
    call say_song_line(song_fumetsu, 3)
    call say_song_line(song_fumetsu, 4)
    call say_song_line(song_fumetsu, 5)
    call say_song_line(song_fumetsu, 6)
    call say_song_line(song_fumetsu, 7)
    call say_song_line(song_fumetsu, 8)
    call say_song_line(song_fumetsu, 9)
    call say_song_line(song_fumetsu, 10)
    call say_song_line(song_fumetsu, 11)
    call say_song_line(song_fumetsu, 12)

    show bg scene02 08 with Dissolve(0.25)
    show bg scene02 09 with Dissolve(0.25)
    kitadani "LET’S GO! CROWN BLASTER!"

    # > THE MONSTER DOES NOT FLINCH.
    show bg scene02 10 with Dissolve(0.25)
    with vpunch
    pause 1.5
    show bg scene02 11 with Dissolve(0.25)
    pause 1.5
    show bg scene02 12 with Dissolve(0.25)
    monster "Your precious Earth is mine to devour!"

    window hide
    window auto
    show bg scene02 13 with Dissolve(0.25)
    pause 1.0
    show bg scene02 14 with Dissolve(0.25)
    pause 2.0
    show bg scene02 15 with Dissolve(0.25)
    kitadani "DAMN!"

    window hide
    window auto
    show bg scene02 16 with Dissolve(0.25)
    pause 2.0
    show bg scene02 17 with Dissolve(0.25)
    computer "Ultima Cannon ready to dispense justice. Survival rate… 1%%."

    window hide
    window auto
    show bg scene02 18 with Dissolve(0.25)
    pause 1.5
    show bg scene02 19 with Dissolve(0.25)
    pause 2.0
    show bg scene02 20 with Dissolve(0.25)
    pause 2.0
    show bg scene02 21 with Dissolve(0.25)
    # > KITADANI GLANCES AT THE FAMILY PHOTO ON HIS DASHBOARD
    ### page 3 ###
    kitadani "This is the only way. Justice requires swift action."
    show bg scene02 22 with Dissolve(0.25)
    kitadani "Citizens of Earth: Lend me your strength! For every human, on this beautiful Earth!"
    show bg scene02 23 with Dissolve(0.25)
    monster "WHAT!?"

    window hide
    window auto
    # > Monster reels back to charge it’s atomic breath
    show bg scene02 24 with Dissolve(0.25)
    pause 2.0
    show bg scene02 25 with Dissolve(0.25)
    kitadani "Ultima Cannon: {b}FIRE!{/b}"

    call say_song_line(song_fumetsu, 13)
    call say_song_line(song_fumetsu, 14)
    call say_song_line(song_fumetsu, 15)
    call say_song_line(song_fumetsu, 16, last=True)
    return

define song_fumetsu = Song(Character("Fumetsu no Hero (Immortal Hero)"), [
    Line("You’ve wandered into the darkness,\nBut I’m coming to save you right now.",
        "Kurayami no naka mayoikonderu\nKimi wo sukui ni yuku yo ima sugu",
        at_measure=11),
    Line("So don’t cry—just wait for me;\nYou are never alone, no matter what.\nDon’t give up; don’t let yourself be defeated.",
        "Dakara nakanaide matte ite yo\nKimi wa hitori ja nai donna toki demo\nAkiramenaide makenaide ite",
        at_measure=19),
    Line("FIGHT once more! TRY again and again!\nSoar HIGH, aiming for the light!\nTurn your tears into strength.",
        "Mou ichido FIGHT!! Nando mo TRY!!\nHikari wo mezashite habatake HIGH!!\nNamida wo tsuyosa ni kaete",
        at_measure=31),
    Line("SEAJETTER KAITO! (KAITO!) Rise above the sorrow,\nAnd let’s reclaim that radiance together.",
        "SEAJETTER KAITO! (KAITO!) Kanashimi koete\nKagayaki wo mata torimodosou issho ni",
        at_measure=38),
    Line("SEAJETTER KAITO! (KAITO!) Even the pain—\nLet’s turn it into power, embracing our overflowing hope.",
        "SEAJETTER KAITO! (KAITO!) Kurushimi sae mo\nChikara ni kaete yukou afureru kibou dakishimete",
        at_measure=46),
    Line("K.A.I.T.O.—rise up!\nSEAJETTER... SEAJETTER KAITO!",
        "K.A.I.T.O tachiagare!\nSEAJETTER... SEAJETTER KAITO!",
        at_measure=55),
    Line("The sun rising over the horizon\nKeeps illuminating our future.",
        "Suiheisen ni noboru taiyou\nBokura no mirai terashi tsuzukeru",
        at_measure=66),
    Line("The bonds we share turn into courage,\nEtching the proof of our lives in our beating hearts.\nI’ll never forget the friendship we share.",
        "Tsunaida kizuna wa yuuki ni nari\nIkiru akashi kizamu furueru mune ni\nWasure wa shinai kimi to no yuujou",
        at_measure=74),
    Line("FIGHT anytime! TRY anywhere!\nSoar high to protect the ones we love!\nPass on the smiles toward tomorrow.",
        "Itsu demo FIGHT!! Doko demo TRY!!\nAisuru mono wo mamoru tame High!!\nHohoemi tsunage ashita he",
        at_measure=86),
    Line("SEAJETTER KAITO! (KAITO!) Let’s create a future\nFilled with smiles, starting right here, right now.",
        "SEAJETTER KAITO! (KAITO!) Egao afureru\nMirai ni kaeru bokura no te de koko kara",
        at_measure=93),
    Line("SEAJETTER KAITO! (KAITO!) No matter the moment,\nLook forward and move ahead—don’t give up on your dreams.",
        "SEAJETTER KAITO! (KAITO!) donna toki demo\nMae wo muite susumou yume wo akiramenaide ite",
        at_measure=101),
    Line("K.A.I.T.O.—believe!\nSEAJETTER... SEAJETTER KAITO!",
        "K.A.I.T.O shinjiyou!\nSEAJETTER... SEAJETTER KAITO!",
        at_measure=110),
    Line("FIGHT once more! TRY again and again!\nSoar HIGH, aiming for the light!\nTurn your tears into strength.",
        "(31 m. of dialogue, ending with \"Ultima Cannon: FIRE!\", then...) Mou ichido FIGHT!! Nando mo TRY!!\nHikari wo mezashite habatake HIGH!!\nNamida wo tsuyosa ni kaete",
        at_measure=141),
    Line("SEAJETTER KAITO! (KAITO!) Rising above the sorrow,\nLet's reclaim our radiance together—",
        "SEAJETTER KAITO! (KAITO!) Kanashimi koete\nKagayaki wo mata torimodosou issho ni",
        at_measure=148),
    Line("SEAJETTER KAITO! (KAITO!) Even the pain\nWe'll turn into strength, embracing hope that overflows—",
        "SEAJETTER KAITO! (KAITO!) Kurushimi sae mo\nChikara ni kaete yukou afureru kibou dakishimete",
        at_measure=156),
    Line("K.A.I.T.O, rise up!\nSEAJETTER... SEAJETTER KAITO!",
        "K.A.I.T.O tachiagare!\nSEAJETTER... SEAJETTER KAITO!",
        at_measure=165),
], """
From: SeaJetter KAITO
Music, Lyrics: Masaaki Endo
Original Arrangement: Kenji Yamamoto
Arrangement: Ko Tanaka (NYC Otaku Choir)
Translation from Japanese: Google Translate
""", num_measures=181)