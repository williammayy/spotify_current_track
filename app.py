import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_playback()

if results:
    track = results['item']['name']
    album = results['item']['album']['name']
    artists = results['item']['artists'][0]['name']
    album_cover = results['item']['album']['images'][0]['url']
    print(f"{track}, {artists} - {artists} \n{album_cover}")
else:
    print("Nothing is playing...")
