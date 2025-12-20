from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def ask_ai(question):
    prompt = (
        "Answer in maximum 2 short sentences. "
        "Use simple words. "
        f"Question: {question}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
