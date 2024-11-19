from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pymilvus import MilvusClient
from openai import OpenAI
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

DATABASE_PATH = os.getenv('database_path')

def get_db():
    db = MilvusClient(DATABASE_PATH)
    try:
        yield db
    finally:
        db.close()

def init_openai_client(api_key: str):
    client = OpenAI(api_key)
    try:
        yield client
    finally:
        client.close()