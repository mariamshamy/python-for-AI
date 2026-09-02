from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import json

load_dotenv()
client = genai.Client()


# ----------------- 1 --------------------------------------
# api_key = os.environ["GEMINI_API_KEY"]
# print("Key loaded:", api_key[:4] + "...")

# ----------------- 2 --------------------------------------
# response = client.models.generate_content(
#  model="gemini-3.7-flash",
#  contents="Say hello in one short sentence."  # or "Give me one productivity tip."
# )
# print(response.text)

# ----------------- 3 --------------------------------------
# chat_session = client.chats.create(
#     model="gemini-3.7-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a friendly assistant."
#     )
# )


# def ask(user_input):
#     response = chat_session.send_message(user_input)
#     return response.text


# print(ask("My favorite color is blue."))
# print(ask("What is my favorite color?"))

# ----------------- 4 --------------------------------------


# def summarize(text):
#     response = client.models.generate_content(
#         model="gemini-3.7-flash",
#         contents=text,
#         config=types.GenerateContentConfig(
#             system_instruction=(
#                 "Summarize the text. Return JSON with a summary string and a key_points array of strings."),
#             response_mime_type="application/json"
#         )
#     )
#     return json.loads(response.text)


# result = summarize("the odyssey")
# print(result["summary"])
# for point in result["key_points"]:
#     print("-", point)

# ----------------- 5 --------------------------------------
stream = client.models.generate_content_stream(
    model="gemini-3.7-flash",
    contents="Write a short poem about the ocean."
)
for chunk in stream:
    if chunk.text:
        print(chunk.text, end="", flush=True)
print()