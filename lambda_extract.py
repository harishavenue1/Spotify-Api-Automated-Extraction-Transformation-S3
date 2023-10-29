import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    # get the envionrment variables names
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"'
    playlist_URI = playlist_link.split("/")[-1].split('?')[0] # to get 37i9dQZEVXbNG2KDcFcKOF -- is the actual id for playlist
    data = sp.playlist_tracks(playlist_URI)
    
    fileName = 'spotify_raw_' + str(datetime.now()) + '.json'
    
    client = boto3.client('s3')
    client.put_object(
        Bucket='spotify-etl-harish',
        Key='raw_data/to_process/'+fileName,
        Body=json.dumps(data)
        )
