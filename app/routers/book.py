from fastapi import FastAPI,Header, status, APIRouter
from fastapi.exceptions import HTTPException
from typing import Optional, List
from app.data import books
from app.schemas import *




router = APIRouter()

@router.get("/",response_model = List[Books])
async def get_books():
    return books

@router.get("/{book_id}",response_model = Books)
async def get_book(book_id:int)-> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status.HTTP_404_NOT_FOUND,detail="book not found")
        


@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Books)-> dict:
    book = book_data.model_dump()
    if not book in books:
        books.append(book)
        return book 
    else:
        raise HTTPException(status.HTTP_409_CONFLICT,detail="book already created")


@router.delete("/{book_id}")
async def delete_book(book_id:int)-> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"response":"succesfully deleted"}
    raise HTTPException(status.HTTP_404_NOT_FOUND,detail="book not found")


@router.put("/{book_id}")
async def update_book(book_id:int,book_data:Book_update)-> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["date"] = book_data.date
            book["pages"] = book_data.pages
            book["language"] = book_data.language
            return {"response":"succesfully updated"}
    raise HTTPException(status.HTTP_404_NOT_FOUND,detail="book not found")