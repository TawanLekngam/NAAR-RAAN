from PySide6.QtWidgets import QWidget

from src.model import *
from src.view import *


class Controller:
    def __init__(self, v: QWidget = None, m: Model = None):
        self.__v = v  # view
        self.__m = m  # model

    def get_page(self) -> QWidget:
        return self.v

    def show_page(self) -> None:
        self.v.show()

    def showf_page(self) -> None:
        self.v.showFullScreen

    def update_view(self) -> None:
        self.v.update()

