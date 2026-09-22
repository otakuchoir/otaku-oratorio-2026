"""renpy

label timed_lyrics(lt, who, first_line=""):
    call start_timer(lt)
    $ renpy.say(who=who, what=first_line)
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
class LyricsTimer:
    timer: Timer
    lyrics_ts: list[tuple[float, str]]
    last_printed = None

    @staticmethod
    def parse(dur: float, s: str) -> "LyricsTimer":
        t = Timer(float(dur))
        ls = lyrics_ts_parse(s)
        if not len(ls):
            raise ValueError('empty lyrics')
        if dur < ls[-1][0]:
            raise ValueError(f"song duration ({dur}) is less than last lyric's timestamp ({ls[-1][0]})")
        return LyricsTimer(t, ls)

    @property
    def lyrics_list(self) -> list[str]:
        return [l for (t, l) in self.lyrics_ts]

    @property
    def lyrics_block(self) -> str:
        return "\n\n".join(self.lyrics_list)

    def say(self, who) -> None:
        for l in self.lyrics_list:
            renpy.say(who=who, what=l) # type: ignore

    def __str__(self):
        l = self.get_at(self.timer.elapsed_seconds)
        return f"{str(self.timer)} {l}"

    def get_at(self, t: float) -> str | None:
        return next((l for (t0, l) in reversed(self.lyrics_ts) if t > t0), None)

    def tick(self):
        self.timer.tick()
        s = str(self)
        if self.last_printed != s:
            # print(f"{CURSOR_UP}\r{CLEAR_LINE}{s}", flush=True)
            print(f"{CLEAR_LINE}{s}", end="\r", flush=True)
            self.last_printed = s

def lyrics_ts_parse(s: str) -> list[tuple[float, str]]:
    lines = [_lyrics_ts_parse_line(l) for l in s.strip().split("\n")]
    sort = sorted(lines, key=lambda pair: pair[0])
    if (str(lines) != str(sort)):
        raise ValueError('timed lyrics must be in order')
    return sort
def _lyrics_ts_parse_line(l: str) -> tuple[float, str]:
    dur, lyric = l.split(None, 1)
    return float(dur), lyric
