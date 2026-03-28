from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_churn

app = FastAPI()

class CustomerData(BaseModel):
    Gender: int
    Senior_Citizen: int
    Partner: int
    Dependents: int
    Tenure_Months: int
    Phone_Service: int
    Multiple_Lines: int
    Online_Security: int
    Online_Backup: int
    Device_Protection: int
    Tech_Support: int
    Streaming_TV: int
    Streaming_Movies: int
    Paperless_Billing: int
    Monthly_Charges: float
    Total_Charges: float
    Internet_Service_Fiber_optic: int
    Internet_Service_No: int
    Contract_One_year: int
    Contract_Two_year: int
    Payment_Method_Credit_card_automatic: int
    Payment_Method_Electronic_check: int
    Payment_Method_Mailed_check: int



@app.get("/")
def home():
    return{"message":"Churn Prediction API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    result = predict_churn(data.dict())
    return {"churn_prediction": result}

