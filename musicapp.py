import math
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#secret will be made invalid on Monday, if you need it again lmk
id="2e7959faa85f44d6b2e859064f9dd1aa"
secrt="2514bb7ab37e449ba19db71e9f43bfc2"

def authentic_version():

    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = id, client_secret = secrt, redirect_uri= 'http://localhost:8080'))
    results = sp.current_user_saved_tracks(limit=1, offset=0)
    n = results['total'] #gives number of saved tracks.
    m = n//50 # get how many chunks of 50 we can do at once
    r = n%50 #remainder
    lowest_v = 2
    for i in range(m):
        #doing 50 at a time results in much, much faster processing
        results = sp.current_user_saved_tracks(limit=50, offset=i*50)
        for idx, item in enumerate(results['items']):
            track = item['track']
            v = sp.audio_features(track['uri'])[0]['valence']
            l = sp.audio_features(track['uri'])[0]['loudness']
            print(idx+50*i, track['artists'][0]['name'], " – ", track['name'],  "v=", v, ", l=", l)
    i += 1
    for j in range(r):
        #remainder are processed individually
        results = sp.current_user_saved_tracks(limit=1, offset=(i+1)*50+j)
        for idx, item in enumerate(results['items']):
            track = item['track']
            v = sp.audio_features(track['uri'])[0]['valence']
            d = sp.audio_features(track['uri'])[0]['danceability']
            print(idx + 50 * i + j, track['artists'][0]['name'], " – ", track['name'], "v=", v, ", d=", d)
def main():
    authentic_version()

main()