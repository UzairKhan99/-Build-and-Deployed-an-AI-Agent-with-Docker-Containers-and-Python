import os
from typing import Any

import psycopg
from fastapi import FastAPI
from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    message: str = Field(..., min_length=1, examples=["Research why going outside is good."])


class AgentResponse(BaseModel):
    status: str
    message: str
    input: str | None = None


app = FastAPI(
    title="Dockerized AI Agent API",
    description="FastAPI backend for the AI agent application.",
    version="0.1.0",
)


def get_database_url() -> str | None:
    return os.getenv("DATABASE_URL")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "AI Agent API is running"}


@app.get("/health")
def health_check() -> dict[str, Any]:
    database_url = get_database_url()

    if not database_url:
        return {
            "status": "ok",
            "database": "not_configured",
        }

    try:
        with psycopg.connect(database_url, connect_timeout=3) as conn:
            with conn.cursor() as cursor:
                cursor.execute("select 1")
                cursor.fetchone()
    except Exception as exc:
        return {
            "status": "degraded",
            "database": "unreachable",
            "detail": str(exc),
        }

    return {
        "status": "ok",
        "database": "reachable",
    }


@app.post("/agent/run", response_model=AgentResponse)
def run_agent(request: AgentRequest) -> AgentResponse:
    return AgentResponse(
        status="success",
        message="Agent endpoint is ready. Add LangChain/LangGraph workflow logic here.",
        input=request.message,
    )
