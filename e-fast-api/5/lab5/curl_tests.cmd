\
@echo off
echo === GET all ===
curl -i http://127.0.0.1:8000/documents

echo.
echo === POST valid ===
curl -i -X POST http://127.0.0.1:8000/documents ^
 -H "Content-Type: application/json" ^
 -d "{\"title\":\"Curl Doc\",\"content\":\"capstone\",\"priority\":3,\"description\":\"Lecture 5\"}"

echo.
echo === GET one (change ID if needed) ===
curl -i http://127.0.0.1:8000/documents/1

echo.
echo === PUT one ===
curl -i -X PUT http://127.0.0.1:8000/documents/1 ^
 -H "Content-Type: application/json" ^
 -d "{\"title\":\"Updated Curl Doc\",\"content\":\"updated\",\"priority\":4,\"description\":\"Lecture 5 update\"}"

echo.
echo === DELETE one ===
curl -i -X DELETE http://127.0.0.1:8000/documents/1

echo.
echo === GET missing -> 404 ===
curl -i http://127.0.0.1:8000/documents/999999

echo.
echo === POST invalid -> 422 ===
curl -i -X POST http://127.0.0.1:8000/documents ^
 -H "Content-Type: application/json" ^
 -d "{\"title\":\"x\",\"content\":\"\",\"priority\":99}"
