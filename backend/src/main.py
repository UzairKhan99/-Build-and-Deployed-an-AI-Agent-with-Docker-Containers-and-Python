from contextlib import asynccontextmanager
from typing import Any

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
    title="Dockerized AI Agent API",
    description="FastAPI backend for the AI agent application.",
    version="0.1.0",
    lifespan=lifespan,
)


class AgentRequest(BaseModel):
    message: str = Field(..., min_length=1, examples=["Research why going outside is good."])


class AgentResponse(BaseModel):
    id: int
    status: str
    message: str
    input: str


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "AI Agent API is running"}


@app.get("/health")
def health_check(session: Session = Depends(get_session)) -> dict[str, Any]:
    try:
        session.exec(text("SELECT 1")).one()
    except SQLAlchemyError as exc:
        return {
            "status": "degraded",
            "database": "unreachable",
            "detail": str(exc),
        }

    return {"status": "ok", "database": "reachable"}


@app.get("/db-test")
def db_test(session: Session = Depends(get_session)) -> dict[str, str | None]:
    result = session.exec(text("SELECT DATABASE()" بذ)).first()
    return {"connected_database": result[0] if result else None}


@app.post("/agent/run", response_model=AgentResponse)
def run_agent(
    request: AgentRequest,
    session: Session = Depends(get_session),
) -> AgentResponse:
    simple_response = "Agent request saved successfully. AI logic will be added later."
    agent_run = AgentRun(
        message=request.message,
        response=simple_response,
        status="success",
    )

    try:
        session.add(agent_run)
        session.commit()
        session.refresh(agent_run)
    except SQLAlchemyError as exc:
        session.rollback()
        raise HTTPException(status_code=503, detail="Could not save the agent run") from exc

    if agent_run.id is None:
        raise HTTPException(status_code=500, detail="Agent run was saved without an ID")

    return AgentResponse(
        id=agent_run.id,
        status=agent_run.status,
        message=simple_response,
        input=agent_run.message,
    )
