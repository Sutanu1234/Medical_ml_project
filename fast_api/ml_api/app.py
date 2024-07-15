from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware

# Load the model
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

app = FastAPI()

# Set up CORS middleware
origins = ["http://localhost:3000/predict"]  # Adjust as necessary for your use case

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/predict")
async def predict(data: DiabetesInput):
    input_data = np.array([[
        data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness,
        data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age
    ]])
    
    print("Input data:", input_data)
    
    input_data_df = pd.DataFrame(input_data, columns=[
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
    ])
    std_data = scaler.transform(input_data_df)
    
    print("Standardized data:", std_data)
    
    prediction = model.predict(std_data)
    
    print("Prediction:", prediction)
    
    return {"prediction": int(prediction[0])}