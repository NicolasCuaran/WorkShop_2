# WorkShop_2
 This repo is for the Workshop#2 in ETL

This project implements an **Extract, Transform, Load (ETL)** pipeline utilizing **Apache Airflow** in **Docker** for task orchestration and **Python** as the primary programming language. Data is collected from various sources, including the essential integration with the **MusicBrainz API** to retrieve detailed artist information, then processed and loaded into a database. The processed data is subsequently utilized to generate reports and visualizations, for instance, using **Power BI**.

## Objectives

- **Extraction:**

  - **Datasets:**
    - **Spotify Data:** A CSV dataset containing song metadata and audio features.
    - **Grammy Awards Data:** Database containing information on Grammy nominees and winners.
  - **MusicBrainz API:** Essential artist information such as unique identifiers and additional metadata retrieved through the API.

- **Transformation:**
  Conduct exploratory analysis, data cleaning, and data merging via notebooks and Apache Airflow orchestrated tasks.

- **Load:**
  Store processed data into a database (e.g., PostgreSQL) and export relevant CSV files to external platforms (e.g., Google Drive) for further analysis.

---

## 📊 Datasets Overview

The analysis primarily relies on two datasets: **`spotify_dataset.csv`** and **`the_grammy_awards.csv`**, complemented by additional artist data from the **MusicBrainz API**. These datasets allow for in-depth exploration of music trends, track feature comparisons, and insights into correlations between musical attributes and Grammy award recognition.

---

### 🎧 Spotify Dataset (`spotify_dataset.csv`)

This dataset contains extensive information about Spotify tracks, each row representing a unique track with its metadata and musical attributes.

**Notable Columns:**

- `Unnamed: 0`: General dataset index.
- `track_id`: Unique Spotify track identifier.
- `artists`: Artist(s) associated with the track.
- `album_name`: Album title.
- `track_name`: Song title.
- `popularity`: Popularity rating (0-100).
- `duration_ms`: Length in milliseconds.
- `danceability`: Dance suitability.
- `energy`: Track intensity and liveliness.
- `key`: Musical key indicator.
- `loudness`: Track loudness in decibels.
- `mode`: Major (1) or minor (0) key.
- `explicit`: Indicates explicit content.
- `tempo`: Beats per minute.
- `valence`: Musical positivity.
- `time_signature`: Predominant time signature.
- `track_genre`: Associated genre.

---

### 🏆 Grammy Awards Dataset (`the_grammy_awards.csv`)

Contains Grammy Award nominees and winners, each row corresponding to a nomination event.

**Notable Columns:**

- `year`: Grammy award year.
- `title`: Event title.
- `published_at`: Publication date of event details.
- `category`: Award category.
- `nominee`: Nominated song/album.
- `artist`: Associated artist(s).
- `workers`: Involved contributors (producers, engineers).
- `img`: URL to relevant images.
- `winner`: Indicates award-winning nominee (True/False).

---

### 🎼 MusicBrainz API

The project incorporates additional artist information from the MusicBrainz API:

**Notable Columns:**

- `artist`: Artist’s name.
- `country`: Origin country.
- `type`: Artist category (Person, Group).
- `disambiguation`: Additional distinguishing information.
- `life_begin`: Artist's birth/start date.
- `life_end`: Artist's death/end date.

## Technologies and Tools

- **Language:** Python 3.10+ ([Python](https://www.python.org/downloads/))
- **Orchestration:** Apache Airflow ([Documentation](https://airflow.apache.org/docs/))
- **Data Handling:** pandas ([Documentation](https://pandas.pydata.org/))
- **Database:** PostgreSQL ([PostgreSQL](https://www.postgresql.org/download/))
- **Database Connection:** SQLAlchemy ([Documentation](https://docs.sqlalchemy.org/))
- **Visualization:** Power BI Desktop ([Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi/desktop))
- **Development Environment:** Jupyter Notebook in VS Code ([Guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks))
- **Cloud Storage:** Google Drive via PyDrive2 ([PyDrive2](https://docs.iterative.ai/PyDrive2/))
- **API Integration:** MusicBrainz ([Documentation](https://musicbrainz.org/doc/MusicBrainz_API))
- **Docker:** Docker Desktop ([Docker](https://www.docker.com/products/docker-desktop/))

## Project Structure

```
├── airflow/
│   ├── dags/                     
│   ├── tasks/                   
│   
├── data/
│   ├── spotify_dataset.csv        
│   └── the_grammy_awards.csv      
│
├── drive_config/                  
│
├── notebooks/
│   ├── 001_extraccion.ipynb   
│   ├── 002_EDA_Spotify.ipynb      
│   ├── 003_EDA_Grammys.ipynb       
│   └── 004_EDA_extract.ipynb       
│
├── src/
├── database/
│   ├──.env
│   ├── db_operations              
├── extract/
│   ├── api_extract.py                
│   ├── grammys_extract.py         
│   └── spotify_extract.py         
├── load_store/
│   ├── load.py                    
│   └── store.py                   
├── transform/
│   ├── api_transform.py           
│   ├── grammys_transform.py       
│   ├── spotify_transform.py      
│   └── merge.py                   
├── .gitignore                     
├── .env                         
├── requirements.txt
├── docker-compose.yml
├── dockerfile
```
## Steps to Activate the Google Drive API and Obtain the `client_secrets.json` File

### 1. Create a Project in Google Cloud Console

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the **Projects** dropdown menu in the upper-left corner and select **New Project**.
3. Specify the project name and select a location.
4. Click **Create**.

---
### 2. Enable the Google Drive API

1. With the project selected, go to the left navigation menu and select **API & Services** > **Library**.
2. In the search field, type **Google Drive API**.
3. Select **Google Drive API** from the results.
4. Click **Enable**.
---

### 3. Create OAuth 2.0 Credentials

1. Once the API is enabled, select **Credentials** from the left-hand menu.
2. Click **Create credentials** and select **OAuth client ID**.
3. If you haven’t configured the OAuth consent screen yet, you will be prompted to do so:
   
    - Click on **Configure consent screen**.
    - Select **External** as the user type and click **Create**.
    - Fill in the basic information (application name, email address, etc.), then click **Save and Continue** until the configuration is complete.
  
---
5. After configuring the consent screen, select **Desktop app** as the application type when creating credentials.
6. Click **Create**.
---
### 4. Download the `client_secrets.json` File

1. After creating the OAuth client ID, you will see an option to **Download** the credentials file.
2. Download the `client_secrets.json` file and save it to your project directory.
---
### 6. Using the `client_secrets.json` File

The `client_secrets.json` file is necessary to authenticate your application with Google Drive using OAuth 2.0. This file should be used when configuring your application's authentication flow.

### 7. Run Your Application

Depending on the library you're using, configure your application to load the `client_secrets.json` file and follow the OAuth 2.0 authentication flow.

## Setup and Execution

### 1. Repository Cloning

```bash
git clone https://github.com/NicolasCuaran/WorkShop_2.git
cd Workshop_2
```
### 2. Environment Variables

Variables

Create a `.env` file:

```ini
DB_HOST=localhost
DB_PORT=5432
DB_USER=user
DB_PASSWORD=password
DB_NAME=db_name
AIRFLOW_UID=0
```

Create `src/database/.env`:

```ini
DB_USER=user
DB_PASSWORD=password
DB_HOST=host.docker.internal
DB_PORT=5432
DB_NAME=db_name
```
### 3. starting Docker containers

```bash
docker-compose up --build
```

## Visualization

Create dashboards in **Power BI** by connecting directly to PostgreSQL, selecting the appropriate tables, and visualizing ETL insights.

## Additional Notes

- Secure sensitive files (credentials, `.env`) properly.


