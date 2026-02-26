from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME
import json

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are a structured AI response generator.

Always respond strictly in JSON format:

{
    "summary": "Brief summary",
    "key_points": ["Point 1", "Point 2", "Point 3"],
    "conclusion": "Final conclusion"
}

Do not add extra text outside JSON.
"""

def generate_structured_response(prompt: str, temperature: float = 0.7) -> str:

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=temperature,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content