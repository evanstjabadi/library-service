from typing import Optional

from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: Optional[str] = None
    description: Optional[str] = None
