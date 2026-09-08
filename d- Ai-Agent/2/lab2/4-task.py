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

    reply = model.invoke(prompt).content

    return {
        "draft": reply,
        "status": "drafted"
    }


def approval_node(
    state: SupportState
) -> Command[Literal["send", "cancel"]]:

    approved = interrupt({
        "question": "Approve sending this message?",
        "draft": state["draft"],
    })

    return Command(
        goto="send" if approved else "cancel"
    )


def send_node(state: SupportState):
    print("SENT:", state["draft"])

    return {
        "status": "sent"
    }


def cancel_node(state: SupportState):
    return {
        "status": "cancelled"
    }


# -----------------------------
# Build the graph
# -----------------------------

builder = StateGraph(SupportState)

builder.add_node("draft", draft_node)
builder.add_node("approval", approval_node)
builder.add_node("send", send_node)
builder.add_node("cancel", cancel_node)


builder.add_edge(START, "draft")
builder.add_edge("draft", "approval")

builder.add_edge("send", END)
builder.add_edge("cancel", END)


# -----------------------------
# Compile with checkpointer
# -----------------------------

graph = builder.compile(
    checkpointer=InMemorySaver()
)


# -----------------------------
# Same thread must be reused
# -----------------------------

config = {
    "configurable": {
        "thread_id": "ticket-2001"
    }
}


initial_state = {
    "request": "My order is three days late",
    "draft": "",
    "status": "new"
}


# -----------------------------
# First invocation -> PAUSE
# -----------------------------

paused = graph.invoke(
    initial_state,
    config
)

print(paused["__interrupt__"])


# -----------------------------
# Human approves -> RESUME
# -----------------------------

final = graph.invoke(
    Command(resume=True),
    config
)

print(final)
print(final["status"])