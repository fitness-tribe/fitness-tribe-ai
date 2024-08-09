# app/schemas/workout.py

from pydantic import BaseModel
from typing import List


class ProfileData(BaseModel):
    weight: float  # in kilograms
    height: float  # in centimeters
    age: int
    sex: str
    goal: str  # bulking, shredding, fat loss, muscle building
    workouts_per_week: int


class Exercise(BaseModel):
    name: str
    sets: int
    reps: str  # could also be 'as many as possible'
    rest: int  # rest time in seconds


class WarmupCardioCooldown(BaseModel):
    description: str
    duration: int


class WorkoutSession(BaseModel):
    exercises: List[Exercise]


class WorkoutPlan(BaseModel):
    warmup: WarmupCardioCooldown
    cardio: WarmupCardioCooldown
    sessions_per_week: int
    workout_sessions: List[WorkoutSession]
    cooldown: WarmupCardioCooldown
