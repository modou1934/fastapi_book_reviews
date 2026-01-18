from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class Books(BaseModel):
    id: Optional[int] 
    title: str
    author: str
    date: str
    pages: int
    language: str


class Book_create(BaseModel):
    title: str
    author: str
    date: str
    pages: int
    language: str


class Book_update(BaseModel):
    title: str
    author: str
    date: str
    pages: int
    language: str

class Book_response(Book_create):
    id: int
    created_at: datetime
    updated_at: datetime