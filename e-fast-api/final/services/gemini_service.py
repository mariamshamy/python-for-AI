from google import genai
from google.genai import types

from schemas import AIAnalysisResponse
from settings import GEMINI_API_KEY, GEMINI_MODEL


def _get_client() -> genai.Client:
    if not GEMINI_API_KEY:
        raise RuntimeError("Gemini is not configured.")
    return genai.Client(api_key=GEMINI_API_KEY)


def analyze_document(content: str) -> AIAnalysisResponse:
    client = _get_client()

    prompt = f"""
Role:
You are a careful document analyst.

Task:
Summarize and classify the supplied document.

Context:
Use only the provided document content.
Do not invent missing facts.

Format:
Return JSON with exactly these fields:
summary, key_points, category, suggested_priority.

Document content:
---
{content}
---
""".strip()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AIAnalysisResponse,
        ),
    )

    if response.parsed is not None:
        return response.parsed

    return AIAnalysisResponse.model_validate_json(response.text)
