from google.genai import Client
import base64
import datetime


client = Client(api_key="AIzaSyAwyO4PDOCNd7xc5ou2vgMo9y2LqWB6WO8")

with open("poem.jpg", "rb") as f:
    image_bytes = f.read()

prompt = f"""
You are analyzing a photograph of a poem.

TASKS:
1. Read the poem from the image.
2. Explain its meaning in clear, natural language.
3. Identify the poem’s central theme.
4. Describe any emotional tone or symbolism.
5. Rate your confidence from 0–100%.

RULE:
If your confidence is below 60%, shorten your explanation and say:
'Confidence is low — interpretation may be inaccurate.'
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": base64.b64encode(image_bytes).decode("utf-8")
                    }
                }
            ]
        }
    ]
)

print("\n--- AI INTERPRETATION ---\n")
print(response.text)

print("\n--- SUCCESS TEST ---")
print("Success if:")
print("- The interpretation changes depending on the time of day.")
print("- The AI includes a confidence rating.")
print("- The rule triggers when confidence < 60%.")
