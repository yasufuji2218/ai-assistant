import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL = "gemini-3.5-flash"

_client =genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ask(system: str, message: str) -> str:
    """指示(system)と発言(message)を渡し、返事の文章を返す。"""
    response = _client.models.generate_content(
        model=MODEL,
        contents=message,
        config=types.GenerateContentConfig(system_instruction=system),
    )
    return response.text
