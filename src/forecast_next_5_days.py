# import numpy as np
# import pandas as pd
# import joblib

# def forcast_next_5_days(last_60_df: pd.DataFrame, model_path: str) -> pd.DataFrame:
    
#     model = joblib.load(model_path)

#     predictions = []
#     temp_df = last_60_df.copy().reset_index(drop=True)

#     for _ in range(5):
      
#         temp_df['MA10'] = temp_df['Close'].rolling(window=10).mean()
#         temp_df['MA50'] = temp_df['Close'].rolling(window=50).mean()
#         temp_df['Return'] = temp_df['Close'].pct_change()

#         last_row = temp_df.iloc[-1]

#         print(f"[DEBUG] Last Row: {last_row}")

        
#         try:
#             ma10 = float(last_row['MA10'])
#             ma50 = float(last_row['MA50'])
#             ret = float(last_row['Return'])
#         except (TypeError, ValueError):
#             print("[WARN] Skipping prediction due to invalid feature values.")
#             predictions.append(np.nan)
#             new_close = temp_df['Close'].iloc[-1]
#             temp_df = pd.concat([temp_df, pd.DataFrame([{'Close': new_close}])], ignore_index=True)
#             continue

     
#         if any(pd.isna([ma10, ma50, ret])):
#             print("[WARN] Skipping prediction due to NaNs in features.")
#             predictions.append(np.nan)
#             new_close = temp_df['Close'].iloc[-1]
#             print("[DEBUG] New Close(columns):",new_close)
            
        
#         else:
#             # Make prediction
#             feature_row = np.array([[ma10, ma50, ret]])  # shape (1, 3)
#             predicted_close = float(model.predict(feature_row).item())
#             print(f"[DEBUG] New Close: {predicted_close}")
#             predictions.append(predicted_close)
#             new_close = predicted_close

        
#         temp_df = pd.concat([temp_df, pd.DataFrame([{'Close': new_close}])], ignore_index=True)

#     return pd.DataFrame({'Day': range(1, 6), 'Predicted_Close': predictions})

import numpy as np
import pandas as pd
import joblib

def forcast_next_5_days(last_60_df: pd.DataFrame, model_path: str) -> pd.DataFrame:
    
    model = joblib.load(model_path)

 
    if isinstance(last_60_df.columns, pd.MultiIndex):
        last_60_df.columns = ['_'.join(col).strip() for col in last_60_df.columns]


    close_col = next((col for col in last_60_df.columns if 'Close' in col), None)
    if close_col is None:
        raise ValueError("No 'Close' column found.")
    
    base_close = last_60_df[close_col].tolist()


    predicted_close_list = []

    for day in range(5):
       
        working_close = base_close + predicted_close_list
        temp_df = pd.DataFrame({'Close': working_close})

    
        temp_df['MA10'] = temp_df['Close'].rolling(window=10).mean()
        temp_df['MA50'] = temp_df['Close'].rolling(window=50).mean()
        temp_df['Return'] = temp_df['Close'].pct_change()

       
        last_row = temp_df.iloc[-1]

        try:
            ma10 = float(last_row['MA10'])
            ma50 = float(last_row['MA50'])
            ret = float(last_row['Return'])
        except (TypeError, ValueError):
            print(f"[WARN] Day {day+1}: Invalid feature values. Skipping.")
            predicted_close_list.append(np.nan)
            continue

        if any(pd.isna([ma10, ma50, ret])):
            print(f"[WARN] Day {day+1}: NaN in features. Skipping.")
            predicted_close_list.append(np.nan)
            continue

        feature_row = np.array([[ma10, ma50, ret]])
        predicted_close = float(model.predict(feature_row).item())
        print(f"[DEBUG] Day {day+1}: Predicted Close = {predicted_close}")
        predicted_close_list.append(predicted_close)

    return pd.DataFrame({
        'Day': range(1, 6),
        'Predicted_Close': predicted_close_list
    })
