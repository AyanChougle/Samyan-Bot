import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Replace with your Google Gemini API key
API_KEY = "AIzaSyAMLdRVoqJ_DToIxmGP1oJVbqRzYQUQohs"

# Configure Gemini AI
genai.configure(api_key=API_KEY)

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)

        bot_message = response.text if response else "I'm sorry, I couldn't process that."
        return jsonify({"response": bot_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
