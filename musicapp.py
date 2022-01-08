import math
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

id="2e7959faa85f44d6b2e859064f9dd1aa"
secrt="2514bb7ab37e449ba19db71e9f43bfc2"
def authentic_version():

    scope = "user-library-read"
    #but wheres the limit
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = id, client_secret = secrt, redirect_uri= 'http://localhost:8080'))
    results = sp.current_user_saved_tracks(limit=1, offset=0)
    n = results['total']
    m = n//50 # get how many chunks of 50 we can do at once
    r = n%50
    print(m)
    print(r)
    for i in range(m):
        results = sp.current_user_saved_tracks(limit=50, offset=i*50)
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx+50*i, track['artists'][0]['name'], " – ", track['name'])
    for j in range(r):
        results = sp.current_user_saved_tracks(limit=1, offset=(i+1)*50+j)
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx+50*(i+1)+j, track['artists'][0]['name'], " – ", track['name'])
def main():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2e7959faa85f44d6b2e859064f9dd1aa",
                                                               client_secret="2514bb7ab37e449ba19db71e9f43bfc2"))

    results = sp.search(q='joji', limit=5)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx+1, track['name'])
    print("---")
    authentic_version()

main()