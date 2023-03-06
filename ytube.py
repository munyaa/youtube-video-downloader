from tkinter import *
from pytube import YouTube

def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    download_label.config(text='Download complete!')

root = Tk()
root.title('YouTube Downloader')

url_label = Label(root, text='Enter YouTube URL:')
url_label.pack()

url_entry = Entry(root, width=50)
url_entry.pack()

download_button = Button(root, text='Download', command=download_video)
download_button.pack()

download_label = Label(root, text='')
download_label.pack()

root.mainloop()


def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    download_label.config(text='Download complete!')
