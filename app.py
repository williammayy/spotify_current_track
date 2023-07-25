import spotipy
import time
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import Tk, Canvas
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state"

previous_song = ""
current_song = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#create the fullscreen window
root = Tk()
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
screen_middle = ((screen_width/2) - (screen_height/2))
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.quit())

default_image = Image.open('./images/black.png')
default_image = default_image.resize((screen_height, screen_height), Image.Resampling.LANCZOS)

#create PhotoImage object for image
photo = ImageTk.PhotoImage(default_image)

#create Canvas and show fullscreen image
canvas = Canvas(root, width=screen_height, height=screen_height, bg="black")
canvas.pack(fill='both', expand=True)
canvas.create_image(screen_middle, 0, image=photo, anchor='nw')
root.config(cursor='none')

while True:
    results = sp.current_playback()
    time.sleep(1)
    if results is None:
        current_song = 'none'
        if previous_song != current_song:
            previous_song = 'none'
            canvas.delete("all")
            photo = ImageTk.PhotoImage(default_image)
            canvas.create_image(screen_middle, 0, image=photo, anchor='nw')
            root.update()
    else:
        print(results)
        current_song = results['item']['name']
        if previous_song != current_song:
            track = results['item']['name']
            album = results['item']['album']['name']
            artists = results['item']['artists'][0]['name']
            album_cover = results['item']['album']['images'][0]['url']
            previous_song = results['item']['name']

            response = requests.get(album_cover)
            canvas.delete("all")
            image = Image.open(BytesIO(response.content))
            image = image.resize((screen_height, screen_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.create_image(screen_middle, 0, image=photo, anchor='nw')
            root.update()

    time.sleep(4)
