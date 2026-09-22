label timer_test:
    "the timer has not yet started."
    "it will start after your next click."

    call timed_lyrics(Character("Some Example Song Lyrics"), LyricsTimer.parse(18, """
    1.0 the timer has started
    3.5 some song lyrics we're hearing...|translated lyrics the audience sees...
    6.0 some more song lyrics...
    8.5 even more song lyrics...
    12.0 almost done with the song...
    15.5 last lyric of the song
    """))
    #call start_timer(lyrics_ts)
    #lyrics_timer_test ""
    #$ lyrics_ts.say(who=lyrics_timer_test)
    #call clear_timer
    "the song is over"