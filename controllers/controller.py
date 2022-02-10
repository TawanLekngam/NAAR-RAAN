from abc import ABC
from PySide6.QtWidgets import QWidget
from models.model import Model


class Controller(ABC):
    __administrator:bool

    def __init__(self, view: QWidget, model: Model,admin = False) -> None:
        self.view = view
        self.model = model
        self.__administrator = admin

    def show_page(self) -> None:
        self.view.showFullScreen()
