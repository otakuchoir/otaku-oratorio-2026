#!/bin/sh
set -eu
cd "`dirname "$0"`"

# -x: extract audio only
# -o: output filename
# --download-sections: clip only part of the audio.
#     many videos have silence at the start/end that we want to clip,
#     but yt-dlp sometimes chokes when we do that, so usually we'll 
#     clip with renpy code instead
#
# comment out already-downloaded videos, to avoid youtube rate-limiting.
# never delete them, keep here for later reference
#yt-dlp -xo bgm_scene02_01 https://www.youtube.com/watch?v=qkIJidLfHjk
#yt-dlp -xo bgm_scene02_02 https://www.youtube.com/watch?v=ZYIcCHqdFuo 
#yt-dlp -xo bgm_scene03_01 https://www.youtube.com/watch?v=q-Dj-8yvfDk
#yt-dlp -xo bgm_scene03_02 https://www.youtube.com/watch?v=oEsGj0tCT4E
#yt-dlp -xo bgm_scene03_03 https://www.youtube.com/watch?v=3Vtrqoe-QzY
#yt-dlp -xo bgm_scene04_01 https://www.youtube.com/watch?v=XVfz__YP4fo
#yt-dlp -xo bgm_scene04_02 https://www.youtube.com/watch?v=ahVNJRbGOrs
#yt-dlp -xo bgm_scene05_01 https://www.youtube.com/watch?v=Fmu32oWqHx0
#yt-dlp -xo bgm_scene06_01 https://www.youtube.com/watch?v=GpBhJo3Jwk8
##yt-dlp -xo bgm_scene07_01 duplicate of 04_01
#yt-dlp -xo bgm_scene10_01 https://www.youtube.com/watch?v=8dZ4OZihEAw
#yt-dlp -xo bgm_scene11_01 https://www.youtube.com/watch?v=b-GWaFYgXM0 
##yt-dlp -xo bgm_scene12_01 duplicate of 04_02
#yt-dlp -xo bgm_scene13_01 https://www.youtube.com/watch?v=H-W7xveVzUw
#yt-dlp -xo bgm_scene13_02 https://www.youtube.com/watch?v=aOwJyEKupdc --download-sections "*00:00:00-00:00:03.05"
#yt-dlp -xo bgm_scene14_01 https://www.youtube.com/watch?v=Al4ongqx_2I
#yt-dlp -xo bgm_scene15_01 https://www.youtube.com/watch?v=kQuBZcO0m7A
#yt-dlp -xo bgm_scene15_02 https://www.youtube.com/watch?v=WSphnwWo7E8