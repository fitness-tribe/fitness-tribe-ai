# app/schemas/meal.py

from pydantic import BaseModel
from typing import Dict


class Meal(BaseModel):
    food_name: str
    total_calories: int
    calories_per_ingredient: Dict[str, int]
