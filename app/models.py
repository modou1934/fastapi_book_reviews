from sqlmodel import SQLModel,Field,Column
from datetime import datetime, date
from sqlalchemy import text
from typing import Optional
from sqlalchemy import DateTime
from pydantic.networks import EmailStr


class Book(SQLModel,table=True):
    id: Optional[int] = Field(nullable=False,primary_key=True)
    title: str
    author: str
    date: str
    pages: int
    language: str
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=text("NOW()"), 
            nullable=False
        )
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=text("NOW()"), 
            nullable=False
        )
    )

class User(SQLModel,table=True):
    id: Optional[int] = Field(nullable=False,primary_key=True)
    username: str
    email: EmailStr
    password: str
    is_verified: bool = False
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=text("NOW()"), 
            nullable=False
        )
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=text("NOW()"), 
            nullable=False
        )
    )

