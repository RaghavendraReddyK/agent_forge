import os
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def get_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY missing! Make sure it's set in .env")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.0,
    )
    # return init_chat_model(
    #     model="gemini-2.5-flash",
    #     model_provider="google_genai",
    #     google_api_key=api_key,
    #     temperature=0.0,
    # )