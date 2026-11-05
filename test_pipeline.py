import pytest
import pandas as pd
import numpy as np

def clean_data(df):
    df = df.copy()
    df = df.drop_duplicates()
    
    if 'Publisher' in df.columns:
        df = df.dropna(subset=['Publisher'])
        
    sales_cols = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    for col in sales_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')
            
    return df

@pytest.fixture
def raw_sample_data():
    return pd.DataFrame({
        'Platform': ['Wii', 'Wii', 'NES', 'GB'],
        'Genre': ['Sports', 'Sports', 'Platform', 'Role-Playing'],
        'Publisher': ['Nintendo', 'Nintendo', np.nan, 'Nintendo'],
        'NA_Sales': ['41,49', '41,49', '29.08', '11.27'],
        'EU_Sales': ['29.02', '29.02', '3.58', '8.89'],
        'JP_Sales': ['3.77', '3.77', '6.81', '10.22'],
        'Other_Sales': ['8.46', '8.46', '0.77', '1.00'],
        'Global_Sales': ['82.74', '82.74', '40.24', '31.37']
    })

def test_drop_duplicates(raw_sample_data):
    df_no_dups = raw_sample_data.drop_duplicates()
    assert len(df_no_dups) == 3

def test_drop_null_publisher(raw_sample_data):
    cleaned = clean_data(raw_sample_data)
    assert cleaned['Publisher'].isnull().sum() == 0

def test_numeric_sales_conversion(raw_sample_data):
    cleaned = clean_data(raw_sample_data)
    assert pd.api.types.is_float_dtype(cleaned['Global_Sales'])