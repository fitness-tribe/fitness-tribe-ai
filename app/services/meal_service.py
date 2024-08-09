# app/services/meal_service.py

from app.models.gemini_model import GeminiModel
from app.schemas.meal import Meal
from fastapi import HTTPException
import logging
import json


def analyze_meal(image_data: bytes) -> Meal:
    logging.info("Starting meal analysis")
    try:
        result_text = GeminiModel.analyze_meal(image_data)
        if not result_text:
            raise HTTPException(status_code=500, detail="No response from Gemini API")

        logging.info(f"Gemini API Response Text (Analyze Meal): {result_text}")

        # Clean the result_text to remove Markdown formatting
        clean_result_text = result_text.strip("```json\n").strip("```")
        logging.info(f"Cleaned Result Text (Analyze Meal): {clean_result_text}")

        # Parse the cleaned JSON response
        result = json.loads(clean_result_text)
        food_name = result.get("food_name")
        total_calories = result.get("total_calories")
        calories_per_ingredient = result.get("calories_per_ingredient")
        logging.info(
            f"Parsed Food Name: {food_name}, Total Calories: {total_calories}, Calories per Ingredient: {calories_per_ingredient}"
        )

        if food_name is None or total_calories is None or not calories_per_ingredient:
            logging.error(
                "Missing food name, total calories, or calories per ingredient in the response"
            )
            raise HTTPException(
                status_code=500,
                detail="Missing food name, total calories, or calories per ingredient in the response",
            )

    except Exception as e:
        logging.error(f"Exception (Analyze Meal): {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    return Meal(
        food_name=food_name,
        total_calories=total_calories,
        calories_per_ingredient=calories_per_ingredient,
    )
