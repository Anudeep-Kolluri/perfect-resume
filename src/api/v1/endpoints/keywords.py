from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from api.dependencies import get_db, oauth2_scheme

router = APIRouter()

@router.post('/insert_keyword')
def insert_keyword(text: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    pass

@router.get('/get_vector')
def get_key_vec(text: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    pass