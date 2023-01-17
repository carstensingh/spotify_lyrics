#export SPOTIPY_CLIENT_ID='bbf5b65023f64e7896ba3b9197caab5f'
#export SPOTIPY_CLIENT_SECRET='826e7c6fdfbc4d0ca2b8fe17f7787231'
#export SPOTIPY_REDIRECT_URI='https://google.com'
#export GENIUS_ACCESS_TOKEN='8Fzw6EtrpIGquPMknNoiphCC8DK1BlDRv4YJMn90KytJa7LFWYr912zGM_up3OMu'

import os
import json
import time
import spotipy
import lyricsgenius as lg

#spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
#spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
#spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
#genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

spotify_client_id = 'bbf5b65023f64e7896ba3b9197caab5f'
spotify_secret = '826e7c6fdfbc4d0ca2b8fe17f7787231'
spotify_redirect_uri = 'https://google.com'
genius_access_token = '8Fzw6EtrpIGquPMknNoiphCC8DK1BlDRv4YJMn90KytJa7LFWYr912zGM_up3OMu'

scope = 'user-read-currently-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id, 
                                client_secret=spotify_secret, 
                                redirect_uri=spotify_redirect_uri, 
                                scope=scope)


token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
#token = oauth_object.get_cached_token()

#spotify object
spotify_object = spotipy.Spotify(auth=token)

#genius object
genius = lg.Genius(genius_access_token)

current = spotify_object.currently_playing()





while True:
    current = spotify_object.currently_playing()
    status = current['currently_playing_type']
    if status == 'track':
        artist_name = current['item']['album']['artists'][0]['name']
        song_title = current['item']['name']
        length = current['item']['duration_ms']
        progress = current['progress_ms']
        time_left = int(((length-progress)/1000))


        song = genius.search_song(title=song_title, artist = artist_name)
        lyrics = song.lyrics
        print(lyrics)

        time.sleep(time_left)
    elif status == 'ad':
        time.sleep(30)