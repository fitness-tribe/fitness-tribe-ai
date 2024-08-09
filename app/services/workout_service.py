# app/services/workout_service.py

from app.models.gemini_model import GeminiModel
from app.schemas.workout import ProfileData, WorkoutPlan, Exercise, WarmupCardioCooldown
from fastapi import HTTPException
import json
import logging
import re


def clean_response_text(response_text: str) -> str:
    # Remove Markdown formatting
    clean_text = response_text.strip("```json\n").strip("```")

    # Fix the "rest" values (remove units and convert to integers)
    clean_text = re.sub(r'("rest": )(\d+) seconds', r"\1\2", clean_text)

    # Fix the "reps" values to ensure they are strings
    clean_text = re.sub(r'("reps": )(\d+)-(\d+)', r'\1"\2-\3"', clean_text)

    return clean_text


def generate_workout_plan(profile_data: ProfileData) -> WorkoutPlan:
    try:
        model_response = GeminiModel.generate_workout_plan(profile_data.model_dump())
        if not model_response:
            raise HTTPException(status_code=500, detail="No response from Gemini API")

        # Clean the result_text to remove Markdown formatting and fix "rest" values
        clean_result_text = clean_response_text(model_response)

        # Parse the cleaned JSON response
        result = json.loads(clean_result_text)

        warmup_data = result.get("warmup")
        cardio_data = result.get("cardio")
        sessions_per_week = result.get("sessions_per_week")
        workout_sessions_data = result.get("workout_sessions")
        cooldown_data = result.get("cooldown")

        if (
            not warmup_data
            or not cardio_data
            or sessions_per_week is None
            or not workout_sessions_data
            or not cooldown_data
        ):
            logging.error("Missing details in the response")
            raise HTTPException(
                status_code=500, detail="Missing details in the response"
            )

        warmup = WarmupCardioCooldown(
            description=warmup_data["description"], duration=warmup_data["duration"]
        )
        cardio = WarmupCardioCooldown(
            description=cardio_data["description"], duration=cardio_data["duration"]
        )
        cooldown = WarmupCardioCooldown(
            description=cooldown_data["description"], duration=cooldown_data["duration"]
        )

        workout_sessions = []
        for session_data in workout_sessions_data:
            exercises = []
            for exercise_data in session_data["exercises"]:
                name = exercise_data.get("name")
                sets = exercise_data.get("sets")
                reps = exercise_data.get("reps")
                rest = exercise_data.get("rest")

                if name is None or sets is None or reps is None or rest is None:
                    logging.error("Invalid exercise format from Gemini API")
                    raise HTTPException(
                        status_code=500,
                        detail="Invalid exercise format from Gemini API",
                    )

                exercises.append(Exercise(name=name, sets=sets, reps=reps, rest=rest))
            workout_sessions.append({"exercises": exercises})

        workout = WorkoutPlan(
            warmup=warmup,
            cardio=cardio,
            sessions_per_week=sessions_per_week,
            workout_sessions=workout_sessions,
            cooldown=cooldown,
        )

    except Exception as e:
        logging.error(f"Exception (Generate Workouts): {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    return workout
