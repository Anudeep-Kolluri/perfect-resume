from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db.session import init_db
from api.v1.endpoints.auth import router as auth_router
from api.v1.endpoints.users import router as user_router
from api.v1.endpoints.texts import router as texts_router
from api.v1.endpoints.keywords import router as keyword_router
import uvicorn


origins = ["*"]

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {"Welcome": "To Zero"}


app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user_router, prefix="/api/v1/user", tags=["user"])
app.include_router(texts_router, prefix="/api/v1/texts", tags=["texts"])
app.include_router(keyword_router, prefix="/api/v1/keywords", tags=["keywords"])


if __name__ == "__main__":
    uvicorn.run(app="app:app", host="127.0.0.1", port=8000, reload=True) 