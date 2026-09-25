define lyric_test_song = Song(Character("Timer Test Song"), [
    Line("some english lyrics", "nihongo uta"),
    Line("2 english lyrics", "2 nihongo uta"),
    Line("3 english lyrics", "3 nihongo uta"),
])
label lyric_test:
    "the song has not yet started."
    "it will start after your next click."

    # Why not do this all in one statement?
    # Because renpy sets a checkpoint at each `call`, so we can roll back (mousewheel up) one line at a time.
    # If it's one statement, mousewheel up resets the whole song.
    call say_song_line(timer_test_song, 0)
    call say_song_line(timer_test_song, 1)
    call say_song_line(timer_test_song, 2)
    call say_song_line(timer_test_song, 3, last=True)

    "the song is over"