from sqlalchemy import Text
from sqlmodel import Field, SQLModel


class AgentRun(SQLModel, table=True):
    __tablename__ = "agent_runs"

    id: int | None = Field(default=None, primary_key=True)
    message: str = Field(sa_type=Text)
    response: str = Field(sa_type=Text)
    status: str = Field(default="success", max_length=50)
