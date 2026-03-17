import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("API_KEY" )
)


def ask_ai(question):

    completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    messages=[
        {
            "role": "user",
            "content":f"Your are a chatbot. Always answare in English Language. Question:{question} " 
        }
    ],
    )
    responce = completion.choices[0].message.content
    return responce