import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

def transforming_api_data(df_api):
    """
    Applies transformations to the API DataFrame.

    - Fills missing values in 'country', 'gender', and 'type'.
    - Drops rows with missing 'artist_name'.
    - Standardizes 'type' to title case.
    """
    try:
        logging.info(f"Starting API data transformation. Initial DataFrame shape: {df_api.shape}")
        
        df_api['country'] = df_api['country'].fillna("unknown")
        df_api = df_api.dropna(subset=['artist_name'])
        df_api['gender'] = df_api['gender'].fillna('unspecified')
        df_api['type'] = df_api['type'].fillna('Other')
        df_api['type'] = df_api['type'].str.title()
        
        logging.info(f"API data transformation complete. Final DataFrame shape: {df_api.shape}")
        return df_api

    except Exception as e:
        logging.error(f"An error occurred during the API data transformation: {e}")
        return pd.DataFrame()
