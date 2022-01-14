from typing import List, Optional

from pydantic import BaseModel

from library_service.schemas.books import Schemas as BookSchemas

books_schema = BookSchemas()


class Schemas:
    class UserBase(BaseModel):
        name: str
        email: str

    class UserCreate(UserBase):
        password: str

    class User(UserBase):
        id: int
        role: str = "reader"
        books: List[books_schema.Book] = []

        class Config:
            orm_mode = True

    class UserLogin(BaseModel):
        email: str
        password: str

    class Role(BaseModel):
        role: str
