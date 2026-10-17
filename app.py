import gradio as gr
import os
from groq import Groq

# Initialize the Groq client using the secure environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def send_message(message, history):
    try:
        # Call the Groq API
        response = client.chat.completions.create(
            # Using the model that supports browser search and Indian languages
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant for Holy Cross School Indore. Answer accurately. You must understand and respond in Hindi and other Indian languages if asked.",
                },
                {"role": "user", "content": message},
            ],
            tools=[{"type": "browser_search"}],
            tool_choice="auto",
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Create the Gradio UI
demo = gr.ChatInterface(
    fn=send_message,
    title="Holy Cross School AI Assistant",
    description="Chat with an assistant that can search the web and speak Indian languages.",
)

if __name__ == "__main__":
    # Render provides a PORT environment variable. Replit defaults to 7860.
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
