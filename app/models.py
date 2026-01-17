from sqlmodel import SQLModel,Field,Column
from datetime import datetime
from sqlalchemy import text
from typing import Optional
from sqlalchemy import DateTime

class Book(SQLModel,table=True):
    id: Optional[int] = Field(nullable=False,primary_key=True)
    title: str
    author: str
    date: str
    pages: int
    language: str
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=text("NOW()"), 
            nullable=False
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=text("NOW()"), 
            nullable=False
        )
    )

def __repr__(self):
    return f"Book(id={self.id}, title={self.title}, author={self.author}, date={self.date}, pages={self.pages}, language={self.language}, created_at={self.created_at}, updated_at={self.updated_at})"