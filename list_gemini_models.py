
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

try:
    print("Models available to your API key:\n")

    for model in client.models.list():
        name = model.name or ""
        actions = getattr(model, "supported_actions", None) or []

        if "generateContent" in actions:
            print(name, "| Supported actions:", actions)

except Exception as exc:
    print("Could not retrieve model list.")
    print(type(exc).__name__, exc)

