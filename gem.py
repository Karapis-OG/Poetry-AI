from google.genai import Client
import base64

# Insert your API key
client = Client(api_key="AIzaSyBQIP3QN4ZkCDVM84B0A6vDIfeqXP7fR_0")

# Load image bytes
with open("poem.jpg", "rb") as f:
    image_bytes = f.read()

prompt = """
You are analyzing a photograph of a poem.
1. Read the poem from the image.
2. Explain its meaning in clear, natural language.
3. Identify the poem’s central theme.
4. Describe any emotional tone or symbolism.
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

print(response.text)
