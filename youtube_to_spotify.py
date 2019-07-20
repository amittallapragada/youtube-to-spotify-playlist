import spotipy
import sys 
import spotipy.util as util 
from youtube_to_song import get_songs
from constants import credentials 

#authorize application
CLIENT_ID = credentials['CLIENT_ID']
CLIENT_ID_SECRET = credentials['CLIENT_ID_SECRET']
SPOTIFY_URL = "https://accounts.spotify.com/authorize"
RESP = 'code'
REDIRECT_URI = 'https://www.spotify.com/us/'
SCOPE = 'playlist-modify-private playlist-modify-public user-library-read'

#enter username and youtube link and new playlist name

if len(sys.argv) > 1:
    username = sys.argv[1]
    URL = sys.argv[2]
    playlist_name = sys.argv[3]
else:
    print("Usage : %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username,SCOPE,client_id=CLIENT_ID, client_secret=CLIENT_ID_SECRET, redirect_uri='http://localhost/')
#create spotipy agent
sp = spotipy.Spotify(auth=token)
#get artist and song names from youtube link
artists, songs = get_songs(URL)
print('got youtube links...')
#create a list of spotify song urls
song_urls = []
for i in range(len(songs)):
    try:
        results = sp.search(q='track:' + songs[i]+ ",", type='track,artist')
        song = None
        for item in results['tracks']['items']:
            if item['artists'][0]['name'] == artists[i]:
                song = item
                break
        if song is None:
            print('couldnt find song: ' + songs[i] + " by: " + arists[i])
        song_urls.append(song['external_urls']['spotify'])
    except Exception as e:
        print(e)
        print(songs[i])
print('got spotify links...')


resp = sp.user_playlist_create(name=playlist_name, user=username, public=False)
print('created new playlist...')
#done get playlist id
playlist_id = resp['id']

sp.user_playlist_add_tracks(username, playlist_id, song_urls, position=None)
print('added songs')
print('done.')
