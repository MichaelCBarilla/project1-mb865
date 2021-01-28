from flask import Flask, render_template
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID='ID GOES HERE'
SPOTIPY_CLIENT_SECRET='SECRET GOES HERE'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
                                                      
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

urn = 'spotify:artist:3Rq3YOF9YG9YfCWD4D56RZ'

artist = spotify.artist(urn)


app = Flask(__name__)

@app.route('/')
def get_song():
    print(artist['name'])
    return render_template(
        'index.html'
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

