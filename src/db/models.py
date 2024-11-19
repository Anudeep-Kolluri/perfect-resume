from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    user_id: str = Field(primary_key=True)
    user_name: str
    email: str
    password: str

class Text(SQLModel, table=True):
    user_id: str = Field(foreign_key="user.user_id", primary_key=True) 
    text_content: str = Field(primary_key=True)
    section: str

class Keyword(SQLModel,table=True):
    user_id: str = Field(foreign_key="user.user_id", primary_key=True)
    keyword: str = Field(primary_key=True)
    




