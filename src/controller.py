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


class BC(Controller):
    """
    Base controller
    connect to another view
    """
    __v: BaseView

    def __init__(self, v: QWidget = None, m: Model = None, u: User = None):
        Controller.__init__(self, v, m)
        __current_sview: Controller = None

    def setup_interface(self) -> None:
        """
        check user access level and setup interface for user (admin or staff).
        """
        pass

    def change_sview(self):
        pass


class LIC(Controller):
    """
    Login controller.
    verify user
    """
    __v: LoginView
    __m: LoginModel

    def __init__(self, v: QWidget = None, m: Model = None):
        Controller.__init__(self, v, m)


class MOC(Controller):
    """
    MenuOrder Controller.
    """
    __v: MenuOrderView
    __m: MenuOrderModel

    def __init__(self, v: QWidget = None, m: Model = None):
        Controller.__init__(self, v, m)

class ALC(Controller):
    """
    AuditLog Controller
    """
    __v: AuditLogView
    __m: AuditLogModel
    