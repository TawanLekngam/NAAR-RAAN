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
            self.receipt_page = ReceiptPage(ReceiptView(), ReceiptModel())
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
        self.total = 0.0

        self.initialize()

    def initialize(self) -> None:
        self.order_list = OrderList(self, OrderListView(), OrderListModel())

        self.view.insert_view(self.order_list.view, 0)

    def increase_total(self, value: float):
        self.total += value
        self.view.set_total(self.total)

    def decrease_total(self, value: float):
        self.total -= value
        self.view.set_total(self.total)


class OrderList(Controller):
    "sub controller"
    parent: OrderPage
    view: OrderListView
    model: OrderListModel

    def __init__(self, parent: Controller, view: QWidget, model: Model):
        super().__init__(view, model)
        self.parent = parent
        self.load_item()

    def load_item(self, filter: str = None) -> None:
        item_list = self.model.get_all_products()
        for item in item_list:
            self.view.add_widget_to_scrollarea(self.__create_item_widget(item))

    def __create_item_widget(self, item) -> OrderListItemView:
        order_listitem = OrderListItem(
            self.parent, OrderListItemView(), item)
        return order_listitem.view


class OrderListItem(Controller):
    parent: OrderPage
    view: OrderListItemView

    def __init__(self, parent: Controller, view: QWidget, item: object):
        super().__init__(view, None)
        self.parent = parent
        self.item = item

        self.view.set_itemname(self.item.get_name())
        self.view.set_button_listener(lambda: self.on_click())

    def on_click(self) -> None:
        if isinstance(self.item, Drink):
            drink_detail = DrinkDetail(
                self.parent, DrinkDetailView(), self.item)
            self.parent.view.insert_view(drink_detail.view, 1)

        else:
            bakery_detail = BakeryDetail(
                self.parent, BakeryDetailView(), self.item)
            self.parent.view.insert_view(bakery_detail.view, 1)

        self.parent.view.move_to_index(1)


class DrinkDetail(Controller):
    parent: OrderPage
    view: DrinkDetailView
    item: Drink

    def __init__(self, parent: Controller, view: QWidget, item: object):
        super().__init__(view, None)
        self.parent = parent
        self.item = item

        self.view.set_name(self.item.get_name() + " " + self.item.get_price())
        self.view.set_cancel_button_listener(lambda: self.cancel_order())
        self.view.set_add_button_listener(lambda: self.add_order())

    def cancel_order(self) -> None:
        self.parent.view.stacked_widget.removeWidget(self.view)

    def add_order(self) -> None:
        curr_price = 0.0
        if self.view.get_drink_type() == "Hot":
            curr_price = self.item.get_hprice()
        elif self.view.get_drink_type() == "Cold":
            curr_price = self.item.get_cprice()
        elif self.view.get_drink_type() == "Blended":
            curr_price = self.item.get_bprice()

        order_item = OrderItem(self.view.get_detail(),
                               curr_price, parent=self.parent)
        self.parent.view.vBox.addWidget(order_item.view)
        self.parent.view.stacked_widget.removeWidget(self.view)


class BakeryDetail(Controller):
    parent: OrderPage
    view: BakeryDetailView
    item: Bakery

    def __init__(self, parent: Controller, view: QWidget, item: object):
        super().__init__(view, None)
        self.parent = parent
        self.item = item

        self.view.set_name(self.item.get_name() + " " +
                           str(self.item.get_price()))
        self.view.set_cancel_button_listener(lambda: self.cancel_order())
        self.view.set_add_button_listener(lambda: self.add_order())

    def cancel_order(self) -> None:
        self.parent.view.stacked_widget.removeWidget(self.view)

    def add_order(self) -> None:
        order_item = OrderItem(self.item.get_name()[0:12],
                               self.item.get_price(), parent=self.parent)
        self.parent.view.vBox.addWidget(order_item.view)
        self.parent.view.stacked_widget.removeWidget(self.view)


class OrderItem(Controller):
    parent: OrderPage
    view: OrderItemView

    def __init__(self, item_name: str, price: float = 0.0, quantity: int = 1, parent: Controller = None):
        super().__init__(OrderItemView(), None)
        self.parent = parent
        self.view.set_item_name(item_name)
        self.price = price
        self.quantity = quantity

        self.view.set_quantity(self.quantity)
        self.view.set_price_label(self.price * self.quantity)
        self.parent.increase_total(self.price)

        self.view.increase_button_listener(lambda: self.increase())
        self.view.decrease_button_listener(lambda: self.decrease())

    def increase(self):
        self.quantity += 1
        self.view.set_quantity(self.quantity)
        self.view.set_price_label(self.price * self.quantity)
        self.parent.increase_total(self.price)

    def decrease(self):
        if self.quantity <= 0:
            return
        self.quantity -= 1
        self.view.set_quantity(self.quantity)
        self.view.set_price_label(self.price * self.quantity)
        self.parent.decrease_total(self.price)
        if self.quantity <= 0:
            pass

    def total_price(self) -> float:
        return self.price * self.quantity


class LogPage(Controller):
    view: LogView
    model: LogModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.initialize()

    def initialize(self) -> None:
        log_list: list[Log] = self.model.get_all_logs()
        for log in log_list:
            self.view.add_log_to_scrollarea(self.__create_log_widget(log))

    def __create_log_widget(self, log: Log) -> LogItem:
        return LogItem(log.get_date(), log.get_time(), log.get_desc()[0:51])


class ReceiptPage(Controller):
    view: ReceiptView
    model: ReceiptModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.initialize()

    def initialize(self) -> None:
        receipt_list: list[Receipt] = self.model.get_all_receipt()
        for receipt in receipt_list:
            print(receipt)
            self.view.add_receipt_to_scrollarea(
                self.__create_receipt_widget(receipt))

    def __create_receipt_widget(self, receipt: Receipt) -> LogItem:
        return LogItem(receipt.get_date(), receipt.get_time(), receipt.get_desc()[0:51])


class AccountPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class MenuPage(Controller):

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
