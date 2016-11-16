#!/bin/bash
CMD='ffmpeg -video_size 322x1078 -framerate 30 -f x11grab -i :0.0+793,0 -acodec libmp3lame -ar 11025 -f mpegts udp://127.0.0.1:1234'

echo Running $CMD ...

ffmpeg -video_size 322x1078 -framerate 30 -f x11grab -i :0.0+793,0 -acodec libmp3lame -ar 11025 -f mpegts udp://127.0.0.1:1234
