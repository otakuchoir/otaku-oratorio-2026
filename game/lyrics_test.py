import unittest
from game.lyrics_ren import Song, Line

class LyricsTest(unittest.TestCase):
    def test_empty(self):
        song = Song(None, [])
        self.assertEqual(len(song.lyrics), 1)
        self.assertEqual(song.lyrics[0].saytext, "")
        self.assertEqual(song.lyrics[0].logtext, """
### CURRENT LINE L.0 / 0
-
-

### NEXT LINE
-
-""")

    def test_no_timing(self):
        song = Song(None, [
            Line('translated lyrics the audience SEES', 'native lyrics the audience HEARS'),
            Line('sub 2', 'lyric 2'),
            Line('sub 3'),
            Line('sub 4', 'lyric 4'),
        ])
        self.assertEqual(len(song.lyrics), 5)
        self.assertEqual(song.lyrics[0].saytext, "")
        self.assertEqual(song.lyrics[0].logtext, """
### CURRENT LINE L.0 / 4
-
-

### NEXT LINE L.1 / 4
native lyrics the audience HEARS
translated lyrics the audience SEES""")
        self.assertEqual(song.lyrics[1].saytext, "translated lyrics the audience SEES")
        self.assertEqual(song.lyrics[1].logtext, """
### CURRENT LINE L.1 / 4
native lyrics the audience HEARS
translated lyrics the audience SEES

### NEXT LINE L.2 / 4
lyric 2
sub 2""")
        self.assertEqual(song.lyrics[2].saytext, "sub 2")
        self.assertEqual(song.lyrics[2].logtext, """
### CURRENT LINE L.2 / 4
lyric 2
sub 2

### NEXT LINE L.3 / 4
-
sub 3""")
        self.assertEqual(song.lyrics[3].saytext, "sub 3")
        self.assertEqual(song.lyrics[3].logtext, """
### CURRENT LINE L.3 / 4
-
sub 3

### NEXT LINE L.4 / 4
lyric 4
sub 4""")
        self.assertEqual(song.lyrics[4].saytext, "sub 4")
        self.assertEqual(song.lyrics[4].logtext, """
### CURRENT LINE L.4 / 4
lyric 4
sub 4

### NEXT LINE
-
-""")

    def test_measures(self):
        song = Song(None, [
            Line('translated lyrics the audience SEES', 'native lyrics the audience HEARS', at_measure=4),
            Line('sub 2', 'lyric 2', at_measure=8),
            Line('sub 3'),
            Line('sub 4', 'lyric 4', at_measure=19),
        ], num_measures=22)
        self.assertEqual(len(song.lyrics), 5)
        self.assertEqual(song.lyrics[0].saytext, "")
        self.assertEqual(song.lyrics[0].logtext, """
### CURRENT LINE m.0 / m.22, L.0 / 4
-
-

### NEXT LINE m.4 / m.22, L.1 / 4
native lyrics the audience HEARS
translated lyrics the audience SEES""")
        self.assertEqual(song.lyrics[1].saytext, "translated lyrics the audience SEES")
        self.assertEqual(song.lyrics[1].logtext, """
### CURRENT LINE m.4 / m.22, L.1 / 4
native lyrics the audience HEARS
translated lyrics the audience SEES

### NEXT LINE m.8 / m.22, L.2 / 4
lyric 2
sub 2""")
        self.assertEqual(song.lyrics[2].saytext, "sub 2")
        self.assertEqual(song.lyrics[2].logtext, """
### CURRENT LINE m.8 / m.22, L.2 / 4
lyric 2
sub 2

### NEXT LINE m.??? / m.22, L.3 / 4
-
sub 3""")
        self.assertEqual(song.lyrics[3].saytext, "sub 3")
        self.assertEqual(song.lyrics[3].logtext, """
### CURRENT LINE m.??? / m.22, L.3 / 4
-
sub 3

### NEXT LINE m.19 / m.22, L.4 / 4
lyric 4
sub 4""")
        self.assertEqual(song.lyrics[4].saytext, "sub 4")
        self.assertEqual(song.lyrics[4].logtext, """
### CURRENT LINE m.19 / m.22, L.4 / 4
lyric 4
sub 4

### NEXT LINE m.22 / m.22
-
-""")