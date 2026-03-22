from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

def compare_actual_vs_predicted(df, ticker):

    # Determine x-axis
    x_axis = df['Date']

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(x_axis, df['Close'], label='Actual Close', color='blue')
    plt.plot(x_axis, df['Predicted_Close'], label='Predicted Close', color='orange')
    plt.title(f'{ticker} - Actual vs Predicted Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'reports/figures/{ticker.replace(".", "_")}_actual_vs_predicted.png')
    plt.show()

    # Calculate metrics
    mae = mean_absolute_error(df['Close'], df['Predicted_Close'])
    mse = mean_squared_error(df['Close'], df['Predicted_Close'])
    rmse = np.sqrt(mse)

    print(f"[METRICS] MAE: {mae:.2f}")
    print(f"[METRICS] MSE: {mse:.2f}")
    print(f"[METRICS] RMSE: {rmse:.2f}")

