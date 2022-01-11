# GUIDES

# Downloading one video
youtube-dl -x youtube_video_URL

# Downloading the mp3 (You will have to install ffmpeg or else just use VLC to convert the webm or m4a to mp3)
youtube-dl -x --audio-format mp3 youtube_video_URL

# Downloading the entire video playlist
youtube-dl -x https://www.youtube.com/playlist?list=XXXXXXXXXXXXXXXXXXX

# Checking the list of available formats
youtube-dl -F "http://www.youtube.com/watch?v=HRIF4_WzU1w"

# Choosing the format you want
youtube-dl -f 22 "http://www.youtube.com/watch?v=P9pzm5b6FFY"

# Using the python version
```py
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
```

```py
from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
```


For more information:
