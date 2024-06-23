## Installation
Use pytube instead of pytube3
```
pip install pytube==15.0.0
cd downloads
```

## Quick Start
Converting YouTube video into mp3
```py
# https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/
import os
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=Vk4KK-gh0FM")

# extract only audio
video = yt.streams.filter(only_audio=True).first()

f = video.download(output_path=".")
os.rename(f, os.path.splitext(f)[0] + ".mp3")
```