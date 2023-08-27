from injectable import autowired, Autowired, injectable
from sqlalchemy.testing.pickleable import User

from modules.backend.service.auth_service import AuthService


@injectable(singleton=True)
class AuthorizeService:
    @autowired
    def __init__(self,
                 auth_service: Autowired(AuthService)
                 ):
        self.auth_service = auth_service

    def authorize(self, auth_id: int) -> User:
        auth = self.auth_service.find_by_id(auth_id)

