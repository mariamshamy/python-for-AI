import json
import logging

from google import genai
from google.genai import types
from sqlalchemy import or_
from sqlalchemy.orm import Session
from pydantic import ValidationError

from database import engine
from models import Document
from schemas import (
    GetDocumentArgs,
    ListDocumentsArgs,
    SearchDocumentsArgs,
)
from settings import GEMINI_API_KEY, GEMINI_MODEL, MAX_STEPS


logger = logging.getLogger("smartdoc.agent")


def list_documents_tool() -> str:
    """List available documents with id, title, and priority only."""
    with Session(engine) as db:
        rows = db.query(Document).order_by(Document.id).all()
        data = [
            {
                "id": row.id,
                "title": row.title,
                "priority": row.priority,
            }
            for row in rows
        ]
        return json.dumps(data, ensure_ascii=False)


def get_document_tool(document_id: int) -> str:
    """Get one stored document by a positive integer document_id."""
    with Session(engine) as db:
        doc = db.get(Document, document_id)

        if doc is None:
            return json.dumps(
                {"error": "Document not found"},
                ensure_ascii=False,
            )

        data = {
            "id": doc.id,
            "title": doc.title,
            "content": doc.content,
            "priority": doc.priority,
            "description": doc.description,
            "ai_summary": doc.ai_summary,
        }
        return json.dumps(data, ensure_ascii=False)


def search_documents_tool(query: str) -> str:
    """Search stored documents by text matching title or numeric id."""
    with Session(engine) as db:
        filters = [Document.title.ilike(f"%{query}%")]

        if query.isdigit():
            filters.append(Document.id == int(query))

        rows = (
            db.query(Document)
            .filter(or_(*filters))
            .order_by(Document.id)
            .all()
        )

        data = [
            {
                "id": row.id,
                "title": row.title,
                "priority": row.priority,
            }
            for row in rows
        ]
        return json.dumps(data, ensure_ascii=False)


TOOLS = {
    "list_documents_tool": list_documents_tool,
    "get_document_tool": get_document_tool,
    "search_documents_tool": search_documents_tool,
}

TOOL_SCHEMAS = {
    "list_documents_tool": ListDocumentsArgs,
    "get_document_tool": GetDocumentArgs,
    "search_documents_tool": SearchDocumentsArgs,
}


def _get_client() -> genai.Client:
    if not GEMINI_API_KEY:
        raise RuntimeError("Gemini is not configured.")
    return genai.Client(api_key=GEMINI_API_KEY)


def ask_document_agent(message: str) -> str:
    client = _get_client()

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=(
                        "You are a read-only SmartDoc AI agent. "
                        "Answer only from stored document data obtained through tools. "
                        "Never modify or delete data. "
                        "If the tools do not support an answer, say so clearly.\n\n"
                        f"User request: {message}"
                    )
                )
            ],
        )
    ]

    config = types.GenerateContentConfig(
        tools=[
            list_documents_tool,
            get_document_tool,
            search_documents_tool,
        ],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        ),
    )

    for _step in range(MAX_STEPS):
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=contents,
            config=config,
        )

        part = response.candidates[0].content.parts[0]
        call = part.function_call

        if call is None:
            return response.text or "No final answer was returned."

        if call.name not in TOOLS:
            logger.warning("tool=%s success=false reason=not_whitelisted", call.name)
            observation = {"error": "Requested tool is not allowed."}
        else:
            try:
                schema = TOOL_SCHEMAS[call.name]
                validated = schema.model_validate(dict(call.args or {}))

                result = TOOLS[call.name](**validated.model_dump())
                observation = {"result": result}

                logger.info("tool=%s success=true", call.name)

            except ValidationError:
                observation = {"error": "Invalid tool arguments."}
                logger.warning(
                    "tool=%s success=false reason=invalid_arguments",
                    call.name,
                )

            except Exception:
                observation = {"error": "Tool execution failed."}
                logger.exception("tool=%s success=false", call.name)

        contents.append(response.candidates[0].content)
        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=call.name,
                        response=observation,
                    )
                ],
            )
        )

    raise RuntimeError("Agent exceeded MAX_STEPS.")
