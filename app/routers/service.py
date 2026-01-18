from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.models import Book
from app.schemas import Book_create,Book_update
from sqlalchemy import desc
from fastapi.exceptions import HTTPException

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def get_book_by_id(self, session: AsyncSession, book_id: int):
        statement = select(Book).where(Book.id == book_id)
        result = await session.exec(statement)
        book = result.first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    
    async def create_book(self, session: AsyncSession, book_data: Book_create):
        new_book = Book(**book_data.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book
    
    async def update_book(self, session: AsyncSession, book_data: Book_update, book_id: int):
        book_to_update = await self.get_book_by_id(session, book_id)
        
        update_data = book_data.model_dump()
        for key, value in update_data.items():
            setattr(book_to_update, key, value)
            
        session.add(book_to_update)
        await session.commit()
        await session.refresh(book_to_update)
        
        return book_to_update
    
    async def delete_book(self, session: AsyncSession, book_id: int):
        book_to_delete = await self.get_book_by_id(session, book_id)
        
        await session.delete(book_to_delete)
        await session.commit()
        return book_to_delete