from app.schemas.chat import ChatRequest
from app.utils.openai_client import ask_gpt


def generate_chat_response(data: ChatRequest) -> str:
    return ask_gpt(data.message)

