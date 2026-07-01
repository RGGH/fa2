# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


model = joblib.load("model.pkl")


class Input(BaseModel):
    value: float


@app.post("/predict")
def predict(data: Input):
    prediction = model.predict([[data.value]])

    return {
        "prediction": prediction[0]
    }


@app.get("/")
def index():
    return FileResponse("index.html")
