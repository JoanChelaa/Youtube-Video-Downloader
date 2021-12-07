#Importing the pytube module

from tkinter import *
from pytube import YouTube
import tk

root = tk()

url = "https://www.youtube.com/watch?v=UEopd9O993M&list=RDUEopd9O993M&start_radio=1"
video = YouTube(url)

print ('The Title of the Video is')
print (video.title)

#Getting the video in the highest resolution
video = video.streams.get_highest_resolution()

print('The video downloaded is:')
video.download()