from typing import TypedDict
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


class SupportState(TypedDict):
    request: str
    draft: str
    status: str


def draft_node(state: SupportState):
    prompt = f"Draft a concise support response for: {state['request']}"

    reply = model.invoke(prompt).content

    return {
        "draft": reply,
        "status": "drafted"
    }


def finalize_node(state: SupportState):
    if state["draft"]:
        return {"status": "approved"}

    return {"status": "rejected"}
