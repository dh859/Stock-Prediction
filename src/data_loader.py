import yfinance as yf
import pandas as pd

def download_stock_data(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)
    return df
