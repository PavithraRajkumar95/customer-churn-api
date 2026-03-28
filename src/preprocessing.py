import pandas as pd

def preprocess_input(data:dict,columns:list):
    df = pd.DataFrame([data])

    #convert bool to int(important for model)
    for col in df.select_dtypes(include=['bool']).columns:
        df[col] = df[col].astype(int)

    #Add Missing Columns
    for col in columns:
        if col not in df:
            df[col]=0

    #Ensure correct order
    df = df[columns]

    return df[columns]