# 📊 Customer Churn Prediction API

## 🌍 Live API
http://44.193.80.59:8000/docs

---

## 📸 Demo

### API Swagger UI
![Swagger UI](https://raw.githubusercontent.com/PavithraRajkumar95/customer-churn-api/main/swagger.png)

### Sample input
![Sample Input](https://raw.githubusercontent.com/PavithraRajkumar95/customer-churn-api/main/sampledatainput.png)

### Prediction Example
![Prediction Output](https://raw.githubusercontent.com/PavithraRajkumar95/customer-churn-api/main/prediction.png)

---

## 🏗️ Architecture

User → FastAPI API → ML Model → Prediction Response  
           ↓  
        Docker Container → AWS EC2 Instance  

---

## 🚀 Project Overview

Customer churn is a critical problem in the telecom industry. This project builds a predictive model to identify customers who are likely to leave, helping businesses take proactive actions.

---

## 🧠 Features

- Data preprocessing pipeline  
- Feature engineering & encoding  
- Model training and evaluation  
- FastAPI-based prediction API  
- Dockerized application  
- Deployed on AWS EC2  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy, Scikit-learn  
- FastAPI  
- Docker  
- AWS EC2  

---

## 📊 Model Comparison

| Model                          | Accuracy | Recall (Churn) | Notes |
|--------------------------------|----------|----------------|------|
| Logistic Regression            | 0.81     | 0.61           | Misses many churn customers |
| Logistic Regression (Balanced) | 0.73     | 0.79 ✅        | Best at detecting churn |
| Random Forest                  | 0.79     | 0.52           | Poor recall for churn |

---

## ✅ Final Model Selection

Logistic Regression with class weights was selected as the final model.

Although it has slightly lower accuracy, it significantly improves recall for churn prediction. In a business context, identifying customers likely to churn is more important than overall accuracy, as it allows proactive retention strategies.

---

## 📈 Evaluation Strategy

- Recall was prioritized over accuracy  
- Missing a churn customer leads to revenue loss  
- False positives are acceptable in this case  
- Focus was on maximizing churn detection  

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
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the API
uvicorn app.main:app --reload
5. Open in browser
http://127.0.0.1:8000/docs

🐳 Run with Docker
Build image
docker build -t churn-api .
Run container
docker run -d -p 8000:8000 churn-api

🔮 API Usage
Endpoint
POST /predict
Sample Input
{
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "TotalCharges": 800
}
Output
{
  "churn_prediction": 1
}

## ☁️ Deployment
Dockerized application
Deployed on AWS EC2

## ⚠️ Note

Dataset is not included in this repository due to size constraints.

## 📌 Future Improvements
Add frontend dashboard
Try advanced models (XGBoost)
Add CI/CD pipeline
Improve feature engineering

## 👩‍💻 Author

Pavithra Rajkumar

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

