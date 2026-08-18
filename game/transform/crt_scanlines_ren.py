import renpy # type: ignore

"""renpy

image fx_crt_scanlines = CRTScanlines()
init python:
"""
import math
class CRTScanlines(renpy.Displayable):
    def __init__(self, **kwargs):
        super(CRTScanlines, self).__init__(**kwargs)

    def render(self, width, height, st, at):
        render = renpy.Render(width, height)
        canvas = render.canvas()
        line_y = 3
        row_y = line_y * 2
        rows = math.ceil(height / row_y)
        for i in range(rows):
            y = i * row_y
            canvas.rect("#000b", (0, i * row_y, width, line_y))
        return render