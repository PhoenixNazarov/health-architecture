from injectable import injectable


@injectable(singleton=True)
class ProcessingUserService:
    def __init__(self):
        pass
