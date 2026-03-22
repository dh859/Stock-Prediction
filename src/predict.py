import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error

def predict(df: pd.DataFrame, model_path='models/linear_regression.joblib'):
    model = joblib.load(model_path)
    X = df[['MA10', 'MA50', 'Return']]
    y_true = df['Close']
    y_pred = model.predict(X)
    mse = mean_squared_error(y_true, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")
    return y_pred


def check_buy_signal(df: pd.DataFrame) -> str:
    """
    Simple rule-based strategy:
    - BUY if MA10 crosses above MA50
    - SELL if MA10 crosses below MA50
    - HOLD otherwise
    """
    if df['MA10'].iloc[-1] > df['MA50'].iloc[-1] and df['MA10'].iloc[-2] <= df['MA50'].iloc[-2]:
        return "BUY ✅ (Bullish crossover)"
    elif df['MA10'].iloc[-1] > df['MA50'].iloc[-1]:
        return "BUY (still above MA50)"
    else:
        return "HOLD ❌ (No bullish crossover)"

# After predictions
def predict_with_signal(df: pd.DataFrame, model_path='models/linear_regression.joblib'):
    predictions = predict(df, model_path)
    signal = check_buy_signal(df)
    # print(f"Trade Signal: {signal}")
    return predictions, signal
