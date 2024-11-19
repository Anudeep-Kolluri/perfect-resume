from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from api.dependencies import oauth2_scheme, get_db
from utils import decode_jwt_token
from crud.users import get_user_by_id, get_user_by_email, create_user
from db.schema import UserForm
from jose import JWTError

router = APIRouter()

@router.post("/register")
def user_registration(user: UserForm, db: Session = Depends(get_db)):
    new_user = get_user_by_email(db, email=user.email)
    if new_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return create_user(db, user)

@router.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try: 
        payload = decode_jwt_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        user = get_user_by_id(db, user_id)
        if user is None:
            raise HTTPException(status_code=401, detail="User could not be found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
        

@router.delete("/delete")
def delete_user():
    pass

