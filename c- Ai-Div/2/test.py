import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# 1. Define multiple local tools


def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divides a by b."""
    return a / b if b != 0 else float("nan")


# Map function names to Python functions for dynamic execution
available_tools = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}
# 2. Register all tools in the chat configuration
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        tools=[add, subtract, multiply, divide],
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(
                mode="ANY"  # Forces the model to pick a tool call
            )
        )
    )
)
# Step 1: Send a prompt requiring a specific tool
response = chat.send_message("What is 100 divided by 4?")
# Step 2: Extract requested tool call
tool_call = response.function_calls[0]
tool_name = tool_call.name
tool_args = tool_call.args
print("Model requested tool:", tool_name)
print("Arguments extracted:", tool_args)
# Step 3: Dynamically execute the requested function
if tool_name in available_tools:
    result = available_tools[tool_name](**tool_args)
    print("Execution result:", result)
