from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_order(order_id: int) -> dict:
    db = {104: {"status": "delayed", "total": 850}}
    return db.get(order_id, {"status": "not_found"})


def calculate_shipping(weight_kg: float, zone: str) -> dict:
    rate = {"local": 20, "regional": 35}.get(zone.lower(), 50)
    return {"cost": round(weight_kg * rate, 2), "currency": "EGP"}


config = types.GenerateContentConfig(
    tools=[get_order, calculate_shipping],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True),
)
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="What is the status of order 104?",
    config=config,
)
call = response.candidates[0].content.parts[0].function_call
print(call.name)
print(call.args)
