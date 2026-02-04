from google import genai

client = genai.Client(api_key="AIzaSyBQIP3QN4ZkCDVM84B0A6vDIfeqXP7fR_0")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)