from pydantic import BaseModel

class Books(BaseModel):
    id: int
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