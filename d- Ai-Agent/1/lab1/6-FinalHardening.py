import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field, ValidationError
from typing import Literal


# --------------------------------
# Gemini setup
# --------------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# --------------------------------
# Pydantic validation models
# --------------------------------

class OrderLookup(BaseModel):
    order_id: int = Field(gt=0)


class ShippingQuote(BaseModel):
    weight_kg: float = Field(gt=0, le=100)
    zone: Literal["local", "regional", "international"]


# --------------------------------
# Real tools
# --------------------------------

def get_order(order_id: int) -> dict:
    db = {
        104: {
            "status": "delayed",
            "total": 850
        }
    }

    return db.get(
        order_id,
        {"status": "not_found"}
    )


def calculate_shipping(weight_kg: float, zone: str) -> dict:
    rates = {
        "local": 20,
        "regional": 35,
        "international": 50
    }

    rate = rates[zone]

    return {
        "cost": round(weight_kg * rate, 2),
        "currency": "EGP"
    }


# --------------------------------
# Whitelisted tools
# --------------------------------

TOOLS = {
    "get_order": get_order,
    "calculate_shipping": calculate_shipping
}


# --------------------------------
# Validation schemas
# --------------------------------

TOOL_SCHEMAS = {
    "get_order": OrderLookup,
    "calculate_shipping": ShippingQuote
}


# --------------------------------
# Demo authorization
# --------------------------------

CURRENT_USER = {
    "username": "student",
    "role": "user"
}


def is_authorized(user, tool_name):
    allowed_tools = {
        "user": {
            "get_order",
            "calculate_shipping"
        }
    }

    return tool_name in allowed_tools.get(
        user["role"],
        set()
    )


# --------------------------------
# Sensitive tools
# --------------------------------

SENSITIVE_TOOLS = {
    # Example later:
    # "delete_order",
    # "send_email",
    # "refund_payment"
}


# --------------------------------
# Gemini configuration
# --------------------------------

config = types.GenerateContentConfig(
    tools=[
        get_order,
        calculate_shipping
    ],
    automatic_function_calling=
        types.AutomaticFunctionCallingConfig(
            disable=True
        )
)


contents = [
    types.Content(
        role="user",
        parts=[
            types.Part(
                text="What is the status of order 104?"
            )
        ]
    )
]


# --------------------------------
# Agent loop
# --------------------------------

MAX_STEPS = 5

for step in range(MAX_STEPS):

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=contents,
        config=config
    )

    part = response.candidates[0].content.parts[0]
    call = part.function_call

    # No tool call = final answer
    if not call:
        print(response.text)
        break


    print(f"\nStep {step + 1}")


    # 1) Is this tool allowed?
    if call.name not in TOOLS:
        raise ValueError(
            f"Blocked tool: {call.name}"
        )


    # 2) Are the arguments valid?
    try:
        schema = TOOL_SCHEMAS[call.name]

        validated = schema(**call.args)

        validated_args = validated.model_dump()

    except ValidationError:
        result = {
            "error": "Invalid tool arguments."
        }

        contents.append(
            response.candidates[0].content
        )

        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=call.name,
                        response={"result": result}
                    )
                ]
            )
        )

        continue


    # 3) Is the user authorized?
    if not is_authorized(
        CURRENT_USER,
        call.name
    ):
        result = {
            "error": "User is not authorized for this tool."
        }

        contents.append(
            response.candidates[0].content
        )

        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=call.name,
                        response={"result": result}
                    )
                ]
            )
        )

        continue


    # 4) Is this action sensitive?
    if call.name in SENSITIVE_TOOLS:
        result = {
            "error": "Human approval is required."
        }

        contents.append(
            response.candidates[0].content
        )

        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=call.name,
                        response={"result": result}
                    )
                ]
            )
        )

        continue


    # 5) Execute and check success
    start = time.perf_counter()
    success = False

    try:
        result = TOOLS[call.name](
            **validated_args
        )

        success = True

    except Exception:
        result = {
            "error": "Tool execution failed."
        }

    duration = time.perf_counter() - start


    # Log execution
    print("Tool:", call.name)
    print("Arguments:", validated_args)
    print("Duration:", round(duration, 4), "seconds")
    print("Success:", success)


    # 6) Safe observation
    safe_result = result

    print("Observation:", safe_result)


    # Add Gemini's tool request
    contents.append(
        response.candidates[0].content
    )


    # Add safe tool result
    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=call.name,
                    response={
                        "result": safe_result
                    }
                )
            ]
        )
    )


else:
    raise RuntimeError(
        "Agent exceeded MAX_STEPS"
    )