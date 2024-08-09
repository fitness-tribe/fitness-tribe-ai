from pydantic import BaseModel
from typing import List, Dict, Optional

# Define ProfileData model
class ProfileData(BaseModel):
    weight: float  # in kilograms
    height: float  # in centimeters
    age: int
    sex: str  # "male" or "female"
    goal: str  # bulking, shredding, fat loss, muscle building
    dietary_preferences: Optional[List[str]] = None  # e.g., ["vegetarian", "high protein, pescatarian, vegan"]
    food_intolerance: Optional[List[str]] = None  # e.g. ["dairy", "gluten", "caffeine"] 
    duration_weeks: int

class MacronutrientRange(BaseModel):
    min: int
    max: int

class DailyCaloriesRange(BaseModel):
    min: int
    max: int

class Ingredient(BaseModel):
    ingredient: str
    quantity: str
    calories: int

class MealOption(BaseModel):
    description: str
    ingredients: List[Ingredient]
    total_calories: int
    recipe: str

class MealPlan(BaseModel):
    breakfast: List[MealOption]
    lunch: List[MealOption]
    dinner: List[MealOption]
    snacks: List[MealOption]

class NutritionPlan(BaseModel):
    daily_calories_range: DailyCaloriesRange
    macronutrients_range: Dict[str, MacronutrientRange]
    meal_plan: MealPlan
