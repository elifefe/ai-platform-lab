from fastapi import FastAPI
from pydantic import BaseModel

from model import predict_score


app = FastAPI(
    title="AI Platform Lab",
    description="My first containerized AI API",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    hours_studied: float


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(request: PredictionRequest):
    score = predict_score(request.hours_studied)

    return {
        "hours_studied": request.hours_studied,
        "predicted_score": score
    }