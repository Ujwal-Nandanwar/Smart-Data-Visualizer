import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # Remove duplicate rows and droping column with missing values
    df = df.drop_duplicates()

    threshold = len(df) * 0.5
    df = df.dropna(thresh=threshold, axis=1)

    # Fill remaining numeric NaN with mean, categorical with mode
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")

    return df
