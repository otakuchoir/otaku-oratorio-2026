"""renpy

label timed_lyrics(who, lt):
    call start_timer(lt)
    call fx.log("\n\nChoir song starting. Lyrics are shown here to help the VN operator, but their timing may be wrong. Listen to the choir!\n\n\n\n\n\n\n")
    $ lt.say(who=who)
    call clear_timer
    return

label start_timer(t):
    # $ timer_st = Timer(t)
    $ timer_st = t
    show screen timer_bg
    return

label clear_timer:
    hide screen timer_bg
    $ timer_st = None
    return

screen timer_bg():
    timer 0.1 repeat True action Function(timer_st.tick)

init -1 python:
"""
import dataclasses
import datetime
import time
import typing

@dataclasses.dataclass
class Timer:
    end_seconds: float
    start_at: float = dataclasses.field(default_factory=time.time)
    now: float = dataclasses.field(default_factory=time.time)

    def tick(self):
        self.now = time.time()
    
    @property
    def end_at(self) -> float:
        return self.start_at + self.end_seconds

    @property
    def elapsed_seconds(self) -> float:
        return min(self.end_seconds, self.now - self.start_at)

    def elapsed_percent(self, elapsed_seconds: float = None) -> float:
        return max(0.0, min(1.0, float(int(elapsed_seconds if elapsed_seconds is not None else self.elapsed_seconds)) / self.end_seconds))
        
    @property
    def elapsed_td(self) -> datetime.timedelta:
        return datetime.timedelta(seconds=int(self.elapsed_seconds))

    @property
    def end_td(self) -> datetime.timedelta:
        return datetime.timedelta(seconds=int(self.end_seconds))

    def render(self, elapsed_seconds=None):
        elapsed_td = datetime.timedelta(seconds=int(elapsed_seconds)) if elapsed_seconds is not None else self.elapsed_td
        return f"{str(elapsed_td)[2:]} / {str(self.end_td)[2:]} ({self.elapsed_percent(elapsed_seconds):3,.0%})"
    
    def __str__(self):
        return self.render()

@dataclasses.dataclass
class LyricsLine:
    timestamp: float
    lyric: str | None
    subtitle: str
    timer: Timer
    next: typing.Self | None = None

    @staticmethod
    def parse(s: str, t: Timer) -> "LyricsLine":
        """
        format: `timestamp sound[|subtitles]`

        example line:
        23.4 baka mitai | I've been a fool

        example with no native lyrics:
        23.4 I've been a fool
        """
        dur, l = s.split(None, 1)
        try:
            lyric, subtitle = l.split('|', 1)
        except ValueError:
            lyric, subtitle = None, l
        return LyricsLine(float(dur), lyric.strip() if lyric else lyric, subtitle.strip(), t)

    @property
    def next_or_empty(self):
        return self.next if self.next else LyricsLine(timestamp=self.timestamp, lyric='', subtitle='', timer=self.timer)

    @property
    def lyric_firstline(self):
        return self.lyric.split('\n')[0] if self.lyric else None

    @property
    def subtitle_firstline(self):
        return self.subtitle.split('\n')[0]

    def render(self, next_line_in=None) -> str:
        next_line_in = next_line_in if next_line_in else datetime.timedelta(seconds=int(self.next_or_empty.timestamp - self.timestamp))
        return f"""
### CURRENT LINE - {self.timer.render(elapsed_seconds=self.timestamp)}
{self.lyric_firstline or '-'}
{self.subtitle_firstline}

### NEXT LINE - IN {str(next_line_in)[2:]}
{self.next_or_empty.lyric_firstline or '-'}
{self.next_or_empty.subtitle_firstline}"""

    def __lt__(self, other: typing.Self) -> bool:
        return self.timestamp < other.timestamp

    def __str__(self):
        return self.render()

@dataclasses.dataclass
class LyricsTimer:
    timer: Timer
    lyrics: list[LyricsLine]

    @staticmethod
    def parse(dur: float, s: str) -> "LyricsTimer":
        t = Timer(float(dur))
        if not len(s.strip()):
            raise ValueError('empty lyrics')
        ls = [LyricsLine.parse(l, t) for l in s.strip().split("\n")]

        n = None
        for l in reversed(ls):
            l.next = n
            n = l
        ls = [LyricsLine(timestamp=0.0, lyric='', subtitle='', next=ls[0], timer=t)] + ls
        sort = sorted(ls)
        if (str(ls) != str(sort)):
            raise ValueError('timed lyrics must be in order')
        if dur < ls[-1].timestamp:
            raise ValueError(f"song duration ({dur}) is less than last lyric's timestamp ({ls[-1].timestamp})")
        return LyricsTimer(t, ls)

    def say(self, who) -> None:
        for l in self.lyrics:
            print(l)
            renpy.say(who=who, what=l.subtitle) # type: ignore

    def tick(self):
        self.timer.tick()