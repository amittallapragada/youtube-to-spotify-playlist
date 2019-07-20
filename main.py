import requests
from bs4 import BeautifulSoup

try:
    file_r = open('output.html')
    data = BeautifulSoup(file_r, 'html.parser')
except Exception as e:
    print(e)
    URL = 'https://m.youtube.com/playlist?list=PLm2SjZLv_q0hxh2FWyL-kVU1gsyXLAsk9'
    data = requests.get(URL)


#try filtering

#1. filter to song table
table = data.find('table', 'pl-video-table')
#print(table)
songs = table.find_all('tr', 'pl-video yt-uix-tile')
song_names = [s.find('td', 'pl-video-title') for s in songs]
song_names = [s.text.replace('\n', '') for s in song_names]
song_names = [s.split('by')[0].strip() for s in song_names]

#fix this
song_names = [s.replace('(Official Video)', '') for s in song_names]
# song_names = [s.replace('\n', '') for s in song_names]

CLIENT_ID = '06fc8266fc51402281de005991aa5759'
CLIENT_ID_SECRET = '1fd014bb10cc4c2490486babcc85b4ab'


SPOTIFY_URL = "https://accounts.spotify.com/authorize"
RESP = 'code'
REDIRECT_URI = 'https://www.spotify.com/us/'
SCOPE = 'playlist-modify-private'

data = {
    'client_id':CLIENT_ID,
    'response_type':'code',
    'redirect_uri':REDIRECT_URI,
    'scope':SCOPE
}

resp = requests.get(SPOTIFY_URL, data=data)
print(resp.text)