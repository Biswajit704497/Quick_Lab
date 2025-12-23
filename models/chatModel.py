from google import genai
from dotenv import load_dotenv
from google.genai.errors import ClientError
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def ask_ai(question):

    try:
        prompt = (
            "Answer in maximum 2 short sentences. "
            "Use simple words. "
            "Behave like a Health CHat bot"
            f"Question: {question}"
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text
    except ClientError as e:
        if e.code == 429:
            return "⚠️ AI limit reached. Please wait and try again."
        elif e.code == 404:
            return "⚠️ Model not available. Check model name."
        else:
            return "⚠️ AI service error."


if __name__ == '__main__':
    print(ask_ai("hello"))

