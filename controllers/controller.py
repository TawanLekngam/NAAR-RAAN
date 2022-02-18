from abc import ABC
from PySide6.QtWidgets import QWidget
from models.model import Model
from views.menu_order import Menu_order


class Controller:

    def __init__(self, view: QWidget, model: Model) -> None:
        self.view = view
        self.model = model

    def show_page(self) -> None:
        self.view.showFullScreen()


class MenuOrderController(Controller):

    def __init__(self):
        Controller.__init__(self, Menu_order(), None)
