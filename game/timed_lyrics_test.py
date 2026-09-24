import unittest
from game import timed_lyrics_ren

class TimedLyricsTest(unittest.TestCase):
    def test_parse_empty(self):
        with self.assertRaises(ValueError) as e:
            timed_lyrics_ren.LyricsTimer.parse(18, "")
        self.assertEqual(e.exception.args[0], 'empty lyrics')

    def test_parse(self):
        lt = timed_lyrics_ren.LyricsTimer.parse(18, """
        1.0 the timer has started

        3.5 some song lyrics we're hearing...|translated lyrics the audience sees...

        6.0 some more song lyrics...

        8.5 even more song lyrics...

        12.0 almost done with the song...

        15.5 last lyric of the song
        """)
        self.assertEqual(len(lt.lyrics), 7)
        self.assertEqual(lt.lyrics[0].lyric, "")
        self.assertEqual(lt.lyrics[0].subtitle, "")
        self.assertEqual(str(lt.lyrics[0]), """
### CURRENT LINE - 00:00 / 00:18 ( 0%)
-


### NEXT LINE - IN 00:01
-
the timer has started""")
        self.assertEqual(lt.lyrics[1].lyric, None)
        self.assertEqual(lt.lyrics[1].subtitle, "the timer has started")
        self.assertEqual(str(lt.lyrics[1]), """
### CURRENT LINE - 00:01 / 00:18 ( 6%)
-
the timer has started

### NEXT LINE - IN 00:02
some song lyrics we're hearing...
translated lyrics the audience sees...""")
        self.assertEqual(lt.lyrics[2].lyric, "some song lyrics we're hearing...")
        self.assertEqual(lt.lyrics[2].subtitle, "translated lyrics the audience sees...")