#!/bin/bash
FPS=60
echo Running at $FPS FPS...

ffmpeg -video_size 640x1080 -framerate $FPS -f x11grab -i :0.0+634,0 -acodec libmp3lame -ar 11025 -f mpegts udp://127.0.0.1:1234
