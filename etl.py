# %%

# Extract: Importiert das requests-Modul, um HTTP-Anfragen an Webseiten/APIs zu senden
# Transform: Pandas
# Load: SQLalchemy um Daten in SQL-Datenbank zu laden

import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. Step: Extract
def extract() -> dict:
    """This API extracts data from http://universities.hipolabs.com"""
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data

# 2. Step: Transform
def transform(data: dict) -> pd.DataFrame:
    """Transforms the dataset into desired structure and filters"""

# macht aus JSON-Daten eine Tabelle
    df = pd.DataFrame(data)
    print(f"Total Number of universities from API: {len(data)}")

    df = df[df["name"].str.contains("California")]
    print(f"Number of universities in California: {len(df)}")

    # Spalte domains und web_pages von Liste in String umwandeln
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df = df.reset_index(drop=True)

    return df[["domains", "country", "web_pages", "name"]]

# 3. Step: Load
def load(df:pd.DataFrame)-> None:
    """ Loads data into a sqllite database"""
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    df.to_sql('cal_uni', disk_engine, if_exists='replace')

# Hauptteil

    data = extract()

    df = transform(data)

    load(df)

  
# %%

