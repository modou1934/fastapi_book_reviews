from fastapi import FastAPI,Header, status, APIRouter, Depends
from fastapi.exceptions import HTTPException
from typing import Optional, List
from app.schemas import *
from app.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService


router = APIRouter()
book_service = BookService()

@router.get("/", response_model=List[Books])
async def get_books(session: AsyncSession = Depends(get_session)):
    return await book_service.get_all_books(session)

@router.get("/{book_id}", response_model=Books)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    return await book_service.get_book_by_id(session, book_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book_response)
async def create_book(book_data: Book_create, session: AsyncSession = Depends(get_session)):
    return await book_service.create_book(session, book_data)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, session: AsyncSession = Depends(get_session)):
    await book_service.delete_book(session, book_id)
    return None

@router.put("/{book_id}", response_model=Book_response)
async def update_book(book_id: int, book_data: Book_update, session: AsyncSession = Depends(get_session)):
    return await book_service.update_book(session, book_data, book_id)