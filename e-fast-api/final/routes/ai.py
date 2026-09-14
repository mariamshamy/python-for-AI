from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from database import engine
from errors import AppError
from models import Document
from schemas import (
    AIAnalysisResponse,
    AgentAskRequest,
    AgentAskResponse,
)
from services.agent_service import ask_document_agent
from services.gemini_service import analyze_document


router = APIRouter(tags=["ai"])


@router.post(
    "/documents/{document_id}/analyze",
    response_model=AIAnalysisResponse,
    summary="Analyze one document with Gemini",
    responses={
        404: {"description": "Document not found"},
        502: {"description": "AI analysis failed"},
    },
)
def analyze_stored_document(document_id: int):
    with Session(engine) as db:
        doc = db.get(Document, document_id)

        if doc is None:
            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

        try:
            analysis = analyze_document(doc.content)
        except Exception:
            raise AppError(
                code="ai_analysis_failed",
                message="Document analysis is temporarily unavailable.",
                status_code=502,
            )

        doc.ai_summary = analysis.summary
        db.commit()

        return analysis


@router.post(
    "/agent/ask",
    response_model=AgentAskResponse,
    summary="Ask the read-only document agent",
    responses={502: {"description": "Agent failed"}},
)
def ask_agent(payload: AgentAskRequest):
    try:
        answer = ask_document_agent(payload.message)
    except Exception:
        raise AppError(
            code="agent_failed",
            message="The document agent is temporarily unavailable.",
            status_code=502,
        )

    return {"answer": answer}
