import matplotlib.pyplot as plt

def plot_stock_prices(df, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['MA10'], label='MA10')
    plt.plot(df['Date'], df['MA50'], label='MA50')
    plt.title(f'{ticker} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('reports/figures/price_plot.png')
    plt.show()
