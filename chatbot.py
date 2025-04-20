import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time


# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=(
        "You are an AI cybersecurity expert specializing in ransomware prevention and recovery. "
        "Your role is to provide users with best practices to prevent attacks, immediate steps after an infection, "
        "and guidance on restoring data without paying ransom. Ensure clear, actionable advice and caution users "
        "about emerging threats and secure practices."
    ),
)

chat_session = model.start_chat(history=[])


app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if "message" not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_input = data["message"].strip()
    if not user_input:
        return jsonify({"response": "No input detected. Please try again."})
    
    response = chat_session.send_message(user_input)
    model_response = response.text.strip()
    
    if not model_response:
        model_response = "I'm sorry, I couldn't process that. Can you try again?"
    
    return jsonify({"response": model_response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
