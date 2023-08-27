from modules.commons.entity.base_entity import BaseEntity


class Auth(BaseEntity):
    __tablename__ = 'auth'

    user_id: int
