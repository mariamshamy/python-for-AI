Lab 4 FastAPI

Install:
python -m pip install fastapi uvicorn sqlalchemy alembic pydantic

Task 1:
cd task1_connect_alembic
alembic current

Task 2:
cd task2_migration
alembic upgrade head
alembic current

Task 3:
cd task3_apirouter
alembic upgrade head
python -m uvicorn main:app --reload
Open http://127.0.0.1:8000/docs

Task 4:
cd task4_docs
alembic upgrade head
python -m uvicorn main:app --reload
Open:
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/openapi.json
