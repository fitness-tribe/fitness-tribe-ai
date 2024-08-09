from fastapi import APIRouter, HTTPException
from app.services.workout_service import generate_workout_plan
from app.schemas.workout import WorkoutPlan, ProfileData

router = APIRouter()

@router.post("/generate", response_model=WorkoutPlan, summary="Generate Workout Plan", description="Input the athlete's profile details to receive a workout plan.")
async def generate_workout_plan_endpoint(profile_data: ProfileData):
    """
    Get a personalized workout plan based on athlete profile.

    - **weight**: Weight in kilograms
    - **height**: Height in centimeters
    - **age**: Age in years
    - **goal**: Fitness goal (e.g., bulking, shredding)
    """
    try:
        result = generate_workout_plan(profile_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
