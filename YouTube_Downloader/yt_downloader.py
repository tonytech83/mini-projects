from pytube import YouTube
from sys import argv

# used to add link to executed python file (py.exe .\yt_downloader.py "https://www.youtube.com/watch?v=_iffYh7Ewy8")
link = argv[1]

# created object with argument link of the video
yt = YouTube(link)

# Output folder, where video should be downloaded (mp4 format)
output_path = 'c:/Temp/Downloaded_Videos'

# Takes info about the video
print('Title: ', yt.title)
print('Views: ', yt.views)

# takes the highest video resolution
yd = yt.streams.get_highest_resolution()

# downloading the video
yd.download(output_path)