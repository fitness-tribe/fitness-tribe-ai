from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.meal_service import analyze_meal
from app.schemas.meal import Meal
from typing import Dict

router = APIRouter()

@router.post("/analyze_meal", response_model=Meal, summary="Analyze Meal", description="Upload a meal image to receive a calorie count and nutrient breakdown.")
async def analyze_meal_endpoint(file: UploadFile = File(...)):
    """
    Analyze a meal image and get calorie and nutrient information.

    - **file**: Image file of the meal
    """
    image_data = await file.read()
    try:
        result = analyze_meal(image_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
