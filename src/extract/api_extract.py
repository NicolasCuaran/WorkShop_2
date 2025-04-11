import requests
import pandas as pd
import re
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

# Función para separar artistas con múltiples delimitadores
def split_artists(texto):
    """
    Split a string of artists into a list, handling various delimiters.
    """

    texto = re.sub(r'\s*Featuring\s*', ',', texto, flags=re.IGNORECASE)

    partes = re.split(r'[;&]', texto)

    return [artista.strip() for artista in partes if artista.strip()]

def read_spotify_data():
    """
    Read Spotify data from a CSV file and return a DataFrame.
    """
    
    df_grammys_artists = pd.read_csv("/opt/airflow/data/artist.csv")
    #df_grammys_artists = df_grammys_artists.head(30)
    
    artistas_raw = df_grammys_artists['artist'].dropna().unique()
    artistas = set()
    
    for grupo in artistas_raw:
        for artista in split_artists(grupo):
            artistas.add(artista)
    
    return artistas


def extracting_musicbrainz_data():
    """
    Extracting data from MusicBrainz and returning it as a DataFrame.
    """
    headers = {'User-Agent': 'ETLWorkshop/1.0 (tucorreo@dominio.com)'}
    datos_artistas = []
    
    artistas = read_spotify_data()
    logging.info(f"Total artists to process: {len(artistas)}")

    for artista in artistas:
        query = artista.replace(" ", "+")
        url = f"https://musicbrainz.org/ws/2/artist/?query=artist:{query}&fmt=json&limit=1"

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get('artists'):
                a = data['artists'][0]
                datos_artistas.append({
                    'artist_name': artista,
                    'artist_id': a.get('id'),
                    'country': a.get('country'),
                    'begin_date': a.get('life-span', {}).get('begin'),
                    'end_date': a.get('life-span', {}).get('end'),
                    'type': a.get('type'),
                    'gender': a.get('gender'),
                    'disambiguation': a.get('disambiguation')
                })
                logging.info(f"Data for {artista} extracted successfully.")
        else:
            logging.error(f"Error with {artista}: {response.status_code}")

        time.sleep(1)

    df_api = pd.DataFrame(datos_artistas)
    return df_api