from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from api.dependencies import get_db, oauth2_scheme

router = APIRouter()

@router.get("/view_section")
def view_section(section: str ,records : int = 3, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    pass

@router.post("/insert_section")
def insert_section(text: str, section: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    pass

@router.patch('/edit_section')
def update_section(new_text: str, token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db)):
    pass

@router.delete('/delete_section')
def delete_section(text: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    pass