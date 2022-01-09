import math
import spotipy
import random
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
    search_length = 20 #how many random tracks to check, keep under a hundred
    hi_score_track = ""
    hi_score = 0
    for i in range(search_length):
        #doing 50 at a time results in much, much faster processing
        results = sp.current_user_saved_tracks(limit=1, offset=random.randrange(0,(n-1)))
        if (len(results) == 0):
            break
        track = results['items'][0]['track']
        uri = track['uri']
        af = sp.audio_features(uri)[0]
        v = af['valence']
        d = af['danceability']
        e = af['energy']
        score = (0.4*e + 0.5*d + 0.5*v + 0.5*(af['mode']))

        if (score > hi_score):
            hi_score_track = track['uri']
            hi_score = score
            print(i, '*')
        else:
            print(i)
    print(sp.track(hi_score_track)['artists'][0]['name'], " - ", sp.track(hi_score_track)['name'])
    print("score= ", hi_score)
def main():
    authentic_version()

main()