import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state"

previous_song = ""
current_song = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
while True:
    results = sp.current_playback()
    if results is None:
        current_song = 'none'
        if previous_song != current_song:
            previous_song = 'none'
            print("There is no song playing...")
    else:
        current_song = results['item']['name']
        if previous_song != current_song:
            track = results['item']['name']
            album = results['item']['album']['name']
            artists = results['item']['artists'][0]['name']
            album_cover = results['item']['album']['images'][0]['url']
            previous_song = results['item']['name']

            print(f"{track}, {artists} - {album} \n{album_cover}")

    time.sleep(5)
