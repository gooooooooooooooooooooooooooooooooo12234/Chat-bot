
import ollama
from app.services.chat.rag import retrieve_event_info

# Load the chatbot model (Trix-Bot-Chat)
MODEL_NAME = ""

def handle_chat_query(query: str):
    event_info = retrieve_event_info(query)
    
    system_prompt = (
    
)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": system_prompt}]
    )
    
    return response["message"]["content"]

