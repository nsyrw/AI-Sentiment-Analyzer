from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.get("/predict")

def predict(text: str):

    vec = vectorizer.transform([text])

    result = model.predict(vec)

    return {"result": result[0]}
