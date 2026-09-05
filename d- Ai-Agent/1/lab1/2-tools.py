


from pydantic import BaseModel
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class OrderLookup(BaseModel):
    order_id: int = Field(gt=0)
class ShippingQuote(BaseModel):
    weight_kg: float = Field(gt=0, le=100)
    zone: str


def get_order(order_id: int) -> dict:
    db = {104: {"status": "delayed", "total": 850}}
    return db.get(order_id, {"status": "not_found"})


def calculate_shipping(weight_kg: float, zone: str) -> dict:
    rate = {"local": 20, "regional": 35}.get(zone.lower(), 50)
    return {"cost": round(weight_kg * rate, 2), "currency": "EGP"}


print(get_order(**OrderLookup(order_id=104).model_dump()))
