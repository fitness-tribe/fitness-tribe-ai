# app/main.py

import os
import logging
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import meals, workouts

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the FastAPI app
app = FastAPI(
    title="Fitness Tribe API",
    description="An AI-powered fitness application for coaches and athletes.",
    version="1.0.0"
)

# Include routers for different endpoints
app.include_router(meals.router, prefix="/meals", tags=["meals"])
app.include_router(workouts.router, prefix="/workouts", tags=["workouts"])

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to Fitness Tribe API"}
