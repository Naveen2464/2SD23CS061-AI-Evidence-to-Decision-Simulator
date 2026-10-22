
import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not api_key:
    raise SystemExit("ERROR: GEMINI_API_KEY is missing from .env")

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=(
            'Return a JSON object with one field: '
            '{"status": "ok"}'
        ),
        config={
            "response_mime_type": "application/json"
        },
    )

    result = json.loads(response.text)

    print("SUCCESS: Gemini API is working!")
    print("Model:", model)
    print("Response:", result)

except Exception as exc:
    print("Gemini API request failed.")
    print("Error type:", type(exc).__name__)
    print("Details:", exc)

