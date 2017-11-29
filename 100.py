import spotipy
import spotipy.util as sputil

import settings

token = sputil.prompt_for_user_token(settings.USER, settings.SCOPE, client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET, redirect_uri=settings.REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

tracks_1 = sp.current_user_saved_tracks(limit=50)
tracks_2 = sp.current_user_saved_tracks(limit=50, offset=50)

track_ids = [track.get('track').get('id') for track in tracks_1.get('items')]
track_ids.extend([track.get('track').get('id') for track in tracks_2.get('items')])
sp.user_playlist_replace_tracks(settings.USER, settings.PLAYLIST_ID, track_ids)