from sqlalchemy import Column, Text
from sqlmodel import Field, SQLModel


class AgentRun(SQLModel, table=True):
    __tablename__ = "agent_runs"

    id: int | None = Field(default=None, primary_key=True)
    message: str = Field(sa_column=Column(Text, nullable=False))
    response: str = Field(sa_column=Column(Text, nullable=False))
    status: str = Field(default="success", max_length=50)
