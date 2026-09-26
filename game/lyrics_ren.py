"""renpy

# Why not loop through all lines in one statement?
# Because renpy sets a checkpoint at each `call`, so we can roll back (mousewheel up) one line at a time.
# If it's one statement, mousewheel up resets the whole song.
label say_song_line(song, index, last=False):
    $ song.say(index, last=last)
    return

init -1 python:
"""
import dataclasses
import typing
import datetime

@dataclasses.dataclass(frozen=True)
class Line:
    subtitle: str
    lyric: str = ''
    at_seconds: float | None = None
    at_measure: int | None = None

    @property
    def lyric_oneline(self):
        return self.lyric.replace('\n', ' \\ ')

    @property
    def subtitle_oneline(self):
        return self.subtitle.replace('\n', ' \\ ')

@dataclasses.dataclass
class SongLine:
    song: 'Song'
    line: Line | None
    next: typing.Self | None = None

    @property
    def at(self) -> str:
        ats = []
        match (self.song.num_measures, self.line.at_measure):
            case (None, None):
                pass
            case (None, _):
                ats.append(f"m.{int(self.line.at_measure)}")
            case (_, None):
                ats.append(f"m.??? / m.{int(self.song.num_measures)}")
            case (_, _):
                ats.append(f"m.{int(self.line.at_measure)} / m.{int(self.song.num_measures)}")
        match (self.song.num_seconds, self.line.at_seconds):
            case (None, None):
                pass
            case (None, _):
                ats.append(str(datetime.timedelta(seconds=int(self.line.at_seconds)))[2:])
            case (_, None):
                ats.append(f"??:?? / {str(datetime.timedelta(seconds=int(self.song.num_seconds)))[2:]}")
            case (_, _):
                ats.append(f"{str(datetime.timedelta(seconds=int(self.line.at_seconds)))[2:]} / {str(datetime.timedelta(seconds=int(self.song.num_seconds)))[2:]}")
        try:
            n = self.song.lyrics.index(self) 
            # zero-index line numbers, even though they're for human viewing, because the first line is blank
            ats.append(f"L.{n} / {len(self.song.lyrics)-1}")
        except ValueError:
            # the last line's "next" won't be in the list of lyrics, that's fine, ignore it
            pass
        return ', '.join(a for a in ats if a is not None)

    @property
    def saytext(self) -> str:
        return self.line.subtitle

    @property
    def logtext(self) -> str:
        return f"""
### CURRENT LINE{' ' if self.at else ''}{self.at}
{self.line.lyric_oneline or '-'}
{self.line.subtitle_oneline or '-'}

### NEXT LINE{' ' if self.next.at else ''}{self.next.at}
{self.next.line.lyric_oneline or '-'}
{self.next.line.subtitle_oneline or '-'}"""


@dataclasses.dataclass
class Song:
    who: 'Character' # type: ignore
    raw_lyrics: list[Line]
    num_measures: int | None = None
    num_seconds: float | None = None

    @property
    def lyrics(self):
        cur = SongLine(self, Line('', '',
            at_measure=0 if self.num_measures is not None else None,
            at_seconds=0 if self.num_seconds is not None else None,
        ))
        ret = [cur]
        for l in self.raw_lyrics:
            next = SongLine(self, l)
            cur.next = next
            cur = next
            ret.append(cur)
        cur.next = SongLine(self, Line('', '', at_measure=self.num_measures, at_seconds=self.num_seconds))
        return ret

    def say(self, index, last=False):
        c = self.lyrics[index]
        print(c.logtext)
        renpy.say(who=c.song.who, what=c.saytext) # type: ignore
        if last and self.lyrics[index] != self.lyrics[-1]:
            raise ValueError(f'not the last lyric: {index}')