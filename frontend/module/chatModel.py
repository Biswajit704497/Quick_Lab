from google import genai
from dotenv import load_dotenv
from google.genai.errors import ClientError
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def ask_ai(question):

    try:
        prompt = (
            "You are a friendly Health Chatbot. "
            "Answer in a maximum of 2 short sentences using very simple words. "
            "Give general health tips only. "
            "Do NOT give medical diagnosis, prescriptions, or emergency advice. "
            "If the question is serious, say to consult a doctor. "
            "Be polite, calm, and supportive. "
            f"Question: {question}")


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

