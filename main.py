import argparse
import os

from src.forecast_next_5_days import forcast_next_5_days
from src.data_loader import download_stock_data
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.predict import  predict_with_signal
from src.visualize import plot_stock_prices
from src.compare_actual_vs_predicted import compare_actual_vs_predicted
# from src.forcecast_next_days import forecast_next_days


def main(ticker: str, period: str, interval: str):
    print(f"[INFO] Downloading data for {ticker}...")
    os.makedirs("data/raw", exist_ok=True)
    try:
        df = download_stock_data(ticker, period, interval)
        df.to_csv(f"data/{ticker.replace('.', '_')}.csv", index=False)
        print(f"[INFO] Data downloaded and saved to data/{ticker.replace('.', '_')}.csv")
    except Exception as e:
        print(f"[ERROR] Failed to download data: {e}")
        return


    print("[INFO] Preprocessing data...")
    os.makedirs("data/processed", exist_ok=True)
    df_processed = preprocess_data(df)
    df_processed.to_csv(f"data/processed/{ticker.replace('.', '_')}_processed.csv", index=False)
    print(f"[INFO] Data preprocessed and saved to data/processed/{ticker.replace('.', '_')}_processed.csv")


    print("[INFO] Training model...")
    model_path = f"models/{ticker.replace('.', '_')}_model.joblib"
    train_model(df_processed, save_path=model_path)

    print("[INFO] Making predictions...")
    os.makedirs("reports", exist_ok=True)
    predictions, signal = predict_with_signal(df_processed, model_path=model_path)
    df_processed["Predicted_Close"] = predictions
    df_processed.to_csv(f"reports/{ticker.replace('.', '_')}_with_predictions.csv", index=False)
    print(f"[RESULT] Trade Decision: {signal}")


    print("[INFO] Plotting stock prices...")
    os.makedirs('reports/figures', exist_ok=True)
    plot_stock_prices(df_processed, ticker)

    print("[INFO] Comparing Actual price vs Predicted price")


    
    compare_actual_vs_predicted(df_processed, ticker)

    print("[INFO] Forecasting next 5 days...")

    last_60 = df.tail(60).copy()
    future_preds = forcast_next_5_days(last_60, model_path)
    print(f"[RESULT] Future Predictions:\n{future_preds}")
    future_preds.to_csv(f"reports/{ticker.replace('.', '_')}_next_5_days.csv", index=False)

    print("[INFO] Pipeline complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stock Price Analysis and Prediction")
    parser.add_argument("--ticker", type=str, default="TCS.NS", help="Stock ticker symbol (e.g. TCS.NS)")
    parser.add_argument("--period", type=str, default="1y", help="Time period for historical data (e.g. 1y, 6mo, 5d)")
    parser.add_argument("--interval", type=str, default="1d", help="Data interval (e.g. 1d, 1h)")

    args = parser.parse_args()
    main(args.ticker, args.period, args.interval)
