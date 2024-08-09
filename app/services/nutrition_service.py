from app.models.gemini_model import GeminiModel
from app.schemas.nutrition import (
    ProfileData,
    NutritionPlan,
    MealOption,
    MealPlan,
    DailyCaloriesRange,
    MacronutrientRange,
)
from fastapi import HTTPException
import json
import logging


def clean_response_text(response_text: str) -> str:
    # Strip unnecessary markdown or whitespace that might have been included
    clean_text = response_text.strip("```json").strip("```").strip()
    return clean_text


def generate_nutrition_plan(profile_data: ProfileData) -> NutritionPlan:
    try:
        result_text = GeminiModel.generate_nutrition_plan(profile_data.model_dump())

        if not result_text:
            raise HTTPException(status_code=500, detail="No response from Gemini API")

        # Clean the result_text to remove Markdown formatting
        clean_result_text = clean_response_text(result_text)

        # Directly parse the cleaned result text
        try:
            result = json.loads(clean_result_text)
        except json.JSONDecodeError as e:
            logging.error(f"JSON Decode Error (Provide Nutrition Advice): {str(e)}")
            logging.error(
                f"Cleaned Result Text (Provide Nutrition Advice) on JSON Decode Error: {clean_result_text}"
            )
            raise HTTPException(status_code=500, detail=f"JSON Decode Error: {str(e)}")

        # Convert the result dictionary to Pydantic models
        daily_calories_range = DailyCaloriesRange(**result["daily_calories_range"])
        macronutrients_range = {
            k: MacronutrientRange(**v)
            for k, v in result["macronutrients_range"].items()
        }

        def parse_meal_options(meal_data):
            return [MealOption(**meal) for meal in meal_data]

        meal_plan = MealPlan(
            breakfast=parse_meal_options(result["meal_plan"]["breakfast"]),
            lunch=parse_meal_options(result["meal_plan"]["lunch"]),
            dinner=parse_meal_options(result["meal_plan"]["dinner"]),
            snacks=parse_meal_options(result["meal_plan"]["snacks"]),
        )

        return NutritionPlan(
            daily_calories_range=daily_calories_range,
            macronutrients_range=macronutrients_range,
            meal_plan=meal_plan,
        )

    except Exception as e:
        logging.error(f"Exception (Provide Nutrition Advice): {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
