import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.reset_index(drop=True, inplace=True)
    
    df['Return'] = df['Close'].pct_change()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    # df['Volatility'] = df['Return'].rolling(window=10).std()

    print("[DEBUG] After features:")
    print(df.tail(5))
    print("[DEBUG] NaN counts:")
    print(df.isna().sum())

    df = df.dropna()

    return df
