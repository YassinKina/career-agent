import React, { useState } from "react";

export default function CareerChat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  async function sendMessage() {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    setInput("");

    try {
      const response = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: input }),
      });

      const data = await response.json();

      const aiMsg = { sender: "ai", text: data.response || "No response" };
      setMessages((prev) => [...prev, aiMsg]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "ai", text: "Error: Could not get response" },
      ]);
    }
  }

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20, fontFamily: "Arial" }}>
      <h2>Career AI Advisor</h2>

      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: 8,
          padding: 10,
          minHeight: 300,
          overflowY: "auto",
          marginBottom: 10,
          backgroundColor: "#f9f9f9",
        }}
      >
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              textAlign: msg.sender === "user" ? "right" : "left",
              margin: "8px 0",
            }}
          >
            <span
              style={{
                display: "inline-block",
                padding: "8px 12px",
                borderRadius: 16,
                backgroundColor: msg.sender === "user" ? "#007bff" : "#e5e5ea",
                color: msg.sender === "user" ? "white" : "black",
                maxWidth: "80%",
                wordWrap: "break-word",
              }}
            >
              {msg.text}
            </span>
          </div>
        ))}
      </div>

      <textarea
        rows={3}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your question here..."
        style={{ width: "100%", padding: 8, borderRadius: 8, border: "1px solid #ccc" }}
      />

      <button
        onClick={sendMessage}
        style={{
          marginTop: 10,
          padding: "10px 20px",
          backgroundColor: "#007bff",
          border: "none",
          borderRadius: 8,
          color: "white",
          cursor: "pointer",
          fontSize: 16,
        }}
      >
        Send
      </button>
    </div>
  );
}
