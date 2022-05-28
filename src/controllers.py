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
            self.view.hide_error_label()
        else:
            self.view.show_error_label()

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
        self.view.set_logout_button_listener(self.__root.move_to_login)
        self.__admin_access = (user.get_access_level() == "admin")
        self.initialize()

        # sub page
        self.order_page = None
        self.log_page = None
        self.receipt_page = None
        self.menu_page = None
        self.user_edit_page = None

    def initialize(self) -> None:
        self.order_page = OrderPage(OrderView(), OrderModel())
        self.view.stacked_widget.addWidget(self.order_page.view)
        self.view.set_home_button_listener(self.move_to_order_page)

        if self.__admin_access:
            self.view.show_admin_button()

            self.log_page = LogPage(LogView(), LogModel())
            self.receipt_page = ReceiptPage(ReceiptView(), ReceiptModel)
            self.menu_page = MenuPage(MenuView(), MenuModel())
            self.account_page = AccountPage(AccountView(), AccountModel())

            self.view.add_view(self.log_page.view)
            self.view.add_view(self.receipt_page.view)
            self.view.add_view(self.menu_page.view)
            self.view.add_view(self.account_page.view)

            self.view.set_log_button_listener(self.move_to_log_page)
            self.view.set_receipt_button_listener(self.move_to_receipt_page)
            self.view.set_menu_button_listener(self.move_to_menu_page)
            self.view.set_account_button_listener(self.move_to_account_page)

        else:
            self.view.hide_admin_button()

    def move_to_order_page(self) -> None:
        self.view.stacked_widget.setCurrentIndex(0)

    def move_to_log_page(self) -> None:
        if self.__admin_access:
            self.view.stacked_widget.setCurrentIndex(1)

    def move_to_receipt_page(self) -> None:
        if self.__admin_access:
            self.view.stacked_widget.setCurrentIndex(2)

    def move_to_menu_page(self) -> None:
        if self.__admin_access:
            self.view.stacked_widget.setCurrentIndex(3)

    def move_to_account_page(self) -> None:
        if self.__admin_access:
            self.view.stacked_widget.setCurrentIndex(4)


class OrderPage(Controller):
    view: OrderView
    model: OrderModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)

        # sub view
        self.order_list = None

        self.initialize()

    def initialize(self) -> None:
        self.order_list = OrderList(self, OrderListView(), OrderListModel())

        self.view.insert_view(self.order_list.view, 0)

    def move_to_drink_detail(self):
        pass

    def move_to_bakery_detail(self):
        pass


class OrderList(Controller):
    "sub controller"
    parent: OrderPage
    view: OrderListView
    model: OrderListModel

    def __init__(self, parent: Controller, view: QWidget, model: Model):
        super().__init__(view, model)
        self.__parent = parent

    def load_item(self, filter: str = None):
        item_list = list()


class OrderListItem(Controller):
    parent: OrderPage
    view: OrderListItemView

    def __init__(self, parent: Controller, view: QWidget, item: object):
        super().__init__(view, None)
        self.__parent = parent


class LogPage(Controller):
    view: LogView
    model: LogModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        # self.__root = root
        self.update_log()

    def update_log(self):
        self.view.add_view(self.model.get_all_logs())


class ReceiptPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class AccountPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class MenuPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
