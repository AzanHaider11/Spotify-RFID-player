#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

DEVICE_ID="**************"
CLIENT_ID="*******************"
CLIENT_SECRET="****************"

reader = SimpleMFRC522()


while True:
    try:
        print("Hold a tag near the reader")
        id = reader.read()[0]
        print(id)
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080",
                                                scope="user-read-playback-state,user-modify-playback-state"))
        
        
        def play(track_id):
            global begin
            sp.start_playback(device_id=DEVICE_ID, uris=[track_id])
            begin = time.time()
        
        def pause():
            global stop, waste
            sp.pause_playback(device_id=DEVICE_ID)
            stop = time.time()
            
        def resume(track_id):
            global stop, begin, waste
            time1 = stop-begin
            time = time1*1000
            sp.start_playback(device_id=DEVICE_ID, uris=[track_id], position_ms=time)

            
        # Plays song
        if id == 689494958099:
            curr_id = 'spotify:track:7MXVkk9YMctZqd1Srtv4MB'
            play(track_id = curr_id)
        
        if id == 620766503081:
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:2uupuqth8eC8SeJVhaMhX8')
        
        # Pauses song
        if id == 634242735091:
            try:
                pause()
            except Exception:
                pass
            
        if id == 427934489400:
            try:
                resume(track_id = curr_id)
            except Exception:
                pass

    except KeyboardInterrupt:
        GPIO.cleanup() 
        raise
