from abc import (ABC)
from PySide6.QtWidgets import (QWidget)

from views import *
from models import *


class Controller:

    def __init__(self, view: QWidget, model: Model) -> None:
        self.view = view
        self.model = model

    def show_page(self) -> None:
        self.view.showFullScreen()


class MenuOrderController(Controller):

    def __init__(self):
        Controller.__init__(self, Menu_order(), MenuModel())


class LogInController(Controller):

    def __init__(self):
        Controller.__init__(self, Log_in(), None)
        self.view.login_button_emit(lambda: print("Clicked"))
