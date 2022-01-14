from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from library_service.models.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(50), nullable=False)
    role = Column(
        String(50), nullable=False, default="reader"
    )  # reader, librarian, author, super
    books = relationship("Book", back_populates="author")