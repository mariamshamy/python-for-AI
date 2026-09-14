from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

app = FastAPI()
engine = create_engine("sqlite:///documents.db")

class Base(DeclarativeBase):
    pass
