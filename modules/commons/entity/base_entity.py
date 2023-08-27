from sqlmodel import SQLModel, Field


class BaseEntity(SQLModel):
    __table_args__ = {'extend_existing': True}

    id: int = Field(default=None, primary_key=True)
