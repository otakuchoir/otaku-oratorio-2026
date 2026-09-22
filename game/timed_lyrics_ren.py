"""renpy

label timed_lyrics(who, lt, first_line=""):
    call start_timer(lt)
    call fx.log("\n\nChoir song starting. Lyrics are shown here to help the VN operator, but their timing may be wrong. Listen to the choir!\n\n\n\n\n\n\n")
    # $ renpy.say(who=who, what=first_line)
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
CURSOR_UP = """\033[F"""
CLEAR_LINE = """\033[K"""

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

    @property
    def elapsed_percent(self) -> float:
        return max(0.0, min(1.0, float(int(self.elapsed_seconds)) / self.end_seconds))
        
    @property
    def elapsed_td(self) -> datetime.timedelta:
        return datetime.timedelta(seconds=int(self.elapsed_seconds))

    @property
    def end_td(self) -> datetime.timedelta:
        return datetime.timedelta(seconds=int(self.end_seconds))
    
    def __str__(self):
        return f"{str(self.elapsed_td)[2:]} / {str(self.end_td)[2:]} ({self.elapsed_percent:3,.0%})"

@dataclasses.dataclass
class LogTimer:
    timer: Timer
    last_printed = None

    def tick(self):
        self.timer.tick()
        s = str(self.timer)
        if self.last_printed != s:
            # print(f"{CURSOR_UP}\r{CLEAR_LINE}{s}", flush=True)
            print(f"{CLEAR_LINE}{s}", end="\r", flush=True)
            self.last_printed = s

@dataclasses.dataclass
class LyricsLine:
    timestamp: float
    lyric: str | None
    subtitle: str
    next: typing.Self | None = None

    @staticmethod
    def parse(s: str) -> "LyricsLine":
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
        return LyricsLine(float(dur), lyric.strip() if lyric else lyric, subtitle.strip())

    @property
    def next_or_empty(self):
        return self.next if self.next else LyricsLine(timestamp=self.timestamp, lyric='', subtitle='')

    @property
    def lyric_firstline(self):
        return self.lyric.split('\n')[0] if self.lyric else None

    @property
    def subtitle_firstline(self):
        return self.subtitle.split('\n')[0]

    def render(self, next_line_in=None) -> str:
        next_line_in = next_line_in if next_line_in else datetime.timedelta(seconds=int(self.next_or_empty.timestamp - self.timestamp))
        return f"""{self.lyric_firstline or '-'}
{self.subtitle_firstline}

next line in {str(next_line_in)[2:]}:
{self.next_or_empty.lyric_firstline or '-'}
{self.next_or_empty.subtitle_firstline}"""

    def __lt__(self, other: typing.Self) -> bool:
        return self.timestamp < other.timestamp

@dataclasses.dataclass
class LyricsTimer:
    timer: Timer
    lyrics: list[LyricsLine]
    last_printed = None

    @staticmethod
    def parse(dur: float, s: str) -> "LyricsTimer":
        t = Timer(float(dur))
        ls = [LyricsLine.parse(l) for l in s.strip().split("\n")]
        if not len(ls):
            raise ValueError('empty lyrics')

        n = None
        for l in reversed(ls):
            l.next = n
            n = l
        ls = [LyricsLine(timestamp=0.0, lyric='', subtitle='', next=ls[0])] + ls
        sort = sorted(ls)
        if (str(ls) != str(sort)):
            raise ValueError('timed lyrics must be in order')
        if dur < ls[-1].timestamp:
            raise ValueError(f"song duration ({dur}) is less than last lyric's timestamp ({ls[-1].timestamp})")
        return LyricsTimer(t, ls)

    @property
    def subs_list(self) -> list[str]:
        return [l.subtitle for l in self.lyrics]

    @property
    def subs_block(self) -> str:
        return "\n\n".join(self.subs_list)

    def say(self, who) -> None:
        for l in self.lyrics:
            renpy.say(who=who, what=l.subtitle) # type: ignore

    def __str__(self):
        l = self.get_at(self.timer.elapsed_seconds, LyricsLine(0.0, '', '', next=self.lyrics[0]))
        # elapsed = l.timestamp if True else self.timer.elapsed_seconds # type: ignore
        # The web build prints less because we can't draw over the old timer
        elapsed = l.timestamp if renpy.variant('web') else self.timer.elapsed_seconds # type: ignore
        n = datetime.timedelta(seconds=int(l.next.timestamp - elapsed)) if l.next else datetime.timedelta(seconds=0)
        t = f"{str(datetime.timedelta(seconds=int(elapsed)))[2:]} / {str(self.timer.end_td)[2:]}"
        return f"""{t}\n{l.render(next_line_in=n)}"""

    def get_at(self, t: float, default_=None) -> LyricsLine | None:
        return next((l for l in reversed(self.lyrics) if t > l.timestamp), default_)

    def tick(self):
        self.timer.tick()
        s = str(self)
        if self.last_printed != s:
            # print(f"{CURSOR_UP}\r{CLEAR_LINE}{s}", flush=True)
            print(f"{CURSOR_UP}\r{CLEAR_LINE}"*7 + s, flush=True)
            self.last_printed = s
