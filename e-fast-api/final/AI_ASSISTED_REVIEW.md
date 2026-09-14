# AI-Assisted Development Review

## Scoped prompt used

In `routes/ai.py`, add `POST /documents/{document_id}/analyze`.
Reuse the existing `Document` model and `Session(engine)` pattern.
Return 404 when the document is missing.
Do not change the existing CRUD routes.
Keep the response compatible with `AIAnalysisResponse`.

## Manual review note

I verified that the generated route keeps the existing direct
`with Session(engine) as db:` database pattern and returns 404 for a
missing document. I also checked that the Gemini API key is not
hardcoded and comes from `.env`. The route saves only the returned
summary to `Document.ai_summary`, rather than overwriting the source
document content. Finally, I checked that AI failures are converted to
a controlled application error instead of exposing a raw traceback.

> Edit this note if your own reviewed diff was different.
