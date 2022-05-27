from abc import ABC
from datetime import date
from PySide6.QtWidgets import QWidget

from models import *
from views import *


class Controller:
    view: QWidget
    model: Model

    def __init__(self, view: QWidget = None, model: Model = None):
        self.view = view
        self.model = model

    def open_page(self):
        if self.view is None:
            return
        self.view.show()


class LoginPage(Controller):
    view: LoginView
    model: LoginModel

    def __init__(self, root, view: QWidget, model: Model):
        super().__init__(view, model)
        self.view.set_login_button_listener(self.verify_login)
        self.__root = root

    def verify_login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        self.model.get_input(username, password)
        self.model.retrive_user(username)
        self.model.verify_login()

        if self.model.is_valid():
            self.model.set_current_user(username)
            self.set_current_user(self.get_current_user())
            self.__root.initialize_page()

    def get_current_user(self) -> User:
        return self.model.get_current_user()

    def set_current_user(self, user: User):
        self.__root.set_current_user(user)

    def clear_input_field(self) -> None:
        self.view.clear_info()


class HomePage(Controller):
    """master page"""

    view: HomeView
    model: HomeModel

    def __init__(self, root, view: QWidget, model: Model, user: User):
        super().__init__(view, model)
        self.__root = root
        self.view.set_username(user.get_username())
        self.__admin_access = (user.get_access_level() == "admin")

    def set_logout_button_listener(self) -> None:
        self.view.user_button.click.connect(self.__root.move_to_login)

    def set_button_listenner(self, btn: QPushButton, function) -> None:
        btn.clicked.connect(function)


class OrderPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class AccountPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class LogPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
