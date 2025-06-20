# Install OpenAI SDK (if not already installed)
!pip install openai==0.28
# importing the required modules and libraries
import openai
import os
import json
import traceback # Import traceback for detailed error info
# Replace with your OpenAI API key
openai.api_key = "OpenAI API key here"  # You can use os.getenv("OPENAI_API_KEY") in real use
# Example Claim Input
claim_data = {
    "claim_id": "CLM2025-001",
    "claim_type": "Crop damage",
    "location": "Kano, Nigeria",
    "date": "2025-06-10",
    "description": "The crops were damaged due to unexpected flooding last week.",
    "farmer_profile": "First-time customer with smallholder maize farm",
    "weather_data": "No rainfall recorded in Kano between June 5–10",
    "attachments": ["maize_field_photo.jpg"]
}

def build_prompt(claim_type, location, date, weather_data, description, farmer_profile):
    return f"""
You are AgroSure AI, an expert agricultural 
insurance claims investigator. Your task is 
to evaluate each incoming claim and assign 
a fraud risk score between 0 and 100, 
where 0 means no fraud risk and 100 means very high risk
- Claim type: {claim_type}
- Location: {location}
- Date: {date}
- Weather on date: {weather_data}
- Farmer profile: {farmer_profile}
- Description: {description}

Output format:
{{
  "score": 85,
  "reason": "No rain recorded despite flood claim."
}}
"""

def chatbot_response(claim_type, location, date, weather_data, description, farmer_profile):
    print("Building prompt...")
    prompt = build_prompt(claim_type, location, date, weather_data, description, farmer_profile)
    print("Prompt built:", prompt)

    try:
        print("Calling OpenAI API...")
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You analyze agricultural insurance claims for fraud risk."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        print("OpenAI API call successful.")

        output_text = response.choices[0].message.content
        print("Raw AI output:", output_text)

        # Remove markdown formatting before parsing JSON
        json_output = output_text.strip().replace("```json\n", "").replace("```", "")
        print("Cleaned AI output for JSON parsing:", json_output)

        try:
            dict_data = json.loads(json_output)
            print("JSON parsed successfully:", dict_data)
            return f"Fraud Score: {dict_data.get('score', 'N/A')}\nReason: {dict_data.get('reason', 'N/A')}"
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Invalid JSON string: {json_output}")
            traceback.print_exc() # Print traceback for more details
            return f"Error processing AI response: JSON Decode Error. Details: {e}"

    except Exception as e:
        print(f"An error occurred during OpenAI API call: {e}")
        traceback.print_exc() # Print traceback for more details
        return f"Error during AI risk assessment: {e}"
