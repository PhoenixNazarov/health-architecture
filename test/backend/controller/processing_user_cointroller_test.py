from unittest import TestCase
from unittest.mock import Mock

from modules.backend.controller.processing_user_cointroller import ProcessingUserController


class ProcessingUserControllerTest(TestCase):
    def setUp(self) -> None:
        self.processing_user_service = Mock()
        self.processing_user_controller = ProcessingUserController(
            processing_user_service=self.processing_user_service
        )

    def test_do(self):
        self.processing_user_controller.do()
