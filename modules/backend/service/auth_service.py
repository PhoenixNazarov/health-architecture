from abc import ABC

from modules.commons.service.base_service import BaseService
from modules.backend.entity.auth import Auth


class AuthService(BaseService[Auth], ABC):
    pass
