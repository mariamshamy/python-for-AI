from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
load_dotenv()
client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)
# Create a chat session with your system instruction
chat = client.chats.create(
model="gemini-3.6-flash",
config=types.GenerateContentConfig(
system_instruction="You are a helpful coding tutor."
)
)
# Send your message through the chat object
response = chat.send_message("Explain what a list comprehension is.")
print(response.text)
