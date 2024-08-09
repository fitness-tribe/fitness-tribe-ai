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
│   │   ├── nutrition.py
│   │   ├── workouts.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── meal.py
│   │   ├── nutrition.py
│   │   ├── workout.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── meal_service.py
│   │   ├── nutrition_service.py
│   │   ├── workout_service.py
├── tests/
│   ├── __init__.py
│   ├── test_meal_service.py
│   ├── test_nutrition_service.py
│   ├── test_workout_service.py
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

5. **Install pre-commit hooks**

   This project uses pre-commit hooks to enforce code quality standards, including linting, formatting, and checking for common issues like large files or merge conflicts.

   To install the hooks, run:

   ```bash
    pre-commit install
   ```

   This will set up the hooks to run automatically before you make any commits.

   You can manually run these checks on all files at any time with:

   ```bash
   pre-commit run --all-files
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

- **Endpoint**: `POST /meals/analyze`
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

### Nutrition Plan generator

- **Endpoint**: `POST /nutrition-plans/generate`
- **Description**: Generate a personalized nutrition plan based on the athlete's profile and dietary preferences, including food intolerances.
- **Request**: JSON with profile details.

  ```json
  {
    "weight": 70,
    "height": 175,
    "age": 25,
    "sex": "male",
    "goal": "bulking",
    "dietary_preferences": ["vegetarian", "high protein"],
    "food_intolerances": ["Gluten", "Dairy"],
    "duration_weeks": 4
  }
  ```

- **Response**: JSON with a daily calorie intake range, macronutrient distribution, and meal plan options for breakfast, lunch, dinner, and snacks.

  ```json
  {
    "daily_calories_range": {
      "min": 2800,
      "max": 3200
    },
    "macronutrients_range": {
      "protein": {
        "min": 140,
        "max": 170
      },
      "carbohydrates": {
        "min": 300,
        "max": 350
      },
      "fat": {
        "min": 60,
        "max": 80
      }
    },
    "meal_plan": {
      "breakfast": [
        {
          "description": "Oatmeal with fruit and nuts",
          "ingredients": [
            {
              "ingredient": "Oatmeal",
              "quantity": "1 cup",
              "calories": 150
            },
            {
              "ingredient": "Banana",
              "quantity": "1/2 cup",
              "calories": 105
            },
            {
              "ingredient": "Almonds",
              "quantity": "1/4 cup",
              "calories": 170
            }
          ],
          "total_calories": 425,
          "recipe": "Cook oatmeal according to package instructions. Top with sliced banana and almonds."
        },
        {
          "description": "Yogurt with berries and granola",
          "ingredients": [
            {
              "ingredient": "Greek yogurt",
              "quantity": "1 cup",
              "calories": 150
            },
            {
              "ingredient": "Blueberries",
              "quantity": "1/2 cup",
              "calories": 40
            },
            {
              "ingredient": "Granola",
              "quantity": "1/4 cup",
              "calories": 100
            }
          ],
          "total_calories": 290,
          "recipe": "Combine yogurt, blueberries, and granola in a bowl."
        }
      ],
      "lunch": [
        {
          "description": "Salad with grilled chicken and vegetables",
          "ingredients": [
            {
              "ingredient": "Salad greens",
              "quantity": "1 cup",
              "calories": 50
            },
            {
              "ingredient": "Grilled chicken breast",
              "quantity": "4 ounces",
              "calories": 120
            },
            {
              "ingredient": "Tomatoes",
              "quantity": "1/2 cup",
              "calories": 25
            },
            {
              "ingredient": "Avocado",
              "quantity": "1/2",
              "calories": 100
            }
          ],
          "total_calories": 295,
          "recipe": "Combine salad greens, grilled chicken, and tomatoes. Top with sliced avocado."
        },
        {
          "description": "Sandwich on whole-wheat bread",
          "ingredients": [
            {
              "ingredient": "Whole-wheat bread",
              "quantity": "2 slices",
              "calories": 150
            },
            {
              "ingredient": "Turkey breast",
              "quantity": "3 ounces",
              "calories": 120
            },
            {
              "ingredient": "Lettuce",
              "quantity": "2 leaves",
              "calories": 5
            },
            {
              "ingredient": "Tomato",
              "quantity": "2 slices",
              "calories": 10
            }
          ],
          "total_calories": 285,
          "recipe": "Layer turkey, lettuce, and tomato between slices of whole-wheat bread."
        }
      ],
      "dinner": [
        {
          "description": "Grilled salmon with quinoa and steamed vegetables",
          "ingredients": [
            {
              "ingredient": "Salmon fillet",
              "quantity": "6 ounces",
              "calories": 240
            },
            {
              "ingredient": "Quinoa",
              "quantity": "1 cup",
              "calories": 220
            },
            {
              "ingredient": "Broccoli",
              "quantity": "1 cup",
              "calories": 55
            }
          ],
          "total_calories": 515,
          "recipe": "Grill salmon until cooked through. Serve with cooked quinoa and steamed broccoli."
        },
        {
          "description": "Stir-fried tofu with brown rice and vegetables",
          "ingredients": [
            {
              "ingredient": "Tofu",
              "quantity": "1 cup",
              "calories": 180
            },
            {
              "ingredient": "Brown rice",
              "quantity": "1 cup",
              "calories": 215
            },
            {
              "ingredient": "Mixed vegetables",
              "quantity": "1 cup",
              "calories": 80
            }
          ],
          "total_calories": 475,
          "recipe": "Stir-fry tofu and vegetables in a pan. Serve over brown rice."
        }
      ],
      "snacks": [
        {
          "description": "Apple with peanut butter",
          "ingredients": [
            {
              "ingredient": "Apple",
              "quantity": "1 medium",
              "calories": 95
            },
            {
              "ingredient": "Peanut butter",
              "quantity": "2 tablespoons",
              "calories": 190
            }
          ],
          "total_calories": 285,
          "recipe": "Slice apple and spread peanut butter on each slice."
        },
        {
          "description": "Trail mix",
          "ingredients": [
            {
              "ingredient": "Mixed nuts",
              "quantity": "1/4 cup",
              "calories": 200
            },
            {
              "ingredient": "Dried fruit",
              "quantity": "1/4 cup",
              "calories": 120
            }
          ],
          "total_calories": 320,
          "recipe": "Combine mixed nuts and dried fruit in a small bowl."
        }
      ]
    }
  }
  ```

### Workout Plan generator

- **Endpoint**: `POST /workout-plans/generate`
- **Description**: Generate a workout plan based on the athlete's profile.
- **Request**: JSON with profile details.

  ```json
  {
    "weight": 70,
    "height": 175,
    "age": 25,
    "sex": "male",
    "goal": "bulking",
    "workouts_per_week": 3
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

## GitHub Actions CI

This project uses GitHub Actions for continuous integration. On every pull request to the main branch, the following will be checked:

- Code linting and formatting via pre-commit hooks.
- Python code linting using ruff.
- Running the test suite via pytest.

## Contributing

1. **Fork the repository**
2. **Create a new branch**
3. **Make your changes**
4. **Submit a pull request**

## License

This project is licensed under the MIT License.
