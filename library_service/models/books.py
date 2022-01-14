from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from library_service.models.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    author_name = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    genre: Optional[str] = None
    description: Optional[str] = None
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="books")
