import numpy as np
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load raw dataset from CSV file."""
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean missing values, remove duplicates and optimize memory."""

    df_clean = df.dropna(subset=['Publisher']).copy()

    df_clean = df_clean.drop_duplicates()

    sales_cols = [
        'NA_Sales',
        'EU_Sales',
        'JP_Sales',
        'Other_Sales',
        'Global_Sales',
    ]

    for col in sales_cols:
        if col in df_clean.columns:
            df_clean[col] = (
                df_clean[col]
                .astype('string')
                .str.replace(',', '.', regex=False)
            )

            df_clean[col] = pd.to_numeric(
                df_clean[col], errors='coerce'
            ).astype('float32')

    for col in ['Platform', 'Genre', 'Publisher']:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype('category')

    return df_clean

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Safely calculate Western market share and sales categories."""
    df_engineered = df.copy()

    df_engineered['NA_EU_Share'] = np.where(
        df_engineered['Global_Sales'] > 0,
        (df_engineered['NA_Sales'] + df_engineered['EU_Sales'])
        / df_engineered['Global_Sales'],
        0.0,
    )
    df_engineered['NA_EU_Share'] = (
        df_engineered['NA_EU_Share']
        .replace([np.inf, -np.inf], np.nan)
        .fillna(0.0)
    )

    bins = [-np.inf, 0.1, 0.5, 2.0, np.inf]
    labels = [
        'Niche (<0.1M)',
        'Moderate (0.1M-0.5M)',
        'Major (0.5M-2M)',
        'Blockbuster (>2M)',
    ]
    df_engineered['Sales_Category'] = pd.cut(
        df_engineered['Global_Sales'], bins=bins, labels=labels
    )

    return df_engineered


def run_pipeline(input_path: str, output_path: str) -> pd.DataFrame:
    """Execute complete data processing pipeline."""
    df_raw = load_data(input_path)
    df_clean = clean_data(df_raw)
    df_final = engineer_features(df_clean)
    df_final.to_csv(output_path, index=False)
    return df_final


if __name__ == '__main__':
    run_pipeline('dato.csv', 'dato_cleaned.csv')