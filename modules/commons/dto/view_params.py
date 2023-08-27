from typing import Optional

from pydantic import BaseModel
from .view_params_filter import ViewParamsFilter
from .view_params_order import ViewParamsOrder


class ViewParams(BaseModel):
    count: Optional[int]
    page: Optional[int]

    filters: list[ViewParamsFilter]
    orders: list[ViewParamsOrder]


class ViewParamsBuilder:
    def __init__(self):
        self.count = None
        self.page = None
        self.filters: list[ViewParamsFilter] = []
        self.orders: list[ViewParamsOrder] = []

    def set_count(self, count: int):
        self.count = count

    def set_page(self, page: int):
        self.page = page

    def add_filter(self, filter: ViewParamsFilter):
        self.filters.append(filter)

    def add_order(self, order: ViewParamsOrder):
        self.orders.append(order)

    def build(self) -> ViewParams:
        return ViewParams(
            count=self.count,
            page=self.page,
            filters=self.filters,
            orders=self.orders
        )
