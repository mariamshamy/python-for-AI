from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
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

    reply = model.invoke(prompt).text

    return {
        "draft": reply,
        "status": "drafted"
    }


def finalize_node(state: SupportState):
    if state["draft"]:
        return {"status": "approved"}

    return {"status": "rejected"}


builder = StateGraph(SupportState)

builder.add_node("draft", draft_node)
builder.add_node("finalize", finalize_node)

builder.add_edge(START, "draft")
builder.add_edge("draft", "finalize")
builder.add_edge("finalize", END)

graph = builder.compile(
    checkpointer=InMemorySaver()
)

config = {
    "configurable": {
        "thread_id": "ticket-1001"
    }
}

result = graph.invoke(
    {
        "request": "My order is three days late",
        "draft": "",
        "status": "new"
    },
    config
)

print(result)
print(result["status"])
