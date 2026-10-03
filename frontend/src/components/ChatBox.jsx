import { useState } from "react";
import api from "../services/api";
import { useDispatch } from "react-redux";
import { setSelectedInteraction } from "../features/interactions/interactionSlice";

function ChatBox() {
  const dispatch = useDispatch();

  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const currentMessage = message;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: currentMessage,
      },
    ]);

    setMessage("");

    try {
          const response = await api.post("/chat/", {
        message: currentMessage,
    });

    console.log("CHAT RESPONSE:", response.data);

      // Update Redux selected interaction
      // This refreshes InteractionForm automatically
      if (response.data.interaction) {
        dispatch(
          setSelectedInteraction(response.data.interaction)
        );
      }

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: response.data.response,
        },
      ]);

    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Something went wrong.",
        },
      ]);
    }
  };

  return (
    <div className="chat-box">
      <div className="chat-header">
        <h2>
          <span className="robot-icon">🤖</span>
          AI Assistant
        </h2>

        <p>
          Log interaction details here via chat
        </p>
      </div>

      <div className="chat-messages">

        {messages.length === 0 && (
          <div className="welcome-message">
            Describe an HCP interaction and I can log or retrieve information for you.
          </div>
        )}

        {messages.map((item, index) => (
          <div
            key={index}
            className={`message ${
              item.sender === "user"
                ? "user-message"
                : "ai-message"
            }`}
          >
            {item.text}
          </div>
        ))}

      </div>

      <div className="chat-input-area">

        <input
          type="text"
          value={message}
          placeholder="Describe interaction..."
          onChange={(e) =>
            setMessage(e.target.value)
          }
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button onClick={sendMessage}>
          Send
        </button>

      </div>

    </div>
  );
}

export default ChatBox;