# vim: set ft=python:

import vapoursynth as vs
core = vs.get_core()

clip = video_in
clip = core.std.Trim(clip, first=0, length=500000)
clip = core.f3kdb.Deband(clip, output_depth=16, dynamic_grain=True, grainy=16, grainc=16)
clip.set_output()
