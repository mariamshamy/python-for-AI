\
@echo off

echo === HEALTH 200 ===
curl -i http://127.0.0.1:8000/health

echo.
echo === GET DOCUMENTS 200 ===
curl -i http://127.0.0.1:8000/documents

echo.
echo === POST VALID 201 ===
curl -i -X POST http://127.0.0.1:8000/documents ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"SmartDoc Notes\",\"content\":\"FastAPI with AI\",\"priority\":2,\"description\":\"Lab 6 curl test\"}"

echo.
echo === POST INVALID 422 ===
curl -i -X POST http://127.0.0.1:8000/documents ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"x\",\"content\":\"\",\"priority\":99}"

echo.
echo === GET MISSING 404 ===
curl -i http://127.0.0.1:8000/documents/999999

echo.
echo === ANALYZE DOCUMENT 1 ===
curl -i -X POST http://127.0.0.1:8000/documents/1/analyze

echo.
echo === ASK AGENT ===
curl -i -X POST http://127.0.0.1:8000/agent/ask ^
-H "Content-Type: application/json" ^
-d "{\"message\":\"List the available documents\"}"
