import json
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.schemas.nutrition import ProfileData

client = TestClient(app)


class TestNutritionService:
    @patch("app.models.gemini_model.GeminiModel.generate_nutrition_plan")
    def test_generate_nutrition_plan(self, mock_generate_nutrition_plan):
        # Mock response from the Gemini API
        mock_response = {
            "daily_calories_range": {"min": 2500, "max": 3000},
            "macronutrients_range": {
                "protein": {"min": 150, "max": 180},
                "carbohydrates": {"min": 300, "max": 400},
                "fat": {"min": 50, "max": 70},
            },
            "meal_plan": {
                "breakfast": [
                    {
                        "description": "Oatmeal with fruit and nuts",
                        "ingredients": [
                            {
                                "ingredient": "Oatmeal",
                                "quantity": "1 cup",
                                "calories": 150,
                            },
                            {
                                "ingredient": "Banana",
                                "quantity": "1/2 cup",
                                "calories": 100,
                            },
                            {
                                "ingredient": "Almonds",
                                "quantity": "1/4 cup",
                                "calories": 170,
                            },
                        ],
                        "total_calories": 420,
                        "recipe": "Combine oatmeal, banana, and almonds in a bowl. Add milk or yogurt.",
                    },
                    {
                        "description": "Yogurt with berries and granola",
                        "ingredients": [
                            {
                                "ingredient": "Yogurt",
                                "quantity": "1 cup",
                                "calories": 150,
                            },
                            {
                                "ingredient": "Blueberries",
                                "quantity": "1/2 cup",
                                "calories": 50,
                            },
                            {
                                "ingredient": "Strawberries",
                                "quantity": "1/2 cup",
                                "calories": 40,
                            },
                            {
                                "ingredient": "Granola",
                                "quantity": "1/4 cup",
                                "calories": 100,
                            },
                        ],
                        "total_calories": 440,
                        "recipe": "Combine yogurt, berries, and granola in a bowl.",
                    },
                ],
                "lunch": [
                    {
                        "description": "Salad with grilled chicken and vegetables",
                        "ingredients": [
                            {
                                "ingredient": "Salad mix",
                                "quantity": "1 cup",
                                "calories": 10,
                            },
                            {
                                "ingredient": "Chicken breast",
                                "quantity": "3 ounces",
                                "calories": 140,
                            },
                            {
                                "ingredient": "Tomatoes",
                                "quantity": "1/2 cup",
                                "calories": 20,
                            },
                            {
                                "ingredient": "Cucumber",
                                "quantity": "1/2 cup",
                                "calories": 15,
                            },
                            {
                                "ingredient": "Avocado",
                                "quantity": "1/4",
                                "calories": 100,
                            },
                        ],
                        "total_calories": 285,
                        "recipe": "Combine salad mix, chicken, tomatoes, cucumber, and avocado in a bowl. Drizzle with dressing.",
                    }
                ],
                "dinner": [
                    {
                        "description": "Grilled salmon with vegetables",
                        "ingredients": [
                            {
                                "ingredient": "Salmon",
                                "quantity": "6 ounces",
                                "calories": 350,
                            },
                            {
                                "ingredient": "Broccoli",
                                "quantity": "1 cup",
                                "calories": 50,
                            },
                            {
                                "ingredient": "Quinoa",
                                "quantity": "1/2 cup",
                                "calories": 120,
                            },
                        ],
                        "total_calories": 520,
                        "recipe": "Grill the salmon and serve with steamed broccoli and cooked quinoa.",
                    }
                ],
                "snacks": [
                    {
                        "description": "Apple with peanut butter",
                        "ingredients": [
                            {
                                "ingredient": "Apple",
                                "quantity": "1 medium",
                                "calories": 95,
                            },
                            {
                                "ingredient": "Peanut butter",
                                "quantity": "2 tablespoons",
                                "calories": 190,
                            },
                        ],
                        "total_calories": 285,
                        "recipe": "Slice the apple and dip in peanut butter.",
                    }
                ],
            },
        }
        mock_generate_nutrition_plan.return_value = json.dumps(mock_response)

        # Create a mock profile data
        profile_data = ProfileData(
            weight=70,
            height=175,
            age=25,
            sex="male",
            goal="bulking",
            dietary_preferences=["high protein"],
            duration_weeks=4,
            food_intolerance=["Dairy", "Gluten"],
        ).model_dump()

        # Send a POST request to the generate nutrition plan endpoint
        response = client.post("/nutrition-plans/generate", json=profile_data)

        # Check the response status code
        assert response.status_code == 200

        # Load the response JSON data
        data = response.json()
        print("Response data:", data)

        # Verify the structure of the response
        assert "daily_calories_range" in data
        assert (
            data["daily_calories_range"]["min"]
            == mock_response["daily_calories_range"]["min"]
        )
        assert (
            data["daily_calories_range"]["max"]
            == mock_response["daily_calories_range"]["max"]
        )

        assert "macronutrients_range" in data
        for key in mock_response["macronutrients_range"]:
            assert (
                data["macronutrients_range"][key]["min"]
                == mock_response["macronutrients_range"][key]["min"]
            )
            assert (
                data["macronutrients_range"][key]["max"]
                == mock_response["macronutrients_range"][key]["max"]
            )

        assert "meal_plan" in data
        for meal_type in ["breakfast", "lunch", "dinner", "snacks"]:
            assert len(data["meal_plan"][meal_type]) == len(
                mock_response["meal_plan"][meal_type]
            )
            for i, meal in enumerate(data["meal_plan"][meal_type]):
                assert (
                    meal["description"]
                    == mock_response["meal_plan"][meal_type][i]["description"]
                )
                assert (
                    meal["total_calories"]
                    == mock_response["meal_plan"][meal_type][i]["total_calories"]
                )
                assert (
                    meal["recipe"] == mock_response["meal_plan"][meal_type][i]["recipe"]
                )
                for j, ingredient in enumerate(meal["ingredients"]):
                    assert (
                        ingredient["ingredient"]
                        == mock_response["meal_plan"][meal_type][i]["ingredients"][j][
                            "ingredient"
                        ]
                    )
                    assert (
                        ingredient["quantity"]
                        == mock_response["meal_plan"][meal_type][i]["ingredients"][j][
                            "quantity"
                        ]
                    )
                    assert (
                        ingredient["calories"]
                        == mock_response["meal_plan"][meal_type][i]["ingredients"][j][
                            "calories"
                        ]
                    )
