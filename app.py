from flask import Flask, render_template
import os
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

class track_info:
    def __init__(self, name, artist, album_image, preview):
        self.name = name
        self.artist = artist
        self.album_image = album_image
        self.preview = preview
        
        
app = Flask(__name__)

# SPOTIPY_CLIENT_ID='id'
# SPOTIPY_CLIENT_SECRET='secret'

# client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
#                                                       client_secret=SPOTIPY_CLIENT_SECRET)
                                                      
# spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



# nujabes = 'spotify:artist:3Rq3YOF9YG9YfCWD4D56RZ'
# sturgill_simpson = 'spotify:artist:3vDpQbGnzRbRVirXlfQagB'
# frank_ocean = '2h93pZq0e7k5yf4dywlkpM'
# the_pillows = '6ilYV5oF8whllOnm4VZlYR'

# artists_IDs = [
#     nujabes, 
#     sturgill_simpson,
#     frank_ocean,
#     the_pillows
# ]

# track_list = []
# track_list_len = len(artists_IDs) * 10

# # Loop through artists
# for artist in artists_IDs:
#     result = spotify.artist_top_tracks(artist)
#     # Get top ten tracks from artist
#     for track in result['tracks'][:10]:
#         track_list.append(track)


@app.route('/')
def get_song():
    # index = random.randint(0,track_list_len-1)
    # chosen_one = track_list[index]
    # name = chosen_one['name']
    # artist = chosen_one['artists'][0]['name']
    # album_image = chosen_one['album']['images'][0]['url']
    # preview = chosen_one['preview_url']
    
    # track = track_info(name, artist, album_image, preview)
    track = track_info("song", "artist", "gfdgdfg", "gfdgdfgdf")
    
    return render_template(
        'index.html',
        track = track
    )
    
app.run(
    port = int(os.environ.get('PORT', 5000)),
    host=os.getenv('IP', '0.0.0.0')
)

