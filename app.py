import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=(
        "You are a supportive mental health companion trained to provide emotional support and guidance. "
        "Your role is to listen actively, show empathy, and suggest healthy coping strategies. "
        "You should always emphasize that you're not a replacement for professional mental health services "
        "and encourage users to seek professional help when appropriate. "
        "Provide evidence-based information about mental health topics including stress management, "
        "anxiety, depression, mindfulness, and self-care practices. "
        "If users express thoughts of self-harm or suicide, respond with compassion and "
        "urgently direct them to emergency services and crisis helplines."
    ),
)

chat_session = model.start_chat(history=[])

app = Flask(__name__, template_folder='templates')


# Serve the home page
@app.route("/")
def home():
    return render_template("index.html")

# Serve the About page
@app.route("/about")
def about():
    return render_template("about.html")

# Serve the Blogs page
@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

# Serve the Features page
@app.route('/features')
def features():
    return render_template("features.html")

# Serve the Chatbot page
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

CORS(app)  # Enable CORS for all routes

# Store user sessions
user_sessions = {}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if "message" not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_input = data["message"].strip()
    if not user_input:
        return jsonify({"response": "No input detected. Please try again."})
    
    # Create a unique session ID if not provided
    session_id = data.get("session_id", "default")
    
    # Get or create a chat session for this user
    if session_id not in user_sessions:
        user_sessions[session_id] = model.start_chat(history=[])
    
    current_session = user_sessions[session_id]
    
    # Send message and get response
    response = current_session.send_message(user_input)
    model_response = response.text.strip()
    
    if not model_response:
        model_response = "I'm sorry, I couldn't process that. Can you try again?"
    
    return jsonify({
        "response": model_response,
        "session_id": session_id
    })

@app.route("/resources", methods=["GET"])
def resources():
    """Endpoint to provide mental health resources"""
    resources = {
        "crisis_lines": [
            {"name": "National Suicide Prevention Lifeline", "number": "988", "url": "https://988lifeline.org"},
            {"name": "Crisis Text Line", "number": "Text HOME to 741741", "url": "https://www.crisistextline.org"},
            {"name": "SAMHSA's National Helpline", "number": "1-800-662-4357", "url": "https://www.samhsa.gov/find-help/national-helpline"}
        ],
        "apps": [
            {"name": "Headspace", "description": "Meditation and mindfulness", "url": "https://www.headspace.com"},
            {"name": "Calm", "description": "Sleep, meditation and relaxation", "url": "https://www.calm.com"},
            {"name": "Woebot", "description": "AI-based cognitive behavioral therapy", "url": "https://woebothealth.com"}
        ],
        "websites": [
            {"name": "NAMI", "description": "National Alliance on Mental Illness", "url": "https://www.nami.org"},
            {"name": "Mental Health America", "description": "Mental health resources and screening tools", "url": "https://www.mhanational.org"},
            {"name": "Psychology Today", "description": "Find a therapist directory", "url": "https://www.psychologytoday.com/us/therapists"}
        ]
    }
    return jsonify(resources)

@app.route("/clear-session", methods=["POST"])
def clear_session():
    """Endpoint to clear a user's chat session"""
    data = request.json
    session_id = data.get("session_id")
    
    if session_id and session_id in user_sessions:
        user_sessions[session_id] = model.start_chat(history=[])
        return jsonify({"status": "success", "message": "Session cleared"})
    
    return jsonify({"status": "error", "message": "Session not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)