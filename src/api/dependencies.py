from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pymilvus import MilvusClient
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

DATABASE_PATH = os.getenv('database_path')

def get_db():
    db = MilvusClient(DATABASE_PATH)
    try:
        yield db
    finally:
        db.close()
