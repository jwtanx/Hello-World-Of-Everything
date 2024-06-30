## Installation
Use pytube instead of pytube3
```
pip install pytube==15.0.0
cd downloads
```

## Quick Start
### Converting YouTube video into mp3
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

### Getting the highest resolution
```py
import pytube
yt = pytube.YouTube("https://www.youtube.com/watch?v=sE5NtcoOR7w")
stream = yt.streams.get_highest_resolution()
stream.download(output_path=".")
```

```py
import pytube
from pytube.cli import on_progress

url = "https://www.youtube.com/watch?v=sE5NtcoOR7w"
yt = pytube.YouTube(url, on_progress_callback=on_progress)
# no sound, unlimited quality, .webm file
video = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
video.download(output_path=".")
```

```py
import pytube

video = pytube.YouTube("https://www.youtube.com/watch?v=sE5NtcoOR7w", on_progress_callback=on_progress)
resolutions = video.streams.all()

for i in resolutions:
    print(i)

video.streams.get_by_itag(136).download(".")
```