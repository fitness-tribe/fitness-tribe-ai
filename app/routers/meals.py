from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.meal_service import analyze_meal
from app.schemas.meal import Meal

router = APIRouter()


@router.post(
    "/analyze",
    response_model=Meal,
    summary="Analyze Meal",
    description="Upload a meal image to receive a description and calorie count breakdown.",
)
async def analyze_meal_endpoint(file: UploadFile = File(...)):
    """
    Analyze a meal image and get a description and calorie count breakdown.

    - **file**: Image file of the meal
    """
    image_data = await file.read()
    try:
        result = analyze_meal(image_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
