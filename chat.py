import gradio as gr
import requests
import os

FASTAPI_URL = "https://chat-app-backend-3-n7qo.onrender.com/chat"

def chat(message):
    response = requests.post(
        FASTAPI_URL,
        json={"message": message}
    )

    if response.status_code == 200:
        return response.json()["answer"]
    else:
        return "Error connecting to FastAPI"

demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        label="Ask Gemini",
        placeholder="Type your question..."
    ),
    outputs=gr.Textbox(label="Gemini Response"),
    title="Gemini AI Chatbot",
    description="Gradio + FastAPI + Gemini"
)



if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
