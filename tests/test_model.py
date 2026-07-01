# test_model.py

import joblib
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_model_prediction():
    model = joblib.load("model.pkl")

    result = model.predict([[10]])

    assert result[0] == 20


def test_invalid_input():

    response = client.post(
        "/predict",
        json={"value": "hello"}
    )

    assert response.status_code == 422