import pickle
import json
import os
from src.preprocessing import preprocess_input

#load model + columns
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model","churn_model.pkl")
columns_path = os.path.join(BASE_DIR,"model", "columns.json")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "r") as f:
    columns = json.load(f)

def predict_churn(data:dict):
    processed_data = preprocess_input(data,columns)
    prediction = model.predict(processed_data)[0]

    return int(prediction)