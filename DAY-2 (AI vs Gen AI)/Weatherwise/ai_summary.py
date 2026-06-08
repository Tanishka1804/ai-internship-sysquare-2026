import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.4
)


def generate_summary(weather):

    prompt = f"""
You are WeatherWise AI.

Generate a short weather summary.

Weather Details:
City: {weather['city']}
Temperature: {weather['temperature']}°C
Feels Like: {weather['feels_like']}°C
Humidity: {weather['humidity']}%
Condition: {weather['condition']}

Rules:
- Maximum 2-3 sentences.
- Friendly and conversational.
- Mention whether outdoor activities are suitable.
- Keep the response concise.
"""

    response = llm.invoke(prompt)

    return response.content     