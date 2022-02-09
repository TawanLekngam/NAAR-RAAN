from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget
from models.model import Model


class Controller(ABC):

    def __init__(self, view: QWidget, model: Model) -> None:
        self.view = view
        self.model = model

    def show_page(self) -> None:
        self.view.showFullScreen()
