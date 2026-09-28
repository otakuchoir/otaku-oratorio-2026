# https://otaku-oratorio-2026-gallery.netlify.app/?t=usagi+postgrad&t=child&t=jojo&t=bart
label scene23a:
    # https://genius.com/Genius-romanizations-kana-boon-silhouette-romanized-lyrics
    # https://drive.google.com/drive/folders/1ChKUs_r4ykOjx3c8W4vzouFeMiTZoKYQ
    scene bg research lab inside with dissolve

    call say_song_line(song_silhouette, 0)
    call say_song_line(song_silhouette, 1)
    call say_song_line(song_silhouette, 2)
    call say_song_line(song_silhouette, 3)
    call say_song_line(song_silhouette, 4)
    call say_song_line(song_silhouette, 5)
    call say_song_line(song_silhouette, 6)
    call say_song_line(song_silhouette, 7)
    call say_song_line(song_silhouette, 8)
    call say_song_line(song_silhouette, 9)
    call say_song_line(song_silhouette, 10)
    call say_song_line(song_silhouette, 11)
    call say_song_line(song_silhouette, 12)
    call say_song_line(song_silhouette, 13)
    call say_song_line(song_silhouette, 14)
    call say_song_line(song_silhouette, 15)
    call say_song_line(song_silhouette, 16)
    call say_song_line(song_silhouette, 17)
    call say_song_line(song_silhouette, 18, last=True)
    return

define song_silhouette = Song(Character("Silhouette"), [
    Line("Altogether now, make a break for the goal line\nWe don't know anything, anything yet",
        "Isse no se de fumikomu goorain bokura wa\nNanimo nanimo mada shiranu",
        at_measure=17),
    Line("We passed the point of no return, but looking back\nWe don't know anything, anything yet",
        "Issen koete furikaeruto mou nai bokura wa\nNanimo nanimo mada shiranu",
        at_measure=25),
    Line("Fired up, fired up, get fired up\nBursting with glistening sweat",
        "Udatte udatte udatteku\nKirameku ase ga koboreru no sa",
        at_measure=33),
    Line("There are probably a lot of things we don't remember\nEveryone, even him, becoming mere silhouettes",
        "Oboetenai koto mo takusan attadarou\nDaremo kare mo shiruetto",
        at_measure=41),
    Line("We've pretended to forget the things we held dear\nSo we can just laugh and say it's nothing",
        "Daiji ni shitetta mono\nWasureta furi o shitanda yo\nNanimo nani yo waraerusa",
        at_measure=49),
    Line("As we count together, we all remember:\nWe wanted to have it all",
        "Isse no de, omoidasu shounen\nBokura wa nanimo kamo wo hoshigatta",
        at_measure=59),
    Line("I know (ahh), I've noticed\nThe hands-on the clock\nThese days can't be stopped",
        "Wakatteru tte, aa kizuiteru tte\nTokei no hari wa hibi wa tomaranai",
        at_measure=67),
    Line("Fighting, fighting, fighting for ownership\nTime and memories flow\nGetting further, further, further away",
        "Ubatte ubatte ubatteku\nNagareru toki to kioku\nTooku tooku tooku ni natte",
        at_measure=75),
    Line("There are probably a lot of things we don't remember\nEveryone, even him, becoming mere silhouettes",
        "Oboetenai koto mo takusan attadarou\nDaremo kare mo shiruetto",
        at_measure=83),
    Line("Everything we've worried about, we've tried to sweep under the carpet\nSo we can just laugh and say it’s nothing",
        "Osorete yamanu koto\nShiranai furi wo shitanda yo\nNanimo nani yo, waraeru sa",
        at_measure=91),
    Line("", "", at_measure=99),
    Line("Lightly, nimbly, they dance…\nJust like those leaves, having a singular purpose\nI want to proceed without impatience",
        "Hirari to hirari to matteru\nKonoha no you ni yureru koto naku\nShousou naku sugoshiteitai yo",
        at_measure=107),
    Line("There are probably a lot of things we don't remember\nBut there are also things that will never change,",
        "Oboetenai koto mo takusan atta kedo\nKitto zutto kawaranai mono ga aru koto o",
        at_measure=117),
    Line("And you who taught me this\nAre a fading, fading silhouette",
        "Oshiete kureta anata wa\nKieru kieru shiruetto",
        at_measure=127),
    Line("Clutching the things we wish to hold dear\nWe'll become more mature, never letting them wander",
        "Daiji ni shitai mono motte otona ni naru nda\nDonna toki mo hanasazu ni",
        at_measure=133),
    Line("Protecting them at all times\nThen someday, we'll be able to laugh about it all",
        "Mamori tsuzukeyou\nSoshitara itsu no hi ni ka\nNanimo kamo wo waraerusa",
        at_measure=141),
    Line("Lightly, nimbly, they dance\nThose leaves fly into the distance",
        "Hirari to hirari to matteru\nKonoha ga tonde yuku",
        at_measure=149),
    Line("", "", at_measure=155),
], """
From: Naruto: Shippuden
Music by: KANA-BOON
Arrangement by: Ko Tanaka (NYC Otaku Choir)
Translation from Japanese:
https://genius.com/Kana-boon-silhouette-lyrics
""", num_measures=174)