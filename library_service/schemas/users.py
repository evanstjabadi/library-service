from typing import List, Optional

from pydantic import BaseModel


class Schemas:
    class UserBase(BaseModel):
        name: str
        email: str

    class UserCreate(UserBase):
        password: str

    class User(UserBase):
        id: int
        role: str = "reader"

        class Config:
            orm_mode = True
