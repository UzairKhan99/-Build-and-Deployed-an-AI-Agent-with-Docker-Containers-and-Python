from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, text

from database import get_session, init_db
from models import AgentRun


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


class AgentRequest(BaseModel):
    message: str = Field(..., min_length=1)


class AgentResponse(BaseModel):
    id: int
    status: str
    message: str
    input: str


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


@app.get("/db-test")
def db_test(session: Session = Depends(get_session)):
    try:
        result = session.exec(text("SELECT DATABASE()")).first()
        return {"connected_database": result[0]}

    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database connection failed")


@app.post("/agent/run", response_model=AgentResponse)
def run_agent(request: AgentRequest, session: Session = Depends(get_session)):
    response_message = "Agent request saved successfully. AI logic will be added later."

    agent_run = AgentRun(
        message=request.message,
        response=response_message,
        status="success",
    )

    try:
        session.add(agent_run)
        session.commit()
        session.refresh(agent_run)

    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=503, detail="Could not save the agent run")

    return AgentResponse(
        id=agent_run.id,
        status=agent_run.status,
        message=response_message,
        input=agent_run.message,
    )