# 🧠 Samyan-Bot: Mental Health AI Chatbot

Samyan-Bot is a compassionate AI-powered mental health chatbot created to support users in dealing with stress, anxiety, and emotional struggles. It leverages Google's Gemini API to provide context-aware, empathetic conversations in real-time. Built using Flask, HTML, CSS, and JavaScript, this bot aims to deliver comfort and mental wellness through technology.

---

## 🌟 Features

- 💬 Conversational mental health support
- 🤖 Gemini API integration for intelligent replies
- 🧠 Emotional understanding and context-aware responses
- 💻 Responsive and clean web UI
- 🔐 Secure API key management via environment variables
- 📦 Organized and modular codebase

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3, Flask
- **AI Engine**: Google Gemini API
- **Templating**: Jinja2
- **Environment Management**: python-dotenv
- **Version Control**: Git + GitHub

---

## 📁 Project Structure

Samyan-Bot/ │ 
            ├── static/ 
            │ ├── css/ │ 
            │ └── style.css 
            │ ├── js/  
            │ │ └── script.js 
            │ ├── templates/ 
            │ ├── index.html 
            │ └── chat.html 
            ├── app.py # Flask app 
            ├── chatbot.py # Gemini integration logic 
            ├── requirements.txt 
            ├── .env # API Key (not pushed to GitHub) 
            └── README.md

---
💬 How It Works
User enters a message in the chat UI.

Message is sent to the Flask backend via JavaScript.

Flask processes the request and forwards it to Gemini via the Gemini API key.

The AI model returns a thoughtful, empathetic response.

The response is displayed in real-time on the frontend.

---

🧪 Example Usage
User: I'm feeling anxious lately and can't focus on my studies.
Samyan-Bot: It's okay to feel overwhelmed sometimes. Let's try some calming techniques together. Would you like to practice a breathing exercise?

---

🧑‍💻 Author
Ayan Chougle
GitHub: @AyanChougle

---

📜 License
This project is licensed under the MIT License.
You're free to use, modify, and distribute it with attribution.


--- 

💡 Future Enhancements
🧑‍⚕️ Connect users to professional resources

📊 Emotional tone analysis

🧭 Suggest wellness routines

🔒 User authentication and data saving

📱 Mobile-friendly PWA version

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
1. git clone https://github.com/AyanChougle/Samyan-Bot.git
2. cd Samyan-Bot
3. python -m venv venv
    source venv/bin/activate        # For Windows: venv\Scripts\activate
4. pip install -r requirements.txt
5. Get Gemini API Key
      Visit: Google AI Studio
      Generate your Gemini API Key
6. Create a .env file and add this line:
      GEMINI_API_KEY=your_gemini_api_key_here
7. python app.py
