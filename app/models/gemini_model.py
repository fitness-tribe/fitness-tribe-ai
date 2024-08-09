import os
import google.generativeai as gemini
import logging
from PIL import Image
from io import BytesIO

# Initialize the Gemini API key and the model
gemini.api_key = os.getenv("GEMINI_API_KEY")
model_name = "gemini-1.5-flash"
model = gemini.GenerativeModel(model_name)

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

        try:
            # Convert image data (which could be bytes) into an Image object
            image = Image.open(BytesIO(image_data))

            # Call the Gemini model with both the prompt and the image
            response = model.generate_content([prompt, image])

            # Log the response for debugging purposes
            logging.info(f"Gemini API Full Response (Analyze Meal): {response}")

            # Directly return the output text
            output_text = response.text
            logging.info(f"Output Text (Analyze Meal): {output_text}")

            return output_text

        except Exception as e:
            logging.error(f"Error communicating with Gemini API: {str(e)}")
            return None

    @staticmethod
    def generate_workout_plan(profile_data):
        prompt = (
            f"Create a workout plan for a {profile_data['age']} year old {profile_data['sex']}, "
        f"weighing {profile_data['weight']}kg and {profile_data['height']}cm tall, with the goal of {profile_data['goal']}. "
        "The workout plan should focus exclusively on safe, appropriate, and positive exercise recommendations. "
        "Avoid any mention of sensitive or controversial topics. Do not include any content related to sexuality, hate speech, violence, or other harmful themes. "
        "Respond in valid JSON format with no additional explanation or text. "
        "The plan should include:\n"
        "- A warm-up section with a description and duration.\n"
        "- Cardio recommendations with a description and duration.\n"
        "- Number of sessions per week.\n"
        "- Detailed exercises for each session with sets, reps, and rest times.\n"
        "- A cooldown section with a description and duration.\n\n"
        "Respond in strict JSON format, ensuring all data is appropriately formatted and focused solely on the workout plan. Ensure that all reps values in the workout_sessions are in double quotes. Here is the format:\n"
        "{\n"
        "  \"warmup\": {\"description\": \"<description>\", \"duration\": <duration in minutes>},\n"
        "  \"cardio\": {\"description\": \"<description>\", \"duration\": <duration in minutes>},\n"
        "  \"sessions_per_week\": <sessions>,\n"
        "  \"workout_sessions\": [\n"
        "    {\n"
        "      \"exercises\": [\n"
        "        {\"name\": \"<exercise name>\", \"sets\": <sets>, \"reps\": \"<reps>\", \"rest\": <rest time in seconds>}\n"
        "      ]\n"
        "    }\n"
        "  ],\n"
        "  \"cooldown\": {\"description\": \"<description>\", \"duration\": <duration in minutes>}\n"
        "}\n"
        )
        try:
            response = model.generate_content(prompt)

            # Log the response for debugging purposes
            logging.info(f"Full Gemini API Response: {response}")
            
            output_text = response.text
            return output_text

        except Exception as e:
            logging.error(f"Error communicating with Gemini API or while parsing the response: {str(e)}")
            return None

    @staticmethod
    def generate_nutrition_plan(profile_data):
        prompt = (
            f"Provide a personalized nutrition plan for a {profile_data['age']} year old, "
            f"{profile_data['sex']}, weighing {profile_data['weight']}kg, height {profile_data['height']}cm, "
            f"with the goal of {profile_data['goal']}. The nutrition plan should include:\n\n"
            "- A daily calorie intake range.\n"
            "- Macronutrient distribution in daily ranges in grams for protein, carbohydrates, and fat.\n"
            "- A meal plan with an appropriate number of meals. Breakfast, lunch, dinner, and snacks each should have 3 options.\n"
            "- Each meal option should include:\n"
            "  - A description.\n"
            "  - Ingredients with quantities (grams, cups, tablespoons).\n"
            "  - Calorie counts per ingredient and per meal.\n"
            "  - A detailed recipe including step-by-step instructions and total cooking time.\n"
            "- Ensure the response follows strict JSON format rules with no trailing commas, and all strings are properly quoted.\n\n"
            "Respond in valid JSON format with no additional explanation or text.\n\n"
            "{\n"
            "  \"daily_calories_range\": {\"min\": <min calories>, \"max\": <max calories>},\n"
            "  \"macronutrients_range\": {\n"
            "    \"protein\": {\"min\": <min grams>, \"max\": <max grams>},\n"
            "    \"carbohydrates\": {\"min\": <min grams>, \"max\": <max grams>},\n"
            "    \"fat\": {\"min\": <min grams>, \"max\": <max grams>}\n"
            "  },\n"
            "  \"meal_plan\": {\n"
            "    \"breakfast\": [\n"
            "      {\"description\": \"<meal description>\", \"ingredients\": [\n"
            "        {\"ingredient\": \"<ingredient>\", \"quantity\": \"<quantity>\", \"calories\": <calories>}\n"
            "      ], \"total_calories\": <calories>, \"recipe\": \"<short recipe>\"}, ...\n"
            "    ],\n"
            "    \"lunch\": [ ... ],\n"
            "    \"dinner\": [ ... ],\n"
            "    \"snacks\": [ ... ]\n"
            "  }\n"
            "}"
        )

        try:
            response = model.generate_content(prompt)

            # Log the response for debugging purposes
            logging.info(f"Full Gemini API Response: {response}")
            output_text = response.text

            return output_text

        except Exception as e:
            logging.error(f"Error communicating with Gemini API or while parsing the response: {str(e)}")
            return None
