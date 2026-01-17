from fastapi import FastAPI,Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from app.routers import book
from .schemas import *
from contextlib import asynccontextmanager
from app.db.main import engine
from app.db.main import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await engine.dispose()

version = "v1"
app = FastAPI(title="Bookly",version=version,description="Rest API fo book review web service",lifespan=lifespan)
app.include_router(book.router,prefix=f"/api/{version}/books",tags=["books"])



@app.get("/")
async def read_root():
    return {"Response": "Hello World"}

@app.get("/greet/")
async def greet(name:Optional[str] = "User",age:int=0)-> dict:
    return {"message":f"Hello {name}","age":f"{age}"}


@app.get("/create_book/")
async def greet(book_data:Books):
    return {"title":f"{book_data.title}","author":f"{book_data.author}"}

@app.get("/get_headers",status_code = 201)
async def get_headers(accept:str=Header(None),content_type: str = Header(None),user_agent: str = Header(None),host: str = Header(None)):
    request= {}
    request["Accept"]= accept
    request["Content-Type"] = content_type
    request["User-Agent"] = user_agent
    request["Host"] = host
    return request

