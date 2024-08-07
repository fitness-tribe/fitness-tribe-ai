import json
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@patch('app.models.gemini_model.GeminiModel.recommend_workouts')
def test_recommend_workouts(mock_recommend_workouts):
    mock_response = """```json
    {
        "warmup": {"description": "Dynamic Stretching", "duration": 5},
        "cardio": {"description": "Moderate-Intensity Steady State", "duration": 30},
        "sessions_per_week": 3,
        "workout_sessions": [
            {
                "exercises": [
                    {"exercise": "Bench Press", "sets": 3, "reps": "8-12", "rest": 60},
                    {"exercise": "Squat", "sets": 3, "reps": "8-12", "rest": 60}
                ]
            },
            {
                "exercises": [
                    {"exercise": "Overhead Press", "sets": 3, "reps": "8-12", "rest": 60},
                    {"exercise": "Barbell Row", "sets": 3, "reps": "8-12", "rest": 60}
                ]
            },
            {
                "exercises": [
                    {"exercise": "Triceps Pushdown", "sets": 3, "reps": "8-12", "rest": 60},
                    {"exercise": "Biceps Curl", "sets": 3, "reps": "8-12", "rest": 60}
                ]
            }
        ],
        "cooldown": {"description": "Static Stretching", "duration": 5}
    }
    ```"""
    mock_recommend_workouts.return_value = mock_response

    profile_data = {
        "weight": 70,
        "height": 175,
        "age": 25,
        "sex": "male",
        "goal": "bulking"
    }
    response = client.post("/workouts/recommend_workouts", json=profile_data)
    assert response.status_code == 200
    data = response.json()
    assert data["warmup"]["description"] == "Dynamic Stretching"
    assert data["warmup"]["duration"] == 5
    assert data["cardio"]["description"] == "Moderate-Intensity Steady State"
    assert data["cardio"]["duration"] == 30
    assert data["sessions_per_week"] == 3
    assert len(data["workout_sessions"]) == 3
    assert data["workout_sessions"][0]["exercises"][0]["name"] == "Bench Press"
    assert data["cooldown"]["description"] == "Static Stretching"
    assert data["cooldown"]["duration"] == 5
