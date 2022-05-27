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
        self.__root: Application = root

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


class HomePage(Controller):

    def __init__(self, view: QWidget, model: Model, admin: bool = False):
        super().__init__(view, model)
        self.__admin_access = admin

    def set_button_listenner(self, btn: QPushButton, function) -> None:
        btn.clicked.connect(function)


class AccountPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class LogPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
