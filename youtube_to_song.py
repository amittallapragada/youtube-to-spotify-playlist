import requests
from bs4 import BeautifulSoup
##Function takes a mobile youtube url and attempts to return the artist and song names from the title

#url must be from youtube mobile
def get_songs(URL):
    data = requests.get(URL)
    data = BeautifulSoup(data.text)
    #1. filter to song table
    table = data.find('table', 'pl-video-table')
    songs = table.find_all('tr', 'pl-video yt-uix-tile')
    song_names = [s.find('td', 'pl-video-title') for s in songs]
    song_names = [s.text.replace('\n', '') for s in song_names]
    song_names = [s.split('by')[0].strip() for s in song_names]
    song_names = [s.replace('(Official Video)', '') for s in song_names]
    artist_names = [s.split('-')[0].strip() for s in song_names]
    song_names = [s.split('-')[1].strip() for s in song_names]
    return artist_names, song_names



#### TEST
# URL = 'https://m.youtube.com/playlist?list=PLm2SjZLv_q0hxh2FWyL-kVU1gsyXLAsk9'
# print(get_songs(URL))