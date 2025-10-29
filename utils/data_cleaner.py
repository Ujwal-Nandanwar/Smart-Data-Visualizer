import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data cleaning on the DataFrame."""
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    for col in df.columns:
        if df[col].dtype == 'O':  # Object (string) type
            df[col] = df[col].fillna("Unknown")
        else:  # Numeric type
            df[col] = df[col].fillna(df[col].mean())

    # Remove empty columns
    df = df.dropna(axis=1, how='all')

    # Reset index
    df = df.reset_index(drop=True)

    return df
