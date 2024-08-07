import json
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@patch('app.models.gemini_model.GeminiModel.analyze_meal')
def test_analyze_meal(mock_analyze_meal):
    mock_response = """```json
    {
        "food_name": "Breakfast Burrito",
        "total_calories": 540,
        "calories_per_ingredient": {
            "eggs": 140,
            "tortilla": 100,
            "cheese": 100,
            "sausage": 100
        }
    }
    ```"""
    mock_analyze_meal.return_value = mock_response

    with open("tests/test_image.jpg", "rb") as image_file:
        response = client.post("/meals/analyze_meal", files={"file": ("test_image.jpg", image_file, "image/jpeg")})
    assert response.status_code == 200
    data = response.json()
    assert data["food_name"] == "Breakfast Burrito"
    assert data["total_calories"] == 540
    assert "eggs" in data["calories_per_ingredient"]
    assert data["calories_per_ingredient"]["eggs"] == 140
