from PySide6.QtWidgets import QStackedWidget

from .model import *
from .view import *
from .controllers import *


class Application(QStackedWidget):

    def __init__(self):
        QStackedWidget().__init__(self, None)
        self.setFixedSize(1920, 1080)
        self.setWindowTitle("Naar Raan")

        self.current_user = None

        # Login Page
        self.login_page = None

    def initialize_page(self) -> None:
        pass

    def set_current_user(self, user: User) -> None:
        self.current_user = user

    def start(self) -> None:
        "driver method."
        self.showFullScreen()
