# Lab 5 — FastAPI Capstone

## Install
```powershell
python -m pip install -r requirements.txt
```

## 1. Verify migration
```powershell
python -m alembic current
```

If needed:
```powershell
python -m alembic upgrade head
```

## 2. Run API
```powershell
python -m uvicorn main:app --reload
```

Open:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/openapi.json

## 3. curl testing
From Windows CMD:
```cmd
curl_tests.cmd
```

Or run the commands inside `curl_tests.cmd` one by one.

## 4. Postman
Import:
- `Lab5_FastAPI.postman_collection.json`
- `Lab5_FastAPI.postman_environment.json`

Select the `Lab5 FastAPI Local` environment.

## 5. Contract matrix
Fill the `Actual` and `Pass/Fail` columns in:
`contract_verification_matrix.csv`

Expected codes:
- GET /documents -> 200
- POST valid -> 201
- POST invalid -> 422
- GET missing -> 404
- DELETE existing -> 200
