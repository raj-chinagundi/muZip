from youtube_search import YoutubeSearch
from pytube import YouTube
from flask import send_file
import zipfile
import os


def searchtube(artist, songNumber):
    results = YoutubeSearch(artist, max_results=songNumber).to_dict()
    s = 'www.youtube.com'
    urls = []
    for value in results:
        urls.append(s+value['url_suffix'])

    for url in urls:
        audio = YouTube(url)
        audio.streams.filter(only_audio=True).first().download(
            output_path='./audio/')

    handle = zipfile.ZipFile('audios.zip', 'w')

    
    os.chdir('./audio/')

    for x in os.listdir():
        handle.write(x, compress_type=zipfile.ZIP_DEFLATED)
        os.remove(x)

    handle.close()
    
    os.chdir("../")

    os.rmdir("./audio/")





