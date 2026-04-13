from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("models/orl_rf_model.pkl")

app = FastAPI(title="ORL IA API", version="1.0")

class Patient(BaseModel):
    age: int
    cancer: int
    larynx: int
    parotide: int
    ethmoide: int

@app.get("/")
def home():
    return {"message": "API ORL IA active 🚀"}

@app.post("/predict")
def predict_patient(data: Patient):
    df = pd.DataFrame([data.dict()])
    df = df[["age", "cancer", "larynx", "parotide", "ethmoide"]]

    prediction = model.predict(df)[0]

    if prediction == "Malin":
        status = "🚨 URGENT"
    elif prediction == "Suspect":
        status = "⚠️ SURVEILLANCE"
    else:
        status = "✅ BENIN"

    return {
        "prediction": prediction,
        "status": status
    }
