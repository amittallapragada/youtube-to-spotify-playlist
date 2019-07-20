
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