from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, text

from database import get_session, init_db
from chat.routing import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title=" AI Agent API",
    description="FastAPI backend for the AI agent application.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(router, prefix="/api/chats")




@app.get("/")
def home():
    return {"message": "AI Agent API is running"}


@app.get("/health")
def health(session: Session = Depends(get_session)):
    try:
        session.exec(text("SELECT 1"))
        return {"status": "ok", "database": "reachable"}

    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database is unreachable")
