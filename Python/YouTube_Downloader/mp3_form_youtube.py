from pytube import YouTube
import os


# yt_url = 'https://www.youtube.com/watch?v=ZWijx_AgPiA'


def donwload_mp3(song):
    audio = YouTube(song).streams.get_audio_only()
    audio_download = audio.download(output_path='C:/Temp/music/Music from the Vietnam War')
    base, ext = os.path.splitext(audio_download)
    new_file = base + '.mp3'
    os.rename(audio_download, new_file)
    print(new_file)


yt_list = [
    'https://www.youtube.com/watch?v=ZWijx_AgPiA',
    'https://www.youtube.com/watch?v=O4irXQhgMqg',
    'https://www.youtube.com/watch?v=80_39eAx3z8',
    'https://www.youtube.com/watch?v=UtWJMCbofDc',
    'https://www.youtube.com/watch?v=RD4TFzkY5F0',
    'https://www.youtube.com/watch?v=N4bFqW_eu2I',
    'https://www.youtube.com/watch?v=LQUXuQ6Zd9w',
    'https://www.youtube.com/watch?v=N-aK6JnyFmk',
    'https://www.youtube.com/watch?v=GgnClrx8N2k',
    'https://www.youtube.com/watch?v=3T1c7GkzRQQ',
]

for song in yt_list:
    donwload_mp3(song)
