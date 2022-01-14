from functools import wraps
from typing import Dict, List

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from library_service.controllers.books import Controller
from library_service.models.books import Base
from library_service.models.db import engine, session
from library_service.schemas.books import Schemas

Base.metadata.create_all(bind=engine)

controller = Controller()
schemas = Schemas()

router = APIRouter()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@router.get("/books/home")
async def book_root():
    try:
        result = controller.get_root()
        print("print", result)
        return {
            "status": "success",
            "data": "Hello from book root",
            "controller_data": result,
        }

    except Exception as e:
        return {"status": "error", "error": str(e)}


@router.post("/author/{author_id}/books/", response_model=schemas.Book)
async def add_book(
    author_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
) -> schemas.Book:

    db_book = controller.create_book(db=db, book=book, author_id=author_id)
    print("db_book", db_book)
    return db_book


@router.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)) -> schemas.Book:
    db_book = controller.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.get("/books/", response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)) -> List[schemas.Book]:
    books = controller.get_books(db=db)
    return books
