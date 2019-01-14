import os
import sys

#from pytube import YouTube
import pytube

args = sys.argv

params = ['--url=']

for a in args:
	if a.startswith(params[0]):
		url = a[len(params[0]):]
		yt = pytube.YouTube
		r = yt(url).streams.filter(file_extension='mp4').first().download()
		print(r)

##>>> YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()

#>>> yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')

#>>> yt.streams
#... .filter(progressive=True, file_extension='mp4')
#... .order_by('resolution')
#... .desc()
#... .first()
#... .download()

#>>> yt.streams.filter(progressive=True).all()

#>>> yt.streams.filter(adaptive=True).all()

#>>> yt.streams.filter(only_audio=True).all()

#>>> yt.streams.filter(file_extension='mp4').all()

#pytube.extract.video_id(url)