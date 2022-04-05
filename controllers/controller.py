from PySide6.QtWidgets import (QWidget)

from views import *
from models import *


class Controller:
    def __init__(self, view: QWidget = None, model: Model = None):
        self.view = view
        self.model = model

    def show_page(self) -> None:
        self.view.showFullScreen()


class LogInController(Controller):
    def __init__(self):
        Controller.__init__(self, LogInPage(), LogInModel())
        self.view: LogInPage
        self.model: LogInModel
        self.view.login_button_emit(self.logIn)
        self.show_page()

    def logIn(self):
        if self.model.login_verify(self.view.lineEdit_username.text(),self.view.lineEdit_password.text()):
            self.view.close()

class MenuOrderController(Controller):
    def __init__(self):
        Controller.__init__(self, MenuOrderPage(), MenuOrderModel())
        self.show_page()
