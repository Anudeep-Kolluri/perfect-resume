from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from api.dependencies import get_db
from crud.users import get_user_by_email
from utils import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.user_id})
    return {"access_token": access_token, "token_type": "Bearer"}