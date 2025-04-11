from extract.spotify_extract import extracting_spotify_data
from extract.grammys_extract import extracting_grammys_data
from extract.api_extract import extracting_musicbrainz_data
from transform.spotify_transform import transforming_spotify_data
from transform.grammys_transform import transforming_grammys_data
from transform.api_transform import transforming_api_data
from transform.merge import merge_data
from load_and_store.load import loading_merged_data
from load_and_store.store import storing_merged_data

import os
import json
import pandas as pd
import logging

def extract_spotify():
    try:
        df = extracting_spotify_data("./data/spotify_dataset.csv") 
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error extracting data: {e}")

def extract_grammys():
    try:
        df = extracting_grammys_data()
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error extracting data: {e}")
        
def extract_musicbrainz():
    try:
        df = extracting_musicbrainz_data()
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error extracting MusicBrainz data: {e}")

def transform_spotify(df):
    try:
        json_df = json.loads(df)
        
        raw_df = pd.DataFrame(json_df)
        df = transforming_spotify_data(raw_df)
        
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        
def transform_grammys(df):
    try:
        json_df = json.loads(df)
        raw_df = pd.DataFrame(json_df)
        df = transforming_grammys_data(raw_df)
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error transforming Grammys data: {e}")

def transform_musicbrainz(df):
    try:
        json_df = json.loads(df)
        raw_df = pd.DataFrame(json_df)
        df = transforming_api_data(raw_df)
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error transforming MusicBrainz data: {e}")

def merge_transformed_data(spotify_data, grammys_data, musicbrainz_data):
    try:
        spotify_df = pd.DataFrame(json.loads(spotify_data))
        grammys_df = pd.DataFrame(json.loads(grammys_data))
        musicbrainz_df = pd.DataFrame(json.loads(musicbrainz_data))
        
        merged_data = merge_data(spotify_df, grammys_df, musicbrainz_df)
        return merged_data
    except Exception as e:
        logging.error(f"Error merging data: {e}")

def load_data_to_database(merged_data):
    try:
        df = pd.DataFrame(json.loads(merged_data))
        loading_merged_data(df, "merged_data")
    except Exception as e:
        logging.error(f"Error loading data to database: {e}")

def store_data(merged_data):
    try:
        df = pd.DataFrame(json.loads(merged_data))
        storing_merged_data("merged_data", df)
    except Exception as e:
        logging.error(f"Error storing data locally: {e}")