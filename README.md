Requirements:

  - Project on https://developer.spotify.com/
  - Python 3 - sudo apt install python3
  - python3-pip - sudo apt install python3-pip
  - Spotipy - pip install spotipy --upgrade - Docs: https://spotipy.readthedocs.io/
  - Pillow Library - pip install pillow --upgrade - To open images
    if has errors: sudo apt install libjpeg-dev zlib1g-dev
  - TK - sudo apt-get install python3-tk - create graphic interface

Setup:
  export environment variables on terminal:
    - export SPOTIPY_CLIENT_ID='your-client-id'
    - export SPOTIPY_CLIENT_SECRET='your-client-secret'
    - export SPOTIPY_REDIRECT_URI='http://localhost/'

  run the python script:
  python3 app.py
  this will open a window to log in your spotify account and grant permission to the app;
  paste the redirected url on terminal, url exemple: 'http://localhost/?code=xxxxxx';
