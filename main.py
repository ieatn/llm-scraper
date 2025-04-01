# dont forget to conda activate llm-scraper and switch interpreter to llm-scraper
print("Hello, World!")
import base64
import os
from google import genai
from google.genai import types
# fixes env variable 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Debugging: Print the API key (make sure to remove this in production)
print(f"GEMINI_API_KEY: {gemini_api_key}")

def generate():
    client = genai.Client(
        api_key=gemini_api_key,
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="Hello, World!"),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
