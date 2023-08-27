from modules.backend.controller.processing_user_cointroller import ProcessingUserController

controller = ProcessingUserController()


# @('/do', POST)
def do():
    controller.do()
