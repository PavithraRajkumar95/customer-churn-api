# 📊 Customer Churn Prediction API

An end-to-end Machine Learning project that predicts whether a customer will churn or not. The project includes data preprocessing, model training, and deployment using FastAPI and Docker.

---

## 🚀 Project Overview

Customer churn is a critical problem in the telecom industry. This project builds a predictive model to identify customers who are likely to leave, helping businesses take proactive actions.

---

## 🧠 Features

- Data preprocessing pipeline
- Feature engineering & encoding
- Model training (Linear, Ridge, Lasso)
- Model evaluation
- FastAPI-based prediction API
- Dockerized application
- Ready for cloud deployment (AWS)

---

## 🗂️ Project Structure
customer-churn-project/
│
├── app/
│ └── main.py # FastAPI app
│
├── src/
│ ├── preprocessing.py # Data preprocessing
│ ├── train.py # Model training
│ └── predict.py # Prediction logic
│
├── model/
│ ├── churn_model.pkl # Trained model
│ └── columns.json # Feature columns
│
├── data/
│ └── telco_customer_churn.csv
│
├── notebooks/
│ └── eda1.ipynb # Exploratory Data Analysis
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/PavithraRajkumar95/customer-churn-api.git
cd customer-churn-api

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

### 3.Install dependencies

pip install -r requirements.txt

### 4. Run the API

uvicorn app.main:app --reload

### 5. Open in browser

http://127.0.0.1:8000/docs

🐳 Run with Docker
Build image

docker build -t churn-api .

Run container

docker run -d -p 8000:8000 churn-api

🔮 API Usage
Endpoint:
POST /predict

Sample Input:
{
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "TotalCharges": 800,
  ...
}
Output:
{
  "churn_prediction": 1
}

📈 Models Used
Linear Regression
Ridge Regression
Lasso Regression

Ridge Regression was selected for better stability and handling multicollinearity.

🧪 Model Evaluation
MAE (Mean Absolute Error)
Feature importance analysis
Residual distribution checks

☁️ Deployment
Dockerized application
Dockerized application

Deployable on AWS EC2
📌 Future Improvements
Add frontend dashboard
Use advanced models (XGBoost, Random Forest)
Add CI/CD pipeline
Improve feature engineering


👩‍💻 Author

Pavithra Rajkumar

⭐ If you like this project

Give it a star ⭐ on GitHub!


---

