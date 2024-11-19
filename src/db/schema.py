from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    userid: str

class UserForm(BaseModel):
    user_name: str
    email: EmailStr
    password: str

class UserInDB(UserBase):
    user_name: str
    email: EmailStr
    password: str

class Text(UserBase):
    text: str
    section: str

class Keyword(UserBase):
    keyword: str

class Token(BaseModel):
    access_token: str
    token_type: str
