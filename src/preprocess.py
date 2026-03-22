import pandas as pd
from src.create_features import create_features


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = create_features(df)
    return df
