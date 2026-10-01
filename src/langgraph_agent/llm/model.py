from langchain_openai import ChatOpenAI
from ..config.settings import OPENAI_API_KEY


def get_model():
    return ChatOpenAI(
        model="gpt-4.1-mini", temperature=0, openai_api_key=OPENAI_API_KEY
    )
