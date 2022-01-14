from typing import List, Optional

from pydantic import BaseModel


class Schemas:
    class BookBase(BaseModel):
        title: str
        author_name: str
        year: int
        genre: Optional[str] = None
        description: Optional[str] = None

    class BookCreate(BookBase):
        pass

    class Book(BookBase):
        id: int
        author_id: int

        class Config:
            orm_mode = True
