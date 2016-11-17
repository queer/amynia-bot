# osu!mania bot

An attempt at making an osu!mania bot that plays the game through OpenCV. Currently, the bot can automatically distinguish between 4K and 7K, and can hit normal notes. Sliders are currently NOT supported, so slider-heavy maps WILL break it.

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
