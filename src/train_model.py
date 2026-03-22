import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

def train_model(df, target_col='Close', save_path='models/linear_regression.joblib'):
    
    if not os.path.exists('models'):
        os.makedirs('models')

    X = df[['MA10', 'MA50', 'Return']]
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, save_path)
    print(f"Model saved to {save_path}")
