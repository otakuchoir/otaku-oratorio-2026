init python:
    for i in [6]:
        load_image(f'eyecatch {i:02d}', f'assets/Eyecatches/Eyecatcher {i}.png') # type: ignore

label eyecatch06:
    scene eyecatch 06 at screen_size with fade
    pause
    scene black with fade
    return