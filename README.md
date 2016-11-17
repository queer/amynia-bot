# osu!mania bot

An attempt at making an osu!mania bot that plays the game through OpenCV

To use:

```
# Terminal A
./ffmpeg.sh

# Terminal B
python3 main.py
```

Main issue(s)

 * Can't stream it at the same time as running it, because OBS makes ffmpeg drop frames for some reason ._>
 * ffmpeg likes dropping lots of frames anyway...
