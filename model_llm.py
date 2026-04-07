import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_review(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "user", "content": f"Summarize this product review in 1 line:\n{text}"}
        ],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()