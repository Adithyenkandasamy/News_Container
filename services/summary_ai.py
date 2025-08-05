import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Setup Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def summarize_article(text: str) -> str:
    prompt = f"Summarize the following article in simple and short points:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
