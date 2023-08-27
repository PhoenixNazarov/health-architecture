from ..base_service import BaseService, Entity
from ...dto.view_params import ViewParams


class BaseServiceImpl(BaseService):
    def find_by_id(self, id: int) -> Entity:
        pass

    def count_by_view_params(self, view_params: ViewParams) -> int:
        pass

    def find_by_view_params(self, view_params: ViewParams) -> list[Entity]:
        pass

    def count_by_key(self, key, val) -> int:
        pass

    def find_by_key(self, key, val) -> list[Entity]:
        pass

    def count_by_keys(self, key, vals: list) -> int:
        pass

    def find_by_keys(self, key, vals: list) -> list[Entity]:
        pass

    def count_all(self) -> int:
        pass

    def find_all(self) -> list[Entity]:
        pass

    def save(self, entity: Entity) -> Entity:
        pass

    def save_all(self, entities: list[Entity]) -> list[Entity]:
        pass

    def remove(self, entity: Entity) -> Entity:
        pass

    def remove_all(self, entities: list[Entity]) -> list[Entity]:
        pass

