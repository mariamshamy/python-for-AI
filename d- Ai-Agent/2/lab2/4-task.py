from typing import TypedDict, Literal
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command, interrupt


# --------------------------------
# Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# Initialize Gemini model
# --------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


# --------------------------------
# Shared graph state
# --------------------------------

class SupportState(TypedDict):
    request: str
    draft: str
    status: str


# --------------------------------
# Draft node
# --------------------------------

def draft_node(state: SupportState):

    prompt = (
        f"Draft a concise support response for: "
        f"{state['request']}"
    )

    response = model.invoke(prompt)

    reply = response.text

    return {
        "draft": reply,
        "status": "drafted"
    }


# --------------------------------
# Approval node
# --------------------------------

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


# --------------------------------
# Simulated send_email node
# --------------------------------

def send_node(state: SupportState):

    print("\nSENT:")
    print(state["draft"])

    return {
        "status": "sent"
    }


# --------------------------------
# Cancel node
# --------------------------------

def cancel_node(state: SupportState):

    print("\nMessage was cancelled.")

    return {
        "status": "cancelled"
    }


# --------------------------------
# Build graph
# --------------------------------

builder = StateGraph(SupportState)

builder.add_node("draft", draft_node)
builder.add_node("approval", approval_node)
builder.add_node("send", send_node)
builder.add_node("cancel", cancel_node)


# --------------------------------
# Add graph edges
# --------------------------------

builder.add_edge(START, "draft")
builder.add_edge("draft", "approval")

builder.add_edge("send", END)
builder.add_edge("cancel", END)


# --------------------------------
# Compile with checkpointer
# --------------------------------

graph = builder.compile(
    checkpointer=InMemorySaver()
)


# --------------------------------
# Thread configuration
# --------------------------------

config = {
    "configurable": {
        "thread_id": "ticket-2001"
    }
}


# --------------------------------
# Initial state
# --------------------------------

initial_state = {
    "request": "My order is three days late",
    "draft": "",
    "status": "new"
}


# --------------------------------
# First run -> PAUSE
# --------------------------------

paused = graph.invoke(
    initial_state,
    config
)

print("\nApproval request:")
print(paused["__interrupt__"])


# --------------------------------
# Human approves -> RESUME
# --------------------------------

final = graph.invoke(
    Command(resume=True),
    config
)


print("\nFinal state:")
print(final)

print("\nFinal status:")
print(final["status"])