import pandas as pd

def clean_and_transform_data(df):

    df["SalesPerQuantity"] = df["Sales"] / df["Quantity"]

    
    df = df[df["Sales"] > 500]

  
    df["OrderMonth"] = pd.to_datetime(df["OrderDate"]).dt.month

    return df
