async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();

  if (message === "") return;

  appendMessage("user", message);
  input.value = "";

  showTypingIndicator();

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  });

  hideTypingIndicator();

  const data = await response.json();
  appendMessage("bot", data.response);
}

function appendMessage(sender, message) {
  const chatWindow = document.getElementById("chat-window");
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", sender);
  msgDiv.innerText = message;
  chatWindow.appendChild(msgDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function showTypingIndicator() {
  const chatWindow = document.getElementById("chat-window");
  const typingDiv = document.createElement("div");
  typingDiv.id = "typing-indicator";
  typingDiv.classList.add("message", "bot");
  typingDiv.innerHTML = `<span class="dot-flashing"></span>`;
  chatWindow.appendChild(typingDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function hideTypingIndicator() {
  const typingDiv = document.getElementById("typing-indicator");
  if (typingDiv) {
    typingDiv.remove();
  }
}

// "Enter to send" feature
document.getElementById("user-input").addEventListener("keydown", function (event) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
});
