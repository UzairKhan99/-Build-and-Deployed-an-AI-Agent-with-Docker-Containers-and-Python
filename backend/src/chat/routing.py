from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, text

from database import get_session
from chat.models import AgentRun


router = APIRouter()

class AgentRequest(BaseModel):
    message: str = Field(..., min_length=1)


class AgentResponse(BaseModel):
    id:int
    message:str
    response:str
    status:str


@router.get('/')
def home():
    return {"message":"Ai Agent  is OLALALALA"}

@router.get("/db-test")
def db_test(session: Session = Depends(get_session)):
    try:
        result = session.exec(text("SELECT DATABASE()")).first()
        return {"connected_database": result[0]}

    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database connection failed")


@router.post("/agent/run", response_model=AgentResponse)
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
        message=agent_run.message,
        response=agent_run.response,
    )
