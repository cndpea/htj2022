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
            print('No results for this account')
            break
        track = results['items'][0]['track']
        uri = track['uri']
        af = sp.audio_features(uri)[0]
        v = af['valence']
        d = af['danceability']
        e = af['energy']
        k = af['key']
        score = (0.4*e+0.6*d+0.6*v+0.2*k) * 100

        if (score > hi_score):
            hi_score_track = track['uri']
            hi_score = score
            #print(i, '*')
        
    print(sp.track(hi_score_track)['artists'][0]['name'], " - ", sp.track(hi_score_track)['name'])
    final_score = "{:.2f}".format(hi_score)
    print("score = ", final_score)
def main():
    authentic_version()

main()