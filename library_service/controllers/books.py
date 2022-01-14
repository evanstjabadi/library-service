from sqlalchemy.orm import Session

from library_service.models.books import Book
from library_service.models.users import User
from library_service.schemas.books import Schemas

schemas = Schemas()


class Controller:
    def get_root(self):
        return {"status": "success", "data": "Hello from book root controller"}

    def get_books(self, db: Session, skip: int = 0, limit: int = 100):
        books = db.query(Book).offset(skip).limit(limit).all()
        return books

    def get_book(self, db: Session, book_id: int):
        return db.query(Book).get(book_id)

    def create_book(
        self, db: Session, book: schemas.BookCreate, author_id: int
    ) -> schemas.Book:
        db_book = Book(**book.dict(), author_id=author_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        print("fone")
        return db_book

    # def modify_book(self, db: Session, book_id: int, book: schemas.BookCreate):
    #     db_book = self.get_book(db=db, book_id=book_id)
    #     db_book.title = book.title
    #     db_book.author_name = book.author_name
    #     db_book.year = book.year
    #     db_book.genre = book.genre
    #     db_book.description = book.description
    #     db.commit()
    #     db.refresh(db_book)
    #     return db_book

    def delete_book(self, db: Session, book_id: int):
        db_book = self.get_book(db=db, book_id=book_id)
        db.delete(db_book)
        db.commit()
        return db_book
