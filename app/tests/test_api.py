from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_api():
    response = client.get(
        "/fizzbuzz",
        params={
            "int1": 3,
            "int2": 5,
            "limit": 15,
            "str1": "Fizz",
            "str2": "Buzz"
        }
    )

    assert response.status_code == 200
    assert "result" in response.json()