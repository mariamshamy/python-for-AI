import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


# --------------------------------
# Load environment variables
# --------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")


# --------------------------------
# Configure Gemini for CrewAI
# --------------------------------

gemini_llm = LLM(
    model="gemini/gemini-3.8-flash",
    api_key=api_key,
    temperature=1.0
)


# --------------------------------
# Agent 1: Support Analyst
# --------------------------------

analyst = Agent(
    role="Support Analyst",
    goal="Draft a factual response",
    backstory="You inspect the customer request carefully.",
    llm=gemini_llm
)


# --------------------------------
# Agent 2: Quality Reviewer
# --------------------------------

reviewer = Agent(
    role="Quality Reviewer",
    goal="Check the response for clarity and risk",
    backstory="You never approve unsupported claims.",
    llm=gemini_llm
)


# --------------------------------
# Task 1: Draft response
# --------------------------------

draft_task = Task(
    description=(
        "Draft a response for this support request: "
        "'My order is three days late.'"
    ),
    expected_output="A concise customer-facing draft.",
    agent=analyst
)


# --------------------------------
# Task 2: Review response
# --------------------------------

review_task = Task(
    description=(
        "Review the response produced by the Support Analyst. "
        "Check it for clarity, factual accuracy, and unsupported claims. "
        "Return a corrected final response."
    ),
    expected_output="A final approved response.",
    agent=reviewer
)


# --------------------------------
# Create Crew
# --------------------------------

crew = Crew(
    agents=[
        analyst,
        reviewer
    ],
    tasks=[
        draft_task,
        review_task
    ],
    process=Process.sequential
)


# --------------------------------
# Run Crew
# --------------------------------

result = crew.kickoff()

print(result)