from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_predict():
    response = client.post(
        "/predict",
        json={"hours_studied": 4.5}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["hours_studied"] == 4.5
    assert data["predicted_score"] == 64.88