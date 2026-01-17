from sqlmodel import create_engine,SQLModel
from app.config import settings
from app.models import Book
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine



engine= create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)



