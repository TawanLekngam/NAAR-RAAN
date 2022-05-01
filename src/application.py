import sys
from PySide6.QtWidgets import QApplication

from src.controller import *
from src.data.data_class import User

class Application:
    """
    main application
    """

    def __init__(self):
        self.root = QApplication(sys.argv)
        self.__current_user: User = None
        self.__current_cont: Controller = None

        """
        controller
        """
        self.__login_page = LIC()

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass