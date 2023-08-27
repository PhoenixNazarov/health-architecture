from typing import TypeVar, Generic

from abc import ABC, abstractmethod

Entity = TypeVar("Entity")


class BaseService(Generic[Entity], ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Entity:
        """ find model T by id """

    @abstractmethod
    def count_by_view_params(self, view_params: ViewParams) -> int:
        """ count, order, filter """

    @abstractmethod
    def find_by_view_params(self, view_params: ViewParams) -> list[Entity]:
        """ find, order, filter """

    @abstractmethod
    def count_by_key(self, key, val) -> int:
        """ count model T by keys: ?_id with id """

    @abstractmethod
    def find_by_key(self, key, val) -> list[Entity]:
        """ find model T by keys: ?_id with id """

    @abstractmethod
    def count_by_keys(self, key, vals: list) -> int:
        """ count model T by keys: ?_id with ids"""

    @abstractmethod
    def find_by_keys(self, key, vals: list) -> list[Entity]:
        """ find model T by keys: ?_id with ids"""

    @abstractmethod
    def count_all(self) -> int:
        """ count all T models"""

    @abstractmethod
    def find_all(self) -> list[Entity]:
        """ find all T models"""

    @abstractmethod
    def save(self, entity: Entity) -> Entity:
        """ save model """

    @abstractmethod
    def save_all(self, entities: list[Entity]) -> list[Entity]:
        """ save all models """

    @abstractmethod
    def remove(self, entity: Entity) -> Entity:
        """ remove model """

    @abstractmethod
    def remove_all(self, entities: list[Entity]) -> list[Entity]:
        """ remove all models """
