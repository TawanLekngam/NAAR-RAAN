"""
    controller
"""


from PySide6.QtWidgets import (QWidget)

from views import *
from models import *



class Controller:
    def __init__(self, view: QWidget = None, model: Model = None):
        self.view = view
        self.model = model

    def show_page(self) -> None:
        self.view.showFullScreen()


class LogInPage(Controller):
    view: LoginView
    model: LoginModel

    def __init__(self, view: LoginView = None, model: LoginModel = None):
        Controller.__init__(self, view, model)
        self.view.login_button_emit(self.logIn)

    def logIn(self):
        if self.model.login_verify(self.view.lineEdit_username.text(), self.view.lineEdit_password.text()):
            self.view.close()


class MenuOrderPage(Controller):
    view: MenuOrderView
    model: MenuOrderModel

    def __init__(self, view: MenuOrderView = None, model: MenuOrderModel = None):
        Controller.__init__(self, view, model)

class OrderTrackingPage(Controller):
    view: OrderTrackingView
    model: OrderTrackingModel

    def __init__(self, view: OrderTrackingView = None, model: OrderTrackingModel = None):
        Controller.__init__(self,view, model)

class TargetRevenuePage(Controller):
    view: TargetRevenueView
    model: TargetRevenueModel

    def __init__(self, view: TargetRevenueView = None, model: TargetRevenueModel = None):
        Controller.__init__(self,view, model)
