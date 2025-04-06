async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
  
    if (message === "") return;
  
    appendMessage("user", message);
    input.value = "";
  
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: message })
    });
  
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
  