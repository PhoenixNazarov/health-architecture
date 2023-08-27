from pydantic import BaseModel


class DbConfig(BaseModel):
    ip: str
    port: int
    user: str
    password: str
    name: str


DB_REQUISITES: dict[str, DbConfig] = {}
