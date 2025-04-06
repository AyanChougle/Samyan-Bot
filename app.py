from flask import Flask, render_template, request, jsonify, send_from_directory

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

# Chatbot API route
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")

    # Basic chatbot logic (can be replaced with AI logic)
    if "hello" in user_message.lower():
        response = "Hello! How can I assist you today?"
    else:
        response = f"You said: {user_message}"

    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
