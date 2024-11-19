import uuid
from sqlmodel import Session, select
from db.models import User
from db.schema import UserInDB
from utils import hash_password
import os
from dotenv import load_dotenv

load_dotenv()

USER_TABLE = os.getenv('user_table')

def create_user(db: Session, user: UserInDB):
    user_id = str(uuid.uuid4())
    # new_user = User(user_id=user_id, user_name=user.user_name, email=user.email, password=hash_password(user.password))
    new_m_data = [{"user_name": user.user_name, "user_id": user_id, "email": user.email, "openai_api_key": user.api_key, "password": hash_password(user.password), "vector": [1,2,3,4,5] }]
    db.insert(
        collection_name = USER_TABLE,
        data = new_m_data
    )
    '''
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    '''
    return {"created": "successfully"}


def get_user_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.exec(statement=statement).first()

def get_user_by_id(db: Session, user_id: str):
    statement = select(User).where(User.user_id == user_id)
    return db.exec(statement=statement).first()