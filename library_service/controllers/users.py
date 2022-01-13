from typing import Dict

from sqlalchemy.orm import Session

from library_service.models.users import User
from library_service.schemas.users import Schemas


schemas = Schemas()


class Controller:
    def get_root(self):
        return {"status": "success", "data": "Hello from user root controller"}

    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(name=user.name, email=user.email, password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def verify_password(self, plain_password: str, hashed_password: str):
        return plain_password + "notreallyhashed" == hashed_password

    def modify_role(self, db: Session, user_id: int, role: schemas.Role):
        user = self.get_user(db=db, user_id=user_id)
        print(role.role)
        user.role = role.role
        db.commit()
        db.refresh(user)
        return user
