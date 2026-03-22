import pandas as pd
import joblib

def forecast_next_days(df, model_path):
    model = joblib.load(model_path)  

    features_used = ['MA10', 'MA50','Return']
    future_predictions = []
    

    if df.empty:
        raise ValueError("Feature DataFrame is empty after applying create_features. Check rolling window size or input data.")

    last_known = df.copy()[-50:]

    latest_features = last_known[features_used].tail(1)

    next_close = model.predict(latest_features)[0]

    future_predictions.append(next_close)

    return pd.DataFrame(future_predictions)


