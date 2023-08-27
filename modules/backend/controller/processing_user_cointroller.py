from injectable import injectable, autowired, Autowired

from modules.health.user.processing_user_service import ProcessingUserService


@injectable(singleton=True)
class ProcessingUserController:
    @autowired
    def __init__(self, processing_user_service: Autowired(ProcessingUserService)):
        self.processing_user_service = processing_user_service

    def do(self):
        self.processing_user_service
