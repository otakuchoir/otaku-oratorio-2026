#!/bin/sh
set -eu
cd "`dirname "$0"`"

# -x: extract audio only
# -o: output filename
# many videos have silence at the start/end that we want to clip, but yt-dlp seems to break sometimes when we do that, so do it with renpy code instead

yt-dlp -xo bgm_scene02_01 https://www.youtube.com/watch?v=qkIJidLfHjk
yt-dlp -xo bgm_scene02_02 https://www.youtube.com/watch?v=ZYIcCHqdFuo 
#yt-dlp -xo bgm_scene03_01 https://www.youtube.com/watch?v=q-Dj-8yvfDk
#yt-dlp -xo bgm_scene03_02 https://www.youtube.com/watch?v=oEsGj0tCT4E
#yt-dlp -xo bgm_scene03_03 https://www.youtube.com/watch?v=3Vtrqoe-QzY
