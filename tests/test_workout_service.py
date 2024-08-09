import json
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.schemas.workout import ProfileData

client = TestClient(app)


class TestWorkoutService:
    @patch("app.models.gemini_model.GeminiModel.generate_workout_plan")
    def test_generate_workout_plan(self, mock_generate_workout_plan):
        # Mock response from the Gemini API
        mock_response = {
            "warmup": {
                "description": "Light cardio, such as jogging or jumping jacks, followed by dynamic stretches like arm circles, leg swings, and torso twists.",
                "duration": 5,
            },
            "cardio": {
                "description": "Optional: 15-20 minutes of moderate-intensity cardio, like running, cycling, or swimming, after each workout.",
                "duration": 20,
            },
            "sessions_per_week": 4,
            "workout_sessions": [
                {
                    "exercises": [
                        {
                            "name": "Barbell Bench Press",
                            "sets": 4,
                            "reps": "8-12",
                            "rest": 60,
                        },
                        {
                            "name": "Barbell Squat",
                            "sets": 4,
                            "reps": "8-12",
                            "rest": 60,
                        },
                        {
                            "name": "Barbell Deadlift",
                            "sets": 1,
                            "reps": "5-8",
                            "rest": 120,
                        },
                        {
                            "name": "Dumbbell Rows",
                            "sets": 3,
                            "reps": "10-15",
                            "rest": 45,
                        },
                        {
                            "name": "Overhead Press",
                            "sets": 3,
                            "reps": "10-15",
                            "rest": 45,
                        },
                    ]
                },
                {
                    "exercises": [
                        {
                            "name": "Dumbbell Bench Press",
                            "sets": 4,
                            "reps": "8-12",
                            "rest": 60,
                        },
                        {"name": "Leg Press", "sets": 4, "reps": "10-15", "rest": 45},
                        {"name": "Pull-ups", "sets": 3, "reps": "8-12", "rest": 60},
                        {
                            "name": "Dumbbell Shoulder Press",
                            "sets": 3,
                            "reps": "10-15",
                            "rest": 45,
                        },
                        {
                            "name": "Dumbbell Bicep Curls",
                            "sets": 3,
                            "reps": "10-15",
                            "rest": 45,
                        },
                    ]
                },
            ],
            "cooldown": {
                "description": "Static stretches focusing on major muscle groups, holding each stretch for 30 seconds.",
                "duration": 5,
            },
        }
        mock_generate_workout_plan.return_value = json.dumps(mock_response)

        # Create a mock profile data
        profile_data = ProfileData(
            weight=70, height=175, age=25, sex="male", goal="bulking"
        ).model_dump()

        # Send a POST request to the generate workout plans endpoint
        response = client.post("/workout-plans/generate", json=profile_data)

        # Check the response status code
        assert response.status_code == 200

        # Load the response JSON data
        data = response.json()

        # Print the data for debugging purposes
        print("Response data:", json.dumps(data, indent=2))

        # Verify the structure of the response
        assert "warmup" in data
        assert data["warmup"]["description"] == mock_response["warmup"]["description"]
        assert data["warmup"]["duration"] == mock_response["warmup"]["duration"]

        assert "cardio" in data
        assert data["cardio"]["description"] == mock_response["cardio"]["description"]
        assert data["cardio"]["duration"] == mock_response["cardio"]["duration"]

        assert "sessions_per_week" in data
        assert data["sessions_per_week"] == mock_response["sessions_per_week"]

        assert "workout_sessions" in data
        assert len(data["workout_sessions"]) == len(mock_response["workout_sessions"])

        for session_index, session in enumerate(data["workout_sessions"]):
            print(
                f"Session {session_index} data: {json.dumps(session, indent=2)}"
            )  # Debugging line
            for exercise_index, exercise in enumerate(session["exercises"]):
                print(
                    f"Exercise {exercise_index} data: {json.dumps(exercise, indent=2)}"
                )  # Debugging line
                assert (
                    exercise["name"]
                    == mock_response["workout_sessions"][session_index]["exercises"][
                        exercise_index
                    ]["name"]
                )
                assert (
                    exercise["sets"]
                    == mock_response["workout_sessions"][session_index]["exercises"][
                        exercise_index
                    ]["sets"]
                )
                assert (
                    exercise["reps"]
                    == mock_response["workout_sessions"][session_index]["exercises"][
                        exercise_index
                    ]["reps"]
                )
                assert (
                    exercise["rest"]
                    == mock_response["workout_sessions"][session_index]["exercises"][
                        exercise_index
                    ]["rest"]
                )

        assert "cooldown" in data
        assert (
            data["cooldown"]["description"] == mock_response["cooldown"]["description"]
        )
        assert data["cooldown"]["duration"] == mock_response["cooldown"]["duration"]
