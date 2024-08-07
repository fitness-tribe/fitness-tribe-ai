# Fitness Tribe API

Fitness Tribe AI is an AI-powered fitness API designed for coaches and athletes. The API provides meal analysis functionality by analyzing meal photos and an AI powered workout builder, which can generate workout plans based on athlete profiles. Fitness Tribe AI has been built the Gemini model.

## Features

- **Meal Analysis**: Upload a photo of a meal to receive a detailed analysis of its ingredients and calorie count.
- **Workout Builder**: Input an athlete's profile details to receive a personalized workout plan tailored to the athlete's fitness goal.

## Project Structure

```
fitness-tribe-ai/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── gemini_model.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── meals.py
│   │   ├── workouts.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── meal.py
│   │   ├── workout.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── meal_service.py
│   │   ├── workout_service.py
├── tests/
│   ├── __init__.py
│   ├── test_meals.py
│   ├── test_workouts.py
├── .gitignore
├── postman_collection.json
├── README.md
├── requirements.txt
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/fitness-tribe-api.git
   cd fitness-tribe-api
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory and add your Gemini API key:

   ```dotenv
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Usage

1. **Run the FastAPI server**

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API documentation**

   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## API Endpoints

### Meal Analysis

- **Endpoint**: `POST /meals/analyze_meal`
- **Description**: Analyze a meal image to provide the food name, total calories, and calories per ingredient.
- **Request**: `multipart/form-data` with an image file.
- **Response**: JSON with calories and nutrients.

  ```json
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
  ```

### Workout Recommendations

- **Endpoint**: `POST /workouts/recommend_workouts`
- **Description**: Generate a workout plan based on the athlete's profile.
- **Request**: JSON with profile details.

  ```json
  {
    "weight": 70,
    "height": 175,
    "age": 25,
    "sex": "male",
    "goal": "bulking"
  }
  ```

- **Response**: JSON with a list of workout sessions, exercises, sets, reps, and rest time.

  ```json
  {
    "warmup": {
      "description": "Dynamic Stretching",
      "duration": 5
    },
    "cardio": {
      "description": "Moderate-Intensity Steady State",
      "duration": 30
    },
    "sessions_per_week": 3,
    "workout_sessions": [
      {
        "exercises": [
          {
            "name": "Bench Press",
            "sets": 3,
            "reps": "8-12",
            "rest": 60
          },
          {
            "name": "Squat",
            "sets": 3,
            "reps": "8-12",
            "rest": 60
          }
        ]
      },
      {
        "exercises": [
          {
            "name": "Overhead Press",
            "sets": 3,
            "reps": "8-12",
            "rest": 60
          },
          {
            "name": "Barbell Row",
            "sets": 3,
            "reps": "8-12",
            "rest": 60
          }
        ]
      },
      {
        "exercises": [
          {
            "name": "Triceps Pushdown",
            "sets": 3,
            "reps": "8-12",
            "rest": 60
          },
          {
            "name": "Biceps Curl",
            "sets": 3,
            "reps": "8-12",
            "rest": 60
          }
        ]
      }
    ],
    "cooldown": {
      "description": "Static Stretching",
      "duration": 5
    }
  }
  ```

## Unit tests

The project contains unit tests for the meal service and the workout service. To execute them you can use the pytest command.

```bash
pytest
```

## Postman Collection

In case you want to test the API endpoints using postman, feel free to import the `postman_collection.json` as a collection into your postman workspace.

## Contributing

1. **Fork the repository**
2. **Create a new branch**
3. **Make your changes**
4. **Submit a pull request**

## License

This project is licensed under the MIT License.
