# app/models/gemini_model.py

import os
import google.generativeai as gemini
import logging

# Initialize the Gemini client
gemini.api_key = os.getenv("GEMINI_API_KEY")

class GeminiModel:
    @staticmethod
    def analyze_meal(image_data):
        prompt = (
            "Analyze the following meal image and provide the name of the food, "
            "total calorie count, and calories per ingredient. "
            "Respond in the following JSON format: "
            "{ \"food_name\": \"<food name>\", \"total_calories\": <total calorie count>, "
            "\"calories_per_ingredient\": {\"<ingredient1>\": <calories>, \"<ingredient2>\": <calories>, ...} }"
        )
        response = gemini.generate_text(
            prompt=prompt
        )
        logging.info(f"Gemini API Full Response (Analyze Meal): {response}")
        
        # Access the first candidate's output text
        if response.candidates:
            for candidate in response.candidates:
                logging.info(f"Candidate: {candidate}")

            output_text = response.candidates[0]['output']
            logging.info(f"Output Text (Analyze Meal): {output_text}")
            return output_text
        else:
            logging.error("No candidates found in the response")
            return None

    @staticmethod
    def recommend_workouts(profile_data):
        prompt = (
            f"Create a workout plan for a {profile_data['age']} year old, "
            f"{profile_data['sex']}, weighing {profile_data['weight']}kg, height {profile_data['height']}cm, "
            f"with the goal of {profile_data['goal']}. "
            f"Respond in the following JSON format: "
            "{ \"warmup\": {\"description\": \"<description>\", \"duration\": <duration in minutes>}, "
            "\"cardio\": {\"description\": \"<description>\", \"duration\": <duration in minutes>}, "
            "\"sessions_per_week\": <sessions>, "
            "\"workout_sessions\": [ "
            "{ \"exercises\": ["
            "{ \"exercise\": \"<exercise name>\", \"sets\": <sets>, \"reps\": \"<reps>\", \"rest\": <rest time in seconds> }"
            "] } ], "
            "\"cooldown\": {\"description\": \"<description>\", \"duration\": <duration in minutes>} }"
        )
        response = gemini.generate_text(
            prompt=prompt
        )
        logging.info(f"Gemini API Full Response (Recommend Workouts): {response}")
        
        # Access the first candidate's output text
        if response.candidates:
            for candidate in response.candidates:
                logging.info(f"Candidate: {candidate}")

            output_text = response.candidates[0]['output']
            logging.info(f"Output Text (Recommend Workouts): {output_text}")
            return output_text
        else:
            logging.error("No candidates found in the response")
            return None
