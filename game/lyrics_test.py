import unittest
from game.lyrics_ren import Song, Line

class LyricsTest(unittest.TestCase):
    def test_empty(self):
        song = Song(None, [])
        self.assertEqual(len(song.lyrics), 1)
        self.assertEqual(song.lyrics[0].saytext, "")
        self.assertEqual(song.lyrics[0].logtext, """
### CURRENT LINE
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
### CURRENT LINE
-
-

### NEXT LINE
native lyrics the audience HEARS
translated lyrics the audience SEES""")
        self.assertEqual(song.lyrics[1].saytext, "translated lyrics the audience SEES")
        self.assertEqual(song.lyrics[1].logtext, """
### CURRENT LINE
native lyrics the audience HEARS
translated lyrics the audience SEES

### NEXT LINE
lyric 2
sub 2""")
        self.assertEqual(song.lyrics[2].saytext, "sub 2")
        self.assertEqual(song.lyrics[2].logtext, """
### CURRENT LINE
lyric 2
sub 2

### NEXT LINE
-
sub 3""")
        self.assertEqual(song.lyrics[3].saytext, "sub 3")
        self.assertEqual(song.lyrics[3].logtext, """
### CURRENT LINE
-
sub 3

### NEXT LINE
lyric 4
sub 4""")
        self.assertEqual(song.lyrics[4].saytext, "sub 4")
        self.assertEqual(song.lyrics[4].logtext, """
### CURRENT LINE
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
### CURRENT LINE m.0 / m.22
-
-

### NEXT LINE m.4 / m.22
native lyrics the audience HEARS
translated lyrics the audience SEES""")
        self.assertEqual(song.lyrics[1].saytext, "translated lyrics the audience SEES")
        self.assertEqual(song.lyrics[1].logtext, """
### CURRENT LINE m.4 / m.22
native lyrics the audience HEARS
translated lyrics the audience SEES

### NEXT LINE m.8 / m.22
lyric 2
sub 2""")
        self.assertEqual(song.lyrics[2].saytext, "sub 2")
        self.assertEqual(song.lyrics[2].logtext, """
### CURRENT LINE m.8 / m.22
lyric 2
sub 2

### NEXT LINE m.??? / m.22
-
sub 3""")
        self.assertEqual(song.lyrics[3].saytext, "sub 3")
        self.assertEqual(song.lyrics[3].logtext, """
### CURRENT LINE m.??? / m.22
-
sub 3

### NEXT LINE m.19 / m.22
lyric 4
sub 4""")
        self.assertEqual(song.lyrics[4].saytext, "sub 4")
        self.assertEqual(song.lyrics[4].logtext, """
### CURRENT LINE m.19 / m.22
lyric 4
sub 4

### NEXT LINE m.22 / m.22
-
-""")