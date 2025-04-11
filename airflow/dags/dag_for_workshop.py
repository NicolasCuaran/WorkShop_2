# Libraries to work with Airflow
# --------------------------------

from datetime import datetime, timedelta
from airflow.decorators import dag, task

# Importing the necessary modules
# --------------------------------
from task.etl import *

# Define the DAG
# --------------

default_args = {
    'owner': "airflow",
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 10),
    'email': "example@example.com",
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    default_args=default_args,
    description='ETL pipeline for data extraction, transformation, and merging.',
    schedule_interval=timedelta(days=1),
    max_active_runs=1,
    catchup=False,
    concurrency=4,
)
def etl_dag():
    """
    This DAG orchestrates the ETL pipeline for extracting, transforming, merging, and storing data.
    """
    
    @task
    def spotify_extraction():
        return extract_spotify()
    
    spotify_raw_data = spotify_extraction()
    
    @task
    def grammys_extraction():
        return extract_grammys()
    
    grammys_raw_data = grammys_extraction()
    
    @task
    def musicbrainz_extraction():
        return extract_musicbrainz()
    
    musicbrainz_raw_data = musicbrainz_extraction()
    
    @task
    def spotify_transformation(raw_data):
        return transform_spotify(raw_data)
    
    spotify_data = spotify_transformation(spotify_raw_data)
    
    @task
    def grammys_transformation(raw_data):
        return transform_grammys(raw_data)
    
    grammys_data = grammys_transformation(grammys_raw_data)
    
    @task
    def musicbrainz_transformation(raw_data):
        return transform_musicbrainz(raw_data)
    
    musicbrainz_data = musicbrainz_transformation(musicbrainz_raw_data)
    
    @task
    def data_merging(spotify_df, grammys_df, musicbrainz_df):
        return merge_transformed_data(spotify_df, grammys_df, musicbrainz_df)
    
    merged_data = data_merging(spotify_data, grammys_data, musicbrainz_data)
    
    @task
    def data_loading(merged_data):
        load_data_to_database(merged_data)
    
    @task
    def data_storing(merged_data):
        store_data(merged_data)
    
    data_loading(merged_data)
    data_storing(merged_data)

etl_dag = etl_dag()
