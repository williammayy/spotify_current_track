import spotipy
import time
import requests
import logging
import os, sys
from logging.handlers import RotatingFileHandler
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import Tk, Canvas
import spotipy.util as util
# from spotipy.oauth2 import SpotifyOAuth

# Configures logger for storing song data
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='spotipy.log',level=logging.INFO)
logger = logging.getLogger('spotipy_logger')

# automatically deletes logs more than 2000 bytes
handler = RotatingFileHandler('spotipy.log', maxBytes=2000,  backupCount=3)
logger.addHandler(handler)

scope = "user-read-playback-state"

previous_song = ""
current_song = ""

directory = os.path.dirname(os.path.abspath(sys.argv[0]))

token_path = directory + '/.cache'
scope = 'user-read-currently-playing'
token = util.prompt_for_user_token(scope, cache_path=token_path)
sp = spotipy.Spotify(auth=token)

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#create the fullscreen window
os.environ['DISPLAY'] = ':0'
display = os.environ.get('DISPLAY')
print(display)
root = Tk()
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
screen_middle = ((screen_width/2) - (screen_height/2))
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.quit())

default_image_path = directory + '/images/black.png'
default_image = Image.open(directory + '/images/black.png')
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
