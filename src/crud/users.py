import uuid
from sqlmodel import Session, select
from db.models import User
from db.schema import UserInDB
from utils import hash_password

def create_user(db: Session, user: UserInDB):
    new_user = User(user_id=str(uuid.uuid4()), user_name=user.user_name, email=user.email, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.exec(statement=statement).first()

def get_user_by_id(db: Session, user_id: str):
    statement = select(User).where(User.user_id == user_id)
    return db.exec(statement=statement).first()