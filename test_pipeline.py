import numpy as np
import pandas as pd
from pipeline import clean_data, engineer_features


def test_clean_data_removes_null_publishers():
    raw_data = pd.DataFrame(
        {
            'Name': ['Game A', 'Game B'],
            'Platform': ['PS4', 'XOne'],
            'Genre': ['Action', 'Sports'],
            'Publisher': ['Nintendo', np.nan],
            'NA_Sales': [1.0, 0.5],
            'EU_Sales': [0.5, 0.2],
            'Global_Sales': [2.0, 1.0],
        }
    )
    cleaned = clean_data(raw_data)
    assert len(cleaned) == 1
    assert cleaned.iloc[0]['Publisher'] == 'Nintendo'


def test_engineer_features_na_eu_share():
    clean_data_df = pd.DataFrame(
        {
            'NA_Sales': [2.0, 0.0],
            'EU_Sales': [1.0, 0.0],
            'Global_Sales': [4.0, 0.0],
        }
    )
    engineered = engineer_features(clean_data_df)
    assert engineered.iloc[0]['NA_EU_Share'] == 0.75
    assert engineered.iloc[1]['NA_EU_Share'] == 0.0

def test_clean_data_removes_duplicates():
    raw_data = pd.DataFrame(
        {
            'Name': ['Game A', 'Game A'],
            'Platform': ['PS4', 'PS4'],
            'Genre': ['Action', 'Action'],
            'Publisher': ['Nintendo', 'Nintendo'],
            'NA_Sales': [1.0, 1.0],
            'EU_Sales': [0.5, 0.5],
            'Global_Sales': [2.0, 2.0],
        }
    )

    cleaned = clean_data(raw_data)

    assert len(cleaned) == 1
    assert cleaned.duplicated().sum() == 0    