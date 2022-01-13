from typing import Dict

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from library_service.controllers.users import Controller
from library_service.models.users import Base
from library_service.schemas.users import Schemas
from library_service.models.db import session, engine

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


@router.get("/users/home")
async def user_root():
    try:
        result = controller.get_root()
        print("print", result)
        return {
            "status": "success",
            "data": "Hello from user root",
            "controller_data": result,
        }

    except Exception as e:
        return {"status": "error", "error": str(e)}


@router.post("/users/", response_model=schemas.User)
async def add_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
) -> schemas.User:
    db_user = controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controller.create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> schemas.User:
    db_user = controller.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/email/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)) -> schemas.User:
    db_user = controller.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found by email")
    return db_user
