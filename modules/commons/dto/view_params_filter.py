from typing import Any

from pydantic import BaseModel


class ViewParamsFilter(BaseModel):
    field: Any
    value: Any
