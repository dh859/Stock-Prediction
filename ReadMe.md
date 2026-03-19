# Team Members
- Ashutosh Anand (23071003244)
- Deependra Yadav (23071003289)
- Dhruv Rathour (2307100230300)

# 📈 Stock Price Prediction Using Machine Learning

This project predicts future stock prices using past historical data. It focuses on Indian stocks (e.g., TCS) and uses simple machine learning models to make predictions based on the stock's closing prices.

---

## 🔍 Objective

The goal of this project is to:
- Collect and analyze past stock price data (TCS.NS from NSE)
- Train a machine learning model (Linear Regression)
- Predict future closing prices
- Visualize the actual vs predicted prices
- Understand market conditions using basic indicators

---

## 🧠 Technologies Used

- **Python 3.8+**
- **Pandas** – for data handling
- **NumPy** – for numerical operations
- **Matplotlib** – for plotting
- **scikit-learn** – for building ML models
- **yfinance** – for downloading historical stock data
- **joblib** – for saving the model

---

## 🗂️ Project Structure

The project is structured as follows:

stock-analysis-project/
│
├── data/
│   ├── raw/                # Original downloaded data (if any)
│   └── processed/          # Cleaned/processed datasets
│
├── notebooks/
│   └── stock_analysis.ipynb # Your Jupyter notebook
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # Functions to load/download data
│   ├── preprocess.py       # Data cleaning and feature engineering
│   ├── train_model.py      # Model training scripts
│   ├── predict.py          # Prediction and evaluation scripts
│   └── visualize.py        # Visualization functions
│
├── models/
│   └── linear_regression.joblib # Saved models
│
├── reports/
│   └── figures/            # Generated plots and figures
│   └── summary.md          # Project summary or findings
│
├── requirements.txt        # List of dependencies
├── README.md               # Project overview and instructions
└── .gitignore              # Files/folders to ignore in git

## Run the project

python main.py

## Open Jupyter Notebook for visual analysis

jupyter notebook notebooks/stock_analysis.ipynb

## 📊 Example Output
Line plot comparing actual vs predicted stock prices

Saved CSV of predictions in outputs/predictions.csv

Model saved in models/model.pkl

## ⚙️ Model Used
Linear Regression

Inputs: Previous day's closing price

Output: Predicted next day's closing price

Evaluation: Mean Squared Error (MSE)

## 📈 Data Source

Data is downloaded using the yfinance Python package using ticker: TCS.NS

