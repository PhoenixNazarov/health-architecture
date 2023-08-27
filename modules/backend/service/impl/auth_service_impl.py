from modules.backend.service.auth_service import AuthService

from modules.commons.service.impl.base_service_impl import BaseServiceImpl

from injectable import injectable


@injectable(singleton=True)
class AuthServiceImpl(AuthService, BaseServiceImpl[AuthService]):
    pass
