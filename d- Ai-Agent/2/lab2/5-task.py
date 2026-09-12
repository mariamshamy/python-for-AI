from typing import TypedDict, Literal

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command, interrupt


# --------------------------------
# Gemini setup
# --------------------------------

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash"
)


# --------------------------------
# Shared State
# --------------------------------

class SupportState(TypedDict):
    request: str
    draft: str
    status: str


# --------------------------------
# 1. Draft node
# Model-backed node
# --------------------------------

def draft_node(state: SupportState):

    prompt = (
        f"Draft a concise support response for: "
        f"{state['request']}"
    )

    response = model.invoke(prompt)

    # .text gives us only the model text
    reply = response.text

    return {
        "draft": reply,
        "status": "drafted"
    }


# --------------------------------
# 2. Approval node
# Human-in-the-loop
# --------------------------------

def approval_node(
    state: SupportState
) -> Command[Literal["send", "cancel"]]:

    decision = interrupt({
        "question": "Approve sending this message?",
        "draft": state["draft"],
    })

    # --------------------------------
    # Simple True / False decision
    # --------------------------------

    if isinstance(decision, bool):

        return Command(
            goto="send" if decision else "cancel"
        )

    # --------------------------------
    # Dictionary decision
    # Example:
    # {
    #     "approved": True,
    #     "edited_text": "..."
    # }
    # --------------------------------

    approved = decision.get("approved", False)

    if not approved:
        return Command(
            goto="cancel"
        )

    edited_text = decision.get("edited_text")

    # Human approved AND changed the draft
    if edited_text:
        return Command(
            goto="send",
            update={
                "draft": edited_text
            }
        )

    # Human approved without editing
    return Command(
        goto="send"
    )


# --------------------------------
# 3. Send node
# Simulated sensitive action
# --------------------------------

def send_node(state: SupportState):

    print("\nSENT:")
    print(state["draft"])

    return {
        "status": "sent"
    }


# --------------------------------
# 4. Cancel node
# --------------------------------

def cancel_node(state: SupportState):

    print("\nMessage was NOT sent.")

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
# Edges
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
# Initial state
# --------------------------------

initial_state = {
    "request": "My order is three days late",
    "draft": "",
    "status": "new"
}


# ================================================
# TEST 1: REJECT
# ================================================

print("----- TEST 1: REJECTION -----")

config_reject = {
    "configurable": {
        "thread_id": "ticket-2002"
    }
}


# First invocation -> pauses at approval
paused = graph.invoke(
    initial_state,
    config_reject
)

print("\nApproval request:")
print(paused["__interrupt__"])


# Human rejects
rejected = graph.invoke(
    Command(resume=False),
    config_reject
)

print("\nFinal status:")
print(rejected["status"])


# ================================================
# TEST 2: EDIT DRAFT + APPROVE
# ================================================

print("\n\n----- TEST 2: EDIT + APPROVE -----")

config_edit = {
    "configurable": {
        "thread_id": "ticket-2003"
    }
}


# New thread -> pauses again at approval
paused = graph.invoke(
    initial_state,
    config_edit
)

print("\nOriginal draft:")
print(paused["__interrupt__"])


# Human edits the draft and approves it
human_decision = {
    "approved": True,
    "edited_text": (
        "We apologize for the delay. "
        "Your order is being reviewed and "
        "we will provide an update shortly."
    )
}


edited_result = graph.invoke(
    Command(resume=human_decision),
    config_edit
)


print("\nFinal status:")
print(edited_result["status"])

print("\nFinal draft:")
print(edited_result["draft"])