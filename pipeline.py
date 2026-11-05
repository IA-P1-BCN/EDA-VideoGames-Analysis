import pandas as pd
import numpy as np
import os

def run_pipeline(input_path='dato.csv', output_path='dato_cleaned.csv'):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
        
    print("Loading raw dataset...")
    df = pd.read_csv(input_path)
    
    print("Applying data cleaning...")
    df = df.drop_duplicates()
    
    if 'Publisher' in df.columns:
        df = df.dropna(subset=['Publisher'])
        
    sales_cols = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    for col in sales_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')
            
    print("Optimizing memory usage...")
    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = df[col].astype(np.float32)
        
    df['NA_EU_Share'] = (df['NA_Sales'] + df['EU_Sales']) / df['Global_Sales']
    
    df.to_csv(output_path, index=False)
    print(f"Pipeline executed successfully. Cleaned file saved to '{output_path}'.")

if __name__ == '__main__':
    run_pipeline()