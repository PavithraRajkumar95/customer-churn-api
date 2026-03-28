import pandas as pd
import pickle
import json
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train_model(df):
    x = df.drop('Churn Value', axis=1)
    y = df['Churn Value']

    x_train,x_test,y_train,y_test=train_test_split(
        x,y,test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000,class_weight='balanced')
    model.fit(x_train,y_train)
    return model,x.columns

def save_model(model,columns):

    with open("model/churn_model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("model/columns.json","w") as f:
        json.dump(list(columns), f)