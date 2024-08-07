# app/schemas/workout.py

from pydantic import BaseModel
from typing import List, Union

class ProfileData(BaseModel):
    weight: float
    height: float
    age: int
    sex: str
    goal: str

class Exercise(BaseModel):
    name: str
    sets: int
    reps: Union[str, int]  # Allow reps to be a string to handle ranges
    rest: int

class WarmupCardioCooldown(BaseModel):
    description: str
    duration: int

class WorkoutSession(BaseModel):
    exercises: List[Exercise]

class Workout(BaseModel):
    warmup: WarmupCardioCooldown
    cardio: WarmupCardioCooldown
    sessions_per_week: int
    workout_sessions: List[WorkoutSession]
    cooldown: WarmupCardioCooldown
