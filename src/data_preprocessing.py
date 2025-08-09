import pandas as pd

def load_data(filepath):
    """Load CSV file into a Pandas DataFrame."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Remove nulls and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df
