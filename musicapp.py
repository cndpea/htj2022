import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

id="2e7959faa85f44d6b2e859064f9dd1aa"
secrt="2514bb7ab37e449ba19db71e9f43bfc2"
def authentic_version():

    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = id, client_secret = secrt, redirect_uri= 'http://localhost:8080'))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2e7959faa85f44d6b2e859064f9dd1aa",
                                                               client_secret="2514bb7ab37e449ba19db71e9f43bfc2"))

    results = sp.search(q='joji', limit=1)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
    authentic_version()

main()