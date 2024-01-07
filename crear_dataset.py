# -*- coding: utf-8 -*-
import pandas as pd
import json

# Cargar datos desde el archivo JSON
with open('taylor_swift_spotify.json') as f:
    data = json.load(f)
    print(data) # Imprimir el archivo JSON

# Verificar si data es un diccionario
if isinstance(data, dict):
    # Si es un diccionario, convertir a una lista de un solo elemento
    data = [data]
   
# Crear listas para almacenar los datos
artist_id_list = []
artist_name_list = []
artist_popularity_list = []
album_id_list = []
album_name_list = []
album_release_date_list = []
album_total_tracks_list = []
disc_number_list = []
duration_ms_list = []
explicit_list = []
track_number_list = []
danceability_list = []
energy_list = []
key_list = []
loudness_list = []
mode_list = []
speechiness_list = []
acousticness_list = []
instrumentalness_list = []
liveness_list = []
valence_list = []
tempo_list = []
id_list = []
time_signature_list = []
track_popularity_list = []
track_id_list = []
track_name_list = []

# Procesar cada artista, álbum y pista
for artist in data:
    artist_id = artist.get('artist_id', '')
    artist_name = artist.get('artist_name', '')
    artist_popularity = artist.get('artist_popularity', 0)

    for album in artist.get('albums', []):
        album_id = album.get('album_id', '')
        album_name = album.get('album_name', '')
        album_release_date = album.get('album_release_date', '')
        album_total_tracks = album.get('album_total_tracks', 0)

        for track in album.get('tracks', []):
            artist_id_list.append(artist_id)
            artist_name_list.append(artist_name)
            artist_popularity_list.append(artist_popularity)
            album_id_list.append(album_id)
            album_name_list.append(album_name)
            album_release_date_list.append(album_release_date)
            album_total_tracks_list.append(album_total_tracks)

            disc_number_list.append(track.get('disc_number', 0))
            duration_ms_list.append(track.get('duration_ms', 0))
            explicit_list.append(track.get('explicit', False))
            track_number_list.append(track.get('track_number', 0))

            audio_features = track.get('audio_features', {})
            danceability_list.append(audio_features.get('danceability', 0))
            energy_list.append(audio_features.get('energy', 0))
            key_list.append(audio_features.get('key', 0))
            loudness_list.append(audio_features.get('loudness', 0))
            mode_list.append(audio_features.get('mode', 0))
            speechiness_list.append(audio_features.get('speechiness', 0))
            acousticness_list.append(audio_features.get('acousticness', 0))
            instrumentalness_list.append(audio_features.get('instrumentalness', 0))
            liveness_list.append(audio_features.get('liveness', 0))
            valence_list.append(audio_features.get('valence', 0))
            tempo_list.append(audio_features.get('tempo', 0))
            id_list.append(audio_features.get('id', ''))
            time_signature_list.append(audio_features.get('time_signature', 0))

            track_popularity_list.append(track.get('track_popularity', 0))
            track_id_list.append(track.get('track_id', ''))
            track_name_list.append(track.get('track_name', ''))

# Crear DataFrame con las listas de datos
df = pd.DataFrame({
    'artist_id': artist_id_list,
    'artist_name': artist_name_list,
    'artist_popularity': artist_popularity_list,
    'album_id': album_id_list,
    'album_name': album_name_list,
    'album_release_date': album_release_date_list,
    'album_total_tracks': album_total_tracks_list,
    'disc_number': disc_number_list,
    'duration_ms': duration_ms_list,
    'explicit': explicit_list,
    'track_number': track_number_list,
    'danceability': danceability_list,
    'energy': energy_list,
    'key': key_list,
    'loudness': loudness_list,
    'mode': mode_list,
    'speechiness': speechiness_list,
    'acousticness': acousticness_list,
    'instrumentalness': instrumentalness_list,
    'liveness': liveness_list,
    'valence': valence_list,
    'tempo': tempo_list,
    'id': id_list,
    'time_signature': time_signature_list,
    'track_popularity': track_popularity_list,
    'track_id': track_id_list,
    'track_name': track_name_list
})

# Verificar el DataFrame antes de guardarlo
print(df.head())

# Guardar el DataFrame en un archivo CSV
df.to_csv('dataset.csv', index=False)