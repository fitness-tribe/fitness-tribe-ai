from fastapi import APIRouter, HTTPException
from app.services.workout_service import recommend_workouts
from app.schemas.workout import Workout, ProfileData

router = APIRouter()

@router.post("/recommend_workouts", response_model=Workout, summary="Recommend Workouts", description="Input your profile details to receive a personalized workout plan.")
async def recommend_workouts_endpoint(profile_data: ProfileData):
    """
    Get a personalized workout plan based on profile data.

    - **weight**: Weight in kilograms
    - **height**: Height in centimeters
    - **age**: Age in years
    - **goal**: Fitness goal (e.g., bulking, shredding)
    """
    try:
        result = recommend_workouts(profile_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
