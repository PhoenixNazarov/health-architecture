from typing import Any

from pydantic import BaseModel


class ViewParamsOrder(BaseModel):
    field: Any
    desc: bool = False
