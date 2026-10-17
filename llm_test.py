from dotenv import load_dotenv
from google import genai

load_dotenv()          #loads .env into the environment
client = genai.Client()   #finds GEMINI_API_KEY on its own

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence.",
)

print(response.text)
