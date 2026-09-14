# SmartDoc AI — Lab 6 Cross-Course Capstone

## 1. Install

```powershell
python -m pip install -r requirements.txt
```

## 2. Configure Gemini

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace:

```text
GEMINI_API_KEY=replace_me
```

with your real Gemini API key.

Never commit `.env`.

## 3. Verify migration

```powershell
python -m alembic current
```

Expected current revision:

```text
0002_add_ai_summary
```

If needed:

```powershell
python -m alembic upgrade head
```

## 4. Run

```powershell
python -m uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/openapi.json

## 5. Main endpoints

- `GET /health`
- `GET /documents`
- `POST /documents`
- `GET /documents/{id}`
- `PUT /documents/{id}`
- `DELETE /documents/{id}`
- `POST /documents/upload`
- `POST /documents/{id}/analyze`
- `POST /agent/ask`

## 6. Upload test

In Swagger open `POST /documents/upload` and choose
`sample_upload.txt`.

Only `text/plain` is accepted.

## 7. Gemini analysis

Create or use an existing document, then call:

```text
POST /documents/1/analyze
```

The response should contain:

- `summary`
- `key_points`
- `category`
- `suggested_priority`

Only the summary is saved into `Document.ai_summary`.

## 8. Read-only agent

Example request:

```json
{
  "message": "Find the API notes and tell me their key idea"
}
```

The agent may only use these tools:

- `list_documents_tool`
- `get_document_tool`
- `search_documents_tool`

The Python application validates and executes the tool calls.
The model does not directly access SQLite.

## 9. curl

From Windows CMD:

```cmd
curl_tests.cmd
```

## 10. Postman

Import:

- `SmartDoc_AI.postman_collection.json`
- `SmartDoc_AI.postman_environment.json`

Select the `SmartDoc AI Local` environment.

For the upload-error requirement, use Swagger or add a Postman
multipart request with a non-text file and confirm HTTP 400.

## 11. Contract matrix

Fill the `Actual` and `Pass/Fail` columns in:

```text
contract_verification_matrix.csv
```

## 12. AI-assisted review

See:

```text
AI_ASSISTED_REVIEW.md
```

Review/edit the note so it matches the diff you actually reviewed.
