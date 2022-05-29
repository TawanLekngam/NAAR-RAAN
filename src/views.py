from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from sqlalchemy import func

from theme import Theme

"""
Log In page
"""


class LoginView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1920, 1080)

        label_logo = QLabel(self)
        label_logo.setObjectName("default_label")
        label_logo.setGeometry(QRect(846, 158, 252, 252))
        label_logo.setPixmap(QPixmap("src/asset/Image/logo.png"))

        label_username = QLabel("Username", self)
        label_username.setObjectName("default_label")
        label_username.setFont(Theme.DONGLE_BOLD_65)
        label_username.setGeometry(QRect(583, 537, 321, 72))

        label_password = QLabel("Password", self)
        label_password.setObjectName("default_label")
        label_password.setFont(Theme.DONGLE_BOLD_65)
        label_password.setGeometry(QRect(583, 706, 291, 72))

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("logIn_bar")
        self.lineEdit_username.setFont(Theme.DONGLE_BOLD_65)
        self.lineEdit_username.setGeometry(QRect(806, 520, 600, 80))

        self.error = QLabel("Incorrect username or password", self)
        self.error.setObjectName("default_label")
        self.error.setFont(Theme.DONGLE_REGULAR_50)
        self.error.setGeometry(QRect(836, 600, 600, 50))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("logIn_bar")
        self.lineEdit_password.setFont(Theme.DONGLE_REGULAR_50)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setGeometry(QRect(806, 685, 600, 80))

        self.login_button = QPushButton(self)
        self.login_button.setObjectName("logIn_button")
        self.login_button.setGeometry(QRect(860, 860, 200, 80))

        self.hide_error_label()
        self.setStyleSheet(Theme.get_stylesheet())

    def reset(self) -> None:
        self.clear_info()
        self.hide_error_label()

    def clear_info(self) -> None:
        self.lineEdit_username.setText("")
        self.lineEdit_password.setText("")

    def show_error_label(self) -> None:
        self.error.show()

    def hide_error_label(self) -> None:
        self.error.hide()

    def get_username(self) -> str:
        return self.lineEdit_username.text()

    def get_password(self) -> str:
        return self.lineEdit_password.text()

    def set_login_button_listener(self, function) -> None:
        self.login_button.clicked.connect(function)


"""
Home Page
"""


class HomeView(QWidget):

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1920, 1080)

        tab_frame = QFrame(self)
        tab_frame.setObjectName("tab_frame")
        tab_frame.setGeometry(QRect(0, 0, 1920, 100))

        self.user_button = QPushButton("User Name", tab_frame)
        self.user_button.setObjectName("user_button")
        self.user_button.setGeometry(QRect(1552, 0, 300, 100))
        self.user_button.setFont(Theme.DONGLE_BOLD_65)

        self.home_button = QPushButton(tab_frame)
        self.home_button.setObjectName("home_button")
        self.home_button.setGeometry(QRect(36, 0, 100, 100))

        self.log_button = QPushButton(tab_frame)
        self.log_button.setObjectName("log_button")
        self.log_button.setGeometry(QRect(136, 0, 100, 100))

        self.receipt_button = QPushButton(tab_frame)
        self.receipt_button.setObjectName("receipt_button")
        self.receipt_button.setGeometry(QRect(236, 0, 100, 100))

        self.menu_button = QPushButton(tab_frame)
        self.menu_button.setObjectName("menu_button")
        self.menu_button.setGeometry(QRect(336, 0, 100, 100))

        self.account_button = QPushButton(tab_frame)
        self.account_button.setObjectName("account_button")
        self.account_button.setGeometry(QRect(436, 0, 100, 100))

        stacked_frame = QFrame(self)
        stacked_frame.setObjectName("stacked_frame")
        stacked_frame.setGeometry(QRect(0, 100, 1920, 1060))

        self.stacked_widget = QStackedWidget(stacked_frame)
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setGeometry(QRect(0, -50, 1920, 1060))

        self.setStyleSheet(Theme.get_stylesheet())

    def add_view(self, view: QWidget) -> None:
        self.stacked_widget.addWidget(view)

    def show_admin_button(self) -> None:
        self.home_button.show()
        self.log_button.show()
        self.receipt_button.show()
        self.menu_button.show()
        self.account_button.show()

    def hide_admin_button(self) -> None:
        self.home_button.hide()
        self.log_button.hide()
        self.receipt_button.hide()
        self.menu_button.hide()
        self.account_button.hide()

    def set_username(self, username: str) -> None:
        self.user_button.setText(username)

    def set_logout_button_listener(self, function) -> None:
        self.user_button.clicked.connect(function)

    def set_home_button_listener(self, function) -> None:
        self.home_button.clicked.connect(function)

    def set_log_button_listener(self, function) -> None:
        self.log_button.clicked.connect(function)

    def set_receipt_button_listener(self, function) -> None:
        self.receipt_button.clicked.connect(function)

    def set_menu_button_listener(self, function) -> None:
        self.menu_button.clicked.connect(function)

    def set_account_button_listener(self, function) -> None:
        self.account_button.clicked.connect(function)

# Order Panel (right side)


class OrderView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        order_frame = QFrame(self)
        order_frame.setObjectName("brown_border_frame")
        order_frame.setGeometry(QRect(1143, 115, 700, 720))

        self.order_scrollArea = QScrollArea(order_frame)
        self.order_scrollArea.setObjectName("default_scrollArea")
        self.order_scrollArea.setGeometry(QRect(25, 40, 650, 580))
        self.order_scrollArea.setWidgetResizable(True)
        self.order_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.order_scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.order_scrollAreaContents = QWidget(self.order_scrollArea)
        self.order_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.order_scrollAreaContents.setGeometry(QRect(0, 0, 648, 578))

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.order_scrollAreaContents.setLayout(self.vBox)
        self.order_scrollArea.setWidget(self.order_scrollAreaContents)

        line = QFrame(order_frame)
        line.setObjectName("brown_line")
        line.setGeometry(QRect(25, 634, 650, 5))

        total_label = QLabel("Total", order_frame)
        total_label.setObjectName("default_label")
        total_label.setFont(Theme.DONGLE_BOLD_65)
        total_label.setGeometry(QRect(420, 660, 110, 40))

        self.number_label = QLabel("0", order_frame)
        self.number_label.setObjectName("default_label")
        self.number_label.setFont(Theme.DONGLE_BOLD_65)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setGeometry(QRect(560, 660, 115, 40))

        self.order_button = QPushButton("Order", self)
        self.order_button.setObjectName("default_button")
        self.order_button.setFont(Theme.DONGLE_BOLD_65)
        self.order_button.setGeometry(QRect(1145, 885, 700, 80))

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setGeometry(QRect(75, 115, 1000, 850))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_order_button_listener(self, function) -> None:
        self.order_button.clicked.connect(function)

    def insert_view(self, view: QWidget, index: int = 0) -> None:
        self.stacked_widget.insertWidget(0, view)

    def set_total(self, total_price: float = 0) -> None:
        self.number_label.setText(f"{total_price:.01f}")

    def get_total(self) -> float:
        return float(self.number_label.text())

    def move_to_index(self, index: int) -> None:
        self.stacked_widget.setCurrentIndex(index)

    def reset(self) -> None:
        self.set_total(0)
        self.clear_layout(self.vBox)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

# Order item (Sub view for order view)


class OrderItemView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(620, 85)

        self.name_label = QLabel("Menu Name", self)
        self.name_label.setObjectName("default_label")
        self.name_label.setFont(Theme.DONGLE_BOLD_65)
        self.name_label.setGeometry(QRect(20, 25, 240, 40))

        self.minus_button = QPushButton("-", self)
        self.minus_button.setObjectName("default_button")
        self.minus_button.setFont(Theme.DONGLE_REGULAR_65)
        self.minus_button.setGeometry(QRect(290, 15, 50, 50))

        self.quantity_label = QLabel("1", self)
        self.quantity_label.setEnabled(False)
        self.quantity_label.setObjectName("default_label")
        self.quantity_label.setFont(Theme.DONGLE_REGULAR_65)
        self.quantity_label.setAlignment(Qt.AlignCenter)
        self.quantity_label.setGeometry(QRect(365, 25, 50, 40))

        self.plus_button = QPushButton("+", self)
        self.plus_button.setObjectName("default_button")
        self.plus_button.setFont(Theme.DONGLE_REGULAR_65)
        self.plus_button.setGeometry(QRect(440, 15, 50, 50))

        self.price_label = QLabel("0.0", self)
        self.price_label.setEnabled(False)
        self.price_label.setObjectName("default_label")
        self.price_label.setFont(Theme.DONGLE_REGULAR_65)
        self.price_label.setAlignment(Qt.AlignCenter)
        self.price_label.setGeometry(QRect(485, 25, 150, 40))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_item_name(self, item_name: str) -> None:
        self.name_label.setText(item_name)

    def set_quantity(self, count: int) -> None:
        self.quantity_label.setText(str(count))

    def set_price_label(self, price: float) -> None:
        self.price_label.setText(f"{price:.01f}")

    def increase_button_listener(self, function) -> None:
        self.plus_button.clicked.connect(function)

    def decrease_button_listener(self, function) -> None:
        self.minus_button.clicked.connect(function)

    def get_total_price(self) -> float:
        return float(self.price_label.text())

# Order List Panel (left side)


class OrderListView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        menu_frame = QFrame(self)
        menu_frame.setObjectName("brown_frame")
        menu_frame.setGeometry(0, 0, 1000, 850)

        menu_label = QLabel("Menu", self)
        menu_label.setObjectName("default_label")
        menu_label.setFont(Theme.DONGLE_BOLD_80)
        menu_label.setGeometry(QRect(54, 26, 128, 116))

        # self.search_bar = QLineEdit(self)
        # self.search_bar.setObjectName("search_bar")
        # self.search_bar.setFont(Theme.DONGLE_REGULAR_65)
        # self.search_bar.setGeometry(QRect(272, 40, 677, 80))

        self.menu_scrollArea = QScrollArea(self)
        self.menu_scrollArea.setObjectName("default_scrollArea")
        self.menu_scrollArea.setGeometry(QRect(57, 169, 885, 630))
        self.menu_scrollArea.setWidgetResizable(True)
        self.menu_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.menu_scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.menu_scrollAreaContents = QWidget(self.menu_scrollArea)
        self.menu_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.menu_scrollAreaContents.setGeometry(QRect(0, 0, 883, 628))

        self.vBox = QVBoxLayout()
        self.menu_scrollAreaContents.setLayout(self.vBox)
        self.menu_scrollArea.setWidget(self.menu_scrollAreaContents)

        self.setStyleSheet(Theme.get_stylesheet())

    # def get_searched_item(self) -> str:
    #     return self.search_bar.text()

    def add_widget_to_scrollarea(self, widget: QWidget) -> None:
        self.vBox.addWidget(widget)

# Order Item (Sub view for order list view)


class OrderListItemView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(800, 80)
        self.setObjectName("brown_item")

        self.name_button = QPushButton("Menu Name", self)
        self.name_button.setObjectName("brown_list_button")
        self.name_button.setFont(Theme.DONGLE_REGULAR_65)
        self.name_button.setGeometry(QRect(50, 10, 780, 50))

        white_line = QFrame(self)
        white_line.setObjectName("white_line")
        white_line.setGeometry(QRect(30, 70, 820, 3))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_itemname(self, item_name: str) -> None:
        self.name_button.setText(item_name)

    def set_button_listener(self, function) -> None:
        self.name_button.clicked.connect(function)

# Drink Menu Details


class DrinkDetailView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        order_frame = QFrame(self)
        order_frame.setObjectName("brown_border_frame")
        order_frame.setGeometry(0, 0, 1000, 850)

        self.menu_name = QLabel("Name Test", order_frame)
        self.menu_name.setObjectName("default_label")
        self.menu_name.setFont(Theme.DONGLE_BOLD_80)
        self.menu_name.setGeometry(QRect(100, 70, 830, 77))

        self.hot_button = QPushButton("Hot", order_frame)
        self.hot_button.setObjectName("click_button")
        self.hot_button.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_button.setGeometry(QRect(100, 147, 200, 60))
        self.hot_button.setCheckable(True)

        self.cold_button = QPushButton("Cold", order_frame)
        self.cold_button.setObjectName("click_button")
        self.cold_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_button.setGeometry(QRect(415, 147, 200, 60))
        self.cold_button.setCheckable(True)

        self.blended_button = QPushButton("Blended", order_frame)
        self.blended_button.setObjectName("click_button")
        self.blended_button.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_button.setGeometry(QRect(730, 147, 200, 60))
        self.blended_button.setCheckable(True)

        self.drinkType_buttonGroup = QButtonGroup(order_frame)
        self.drinkType_buttonGroup.setObjectName("drinkType_ButtonGroup")
        self.drinkType_buttonGroup.addButton(self.hot_button)
        self.drinkType_buttonGroup.addButton(self.cold_button)
        self.drinkType_buttonGroup.addButton(self.blended_button)

        sweetness_label = QLabel("Sweetness", order_frame)
        sweetness_label.setObjectName("brown_label")
        sweetness_label.setFont(Theme.DONGLE_REGULAR_65)
        sweetness_label.setGeometry(QRect(100, 258, 200, 103))

        self.sweet0_button = QPushButton("0", order_frame)
        self.sweet0_button.setObjectName("click_button")
        self.sweet0_button.setFont(Theme.DONGLE_REGULAR_65)
        self.sweet0_button.setGeometry(QRect(358, 271, 100, 60))
        self.sweet0_button.setCheckable(True)

        self.sweet25_button = QPushButton("25", order_frame)
        self.sweet25_button.setObjectName("click_button")
        self.sweet25_button.setFont(Theme.DONGLE_REGULAR_65)
        self.sweet25_button.setGeometry(QRect(515, 271, 100, 60))
        self.sweet25_button.setCheckable(True)

        self.sweet50_button = QPushButton("50", order_frame)
        self.sweet50_button.setObjectName("click_button")
        self.sweet50_button.setFont(Theme.DONGLE_REGULAR_65)
        self.sweet50_button.setGeometry(QRect(673, 271, 100, 60))
        self.sweet50_button.setCheckable(True)

        self.sweet100_button = QPushButton("100", order_frame)
        self.sweet100_button.setObjectName("click_button")
        self.sweet100_button.setFont(Theme.DONGLE_REGULAR_65)
        self.sweet100_button.setGeometry(QRect(830, 271, 100, 60))
        self.sweet100_button.setCheckable(True)

        self.sweetness_buttonGroup = QButtonGroup(order_frame)
        self.sweetness_buttonGroup.setObjectName("sweetness_buttonGroup")
        self.sweetness_buttonGroup.addButton(self.sweet0_button)
        self.sweetness_buttonGroup.addButton(self.sweet25_button)
        self.sweetness_buttonGroup.addButton(self.sweet50_button)
        self.sweetness_buttonGroup.addButton(self.sweet100_button)

        self.cancel_button = QPushButton("Cancel", order_frame)
        self.cancel_button.setObjectName("default_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(277, 739, 200, 80))

        self.add_button = QPushButton("Add", order_frame)
        self.add_button.setObjectName("default_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(558, 739, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_name(self, name: str) -> None:
        self.menu_name.setText(name)

    def get_drink_type(self) -> str:
        return self.drinkType_buttonGroup.checkedButton().text()

    def get_sweetness(self) -> str:
        return self.sweetness_buttonGroup.checkedButton().text()

    def set_hbtn_able(self, able: bool) -> None:
        self.hot_button.setEnabled(able)

    def set_cbtn_able(self, able: bool) -> None:
        self.cold_button.setEnabled(able)

    def set_bbtn_able(self, able: bool) -> None:
        self.blended_button.setEnabled(able)

    def get_detail(self) -> str:
        return f"{self.menu_name.text()[0:6]} {self.get_drink_type()[0].upper()}{int(self.get_sweetness()):02d}"

    def set_cancel_button_listener(self, function) -> None:
        self.cancel_button.clicked.connect(function)

    def set_add_button_listener(self, function) -> None:
        self.add_button.clicked.connect(function)

# Bakery Menu Details


class BakeryDetailView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        order_frame = QFrame(self)
        order_frame.setObjectName("brown_border_frame")
        order_frame.setGeometry(0, 0, 1000, 850)

        self.menu_name = QLabel("Name Test", order_frame)
        self.menu_name.setObjectName("default_label")
        self.menu_name.setFont(Theme.DONGLE_BOLD_80)
        self.menu_name.setGeometry(QRect(100, 70, 830, 77))

        self.cancel_button = QPushButton("Cancel", order_frame)
        self.cancel_button.setObjectName("default_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(277, 739, 200, 80))

        self.add_button = QPushButton("Add", order_frame)
        self.add_button.setObjectName("default_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(558, 739, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_name(self, name: str) -> None:
        self.menu_name.setText(name)

    def set_cancel_button_listener(self, function) -> None:
        self.cancel_button.clicked.connect(function)

    def set_add_button_listener(self, function) -> None:
        self.add_button.clicked.connect(function)


"""
Receipt Page
"""


class ReceiptView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(1920, 1080)

        receipt_frame = QFrame(self)
        receipt_frame.setObjectName("upper_curve_frame")
        receipt_frame.setGeometry(QRect(60, 100, 1800, 980))

        self.label_date = QLabel("Date", receipt_frame)
        self.label_date.setObjectName("white_label")
        self.label_date.setGeometry(QRect(89, 31, 151, 61))
        self.label_date.setFont(Theme.DONGLE_BOLD_70)

        self.label_time = QLabel("Time", receipt_frame)
        self.label_time.setObjectName("white_label")
        self.label_time.setGeometry(QRect(439, 31, 151, 61))
        self.label_time.setFont(Theme.DONGLE_BOLD_70)

        self.label_name = QLabel("Description", receipt_frame)
        self.label_name.setObjectName("white_label")
        self.label_name.setGeometry(QRect(688, 31, 250, 61))
        self.label_name.setFont(Theme.DONGLE_BOLD_70)

        brown_line = QFrame(receipt_frame)
        brown_line.setObjectName("dark_brown_line")
        brown_line.setGeometry(QRect(40, 103, 1722, 3))

        self.receipt_scrollArea = QScrollArea(receipt_frame)
        self.receipt_scrollArea.setObjectName("default_scrollArea")
        self.receipt_scrollArea.setGeometry(QRect(45, 129, 1712, 750))
        self.receipt_scrollArea.setWidgetResizable(True)
        self.receipt_scrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.receipt_scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.receipt_scrollAreaContents = QWidget(self.receipt_scrollArea)
        self.receipt_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.receipt_scrollAreaContents.setGeometry(QRect(0, 0, 1710, 748))

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.receipt_scrollAreaContents.setLayout(self.vBox)
        self.receipt_scrollArea.setWidget(self.receipt_scrollAreaContents)

        self.setStyleSheet(Theme.get_stylesheet())

    def add_receipt_to_scrollarea(self, widget: QWidget) -> None:
        self.vBox.addWidget(widget)


"""
Audit Log Page
"""


class LogView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(1920, 1080)

        log_frame = QFrame(self)
        log_frame.setObjectName("upper_curve_frame")
        log_frame.setGeometry(QRect(60, 100, 1800, 980))

        self.label_date = QLabel("Date", log_frame)
        self.label_date.setObjectName("white_label")
        self.label_date.setGeometry(QRect(89, 31, 151, 61))
        self.label_date.setFont(Theme.DONGLE_BOLD_70)

        self.label_time = QLabel("Time", log_frame)
        self.label_time.setObjectName("white_label")
        self.label_time.setGeometry(QRect(439, 31, 151, 61))
        self.label_time.setFont(Theme.DONGLE_BOLD_70)

        self.label_name = QLabel("Activity", log_frame)
        self.label_name.setObjectName("white_label")
        self.label_name.setGeometry(QRect(688, 31, 231, 61))
        self.label_name.setFont(Theme.DONGLE_BOLD_70)

        brown_line = QFrame(log_frame)
        brown_line.setObjectName("dark_brown_line")
        brown_line.setGeometry(QRect(40, 103, 1722, 3))

        self.log_scrollArea = QScrollArea(log_frame)
        self.log_scrollArea.setObjectName("default_scrollArea")
        self.log_scrollArea.setGeometry(QRect(45, 129, 1712, 750))
        self.log_scrollArea.setWidgetResizable(True)
        self.log_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.log_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.log_scrollAreaContents = QWidget(self.log_scrollArea)
        self.log_scrollAreaContents.setObjectName("default_scrollAreaContents")
        self.log_scrollAreaContents.setGeometry(QRect(0, 0, 1710, 748))

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.log_scrollAreaContents.setLayout(self.vBox)
        self.log_scrollArea.setWidget(self.log_scrollAreaContents)

        self.setStyleSheet(Theme.get_stylesheet())

    def add_log_to_scrollarea(self, widget: QWidget) -> None:
        self.vBox.addWidget(widget)


# Log Item (Sub view for log view and receipt view)


class LogItem(QWidget):
    def __init__(self, date: str = None, time: str = None, desc: str = None):
        QWidget.__init__(self, None)
        self.setFixedSize(1680, 80)
        self.setObjectName("brown_item")

        self.date = QLabel(date, self)
        self.date.setObjectName("default_label")
        self.date.setFont(Theme.DONGLE_REGULAR_65)
        self.date.setGeometry(QRect(0, 10, 211, 41))

        self.time = QLabel(time, self)
        self.time.setObjectName("default_label")
        self.time.setFont(Theme.DONGLE_REGULAR_65)
        self.time.setGeometry(QRect(385, 10, 111, 41))

        self.name_act = QLabel(desc, self)
        self.name_act.setObjectName("default_label")
        self.name_act.setFont(Theme.DONGLE_REGULAR_65)
        self.name_act.setGeometry(QRect(630, 10, 1020, 41))

        line = QFrame(self)
        line.setObjectName("white_line")
        line.setGeometry(QRect(0, 70, 1670, 3))

        self.setStyleSheet(Theme.get_stylesheet())


"""
Empty Page
"""


class AdminEmptyView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)

        admin_frame = QFrame(self)
        admin_frame.setObjectName("brown_frame")
        admin_frame.setGeometry(0, 0, 720, 850)

        label_logo = QLabel(admin_frame)
        label_logo.setObjectName("default_label")
        label_logo.setGeometry(QRect(260, 276, 253, 253))
        label_logo.setPixmap(QPixmap("src/asset/Image/logo.png"))

        self.setStyleSheet(Theme.get_stylesheet())


"""
Menu Management for Admin
"""


class MenuView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        admin_frame = QFrame(self)
        admin_frame.setObjectName("dark_brown_border_frame")
        admin_frame.setGeometry(75, 115, 1000, 850)

        menu_label = QLabel("Menu", admin_frame)
        menu_label.setObjectName("default_label")
        menu_label.setFont(Theme.DONGLE_BOLD_80)
        menu_label.setGeometry(QRect(55, 70, 130, 51))

        # self.search_bar = QLineEdit(admin_frame)
        # self.search_bar.setObjectName("search_bar")
        # self.search_bar.setFont(Theme.DONGLE_REGULAR_65)
        # self.search_bar.setGeometry(QRect(260, 53, 680, 80))

        self.admin_scrollArea = QScrollArea(admin_frame)
        self.admin_scrollArea.setObjectName("default_scrollArea")
        self.admin_scrollArea.setGeometry(QRect(55, 182, 890, 480))
        self.admin_scrollArea.setWidgetResizable(True)
        self.admin_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.admin_scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.admin_scrollAreaContents = QWidget(self.admin_scrollArea)
        self.admin_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.admin_scrollAreaContents.setGeometry(QRect(0, 0, 888, 478))

        self.vBox = QVBoxLayout()
        self.admin_scrollAreaContents.setLayout(self.vBox)
        self.admin_scrollArea.setWidget(self.admin_scrollAreaContents)

        self.add_button = QPushButton("+", self)
        self.add_button.setObjectName("default_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(915, 820, 100, 100))

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setGeometry(QRect(1130, 115, 720, 850))
        # self.stacked_widget.setStyleSheet("background: black")

        self.setStyleSheet(Theme.get_stylesheet())

    # def get_searched_item(self) -> str:
    #     return self.search_bar.text()

    def add_view_to_scrollarea(self, view: QWidget) -> None:
        self.vBox.addWidget(view)

    def add_view_to_stackedwidget(self, view: QWidget) -> None:
        self.stacked_widget.insertWidget(0, view)

    def clear__scrollarea(self):
        for i in reversed(range(self.vBox.count())):
            self.vBox.itemAt(i).widget().setParent(None)

    def set_add_button_listener(self, function) -> None:
        self.add_button.clicked.connect(function)

# Create new menu (Sub view for menu view)


class MenuCreateView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)

        menu_frame = QFrame(self)
        menu_frame.setObjectName("brown_frame")
        menu_frame.setGeometry(0, 0, 720, 850)

        name_label = QLabel("Name", menu_frame)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name_bar = QLineEdit(menu_frame)
        self.name_bar.setObjectName("input_bar")
        self.name_bar.setFont(Theme.DONGLE_REGULAR_65)
        self.name_bar.setGeometry(QRect(210, 49, 470, 60))

        type_label = QLabel("Type", menu_frame)
        type_label.setObjectName("default_label")
        type_label.setFont(Theme.DONGLE_BOLD_65)
        type_label.setGeometry(QRect(33, 185, 111, 41))

        self.drink_button = QRadioButton("Drink", menu_frame)
        self.drink_button.setObjectName("default_radio")
        self.drink_button.setFont(Theme.DONGLE_REGULAR_65)
        self.drink_button.setGeometry(QRect(210, 185, 151, 41))

        self.bakery_button = QRadioButton("Bakery", menu_frame)
        self.bakery_button.setObjectName("default_radio")
        self.bakery_button.setFont(Theme.DONGLE_REGULAR_65)
        self.bakery_button.setGeometry(QRect(500, 185, 171, 41))

        type_buttonGroup = QButtonGroup(menu_frame)
        type_buttonGroup.setObjectName("type_buttonGroup")
        type_buttonGroup.addButton(self.drink_button)
        type_buttonGroup.addButton(self.bakery_button)

        price_label = QLabel("Price", menu_frame)
        price_label.setObjectName("default_label")
        price_label.setFont(Theme.DONGLE_BOLD_65)
        price_label.setGeometry(QRect(33, 301, 111, 41))

        self.hot_checkBox = QCheckBox("Hot", menu_frame)
        self.hot_checkBox.setObjectName("default_checkbox")
        self.hot_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_checkBox.setGeometry(QRect(194, 281, 141, 71))

        self.cold_checkBox = QCheckBox("Cold", menu_frame)
        self.cold_checkBox.setObjectName("default_checkbox")
        self.cold_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_checkBox.setGeometry(QRect(194, 370, 151, 61))

        self.blended_checkBox = QCheckBox("Blended", menu_frame)
        self.blended_checkBox.setObjectName("default_checkbox")
        self.blended_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_checkBox.setGeometry(QRect(194, 459, 211, 61))

        self.hot_price = QLineEdit(menu_frame)
        self.hot_price.setObjectName("input_bar")
        self.hot_price.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_price.setGeometry(QRect(480, 281, 200, 60))
        self.hot_price.setAlignment(Qt.AlignCenter)
        self.hot_price.setEnabled(False)

        self.cold_price = QLineEdit(menu_frame)
        self.cold_price.setObjectName("input_bar")
        self.cold_price.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_price.setGeometry(QRect(480, 370, 200, 60))
        self.cold_price.setAlignment(Qt.AlignCenter)
        self.cold_price.setEnabled(False)

        self.blended_price = QLineEdit(menu_frame)
        self.blended_price.setObjectName("input_bar")
        self.blended_price.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_price.setGeometry(QRect(480, 459, 200, 60))
        self.blended_price.setAlignment(Qt.AlignCenter)
        self.blended_price.setEnabled(False)

        self.bakery_price = QLineEdit(menu_frame)
        self.bakery_price.setObjectName("input_bar")
        self.bakery_price.setFont(Theme.DONGLE_REGULAR_65)
        self.bakery_price.setGeometry(QRect(210, 281, 200, 60))
        self.bakery_price.setAlignment(Qt.AlignCenter)

        self.cancel_button = QPushButton("Cancel", menu_frame)
        self.cancel_button.setObjectName("default_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(124, 730, 200, 80))

        self.add_button = QPushButton("Add", menu_frame)
        self.add_button.setObjectName("default_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(394, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())

# Edit menu (Sub view for menu view)


class MenuEditView(QWidget):

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)

        menu_frame = QFrame(self)
        menu_frame.setObjectName("brown_frame")
        menu_frame.setGeometry(0, 0, 720, 850)

        name_label = QLabel("Name", menu_frame)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name_bar = QLineEdit(menu_frame)
        self.name_bar.setObjectName("input_bar")
        self.name_bar.setFont(Theme.DONGLE_REGULAR_65)
        self.name_bar.setGeometry(QRect(210, 49, 470, 60))

        type_label = QLabel("Type", menu_frame)
        type_label.setObjectName("default_label")
        type_label.setFont(Theme.DONGLE_BOLD_65)
        type_label.setGeometry(QRect(33, 185, 111, 41))

        self.drink_button = QRadioButton("Drink", menu_frame)
        self.drink_button.setObjectName("default_radio")
        self.drink_button.setFont(Theme.DONGLE_REGULAR_65)
        self.drink_button.setGeometry(QRect(210, 185, 151, 41))

        self.bakery_button = QRadioButton("Bakery", menu_frame)
        self.bakery_button.setObjectName("default_radio")
        self.bakery_button.setFont(Theme.DONGLE_REGULAR_65)
        self.bakery_button.setGeometry(QRect(500, 185, 171, 41))

        type_buttonGroup = QButtonGroup(menu_frame)
        type_buttonGroup.setObjectName("type_buttonGroup")
        type_buttonGroup.addButton(self.drink_button)
        type_buttonGroup.addButton(self.bakery_button)

        price_label = QLabel("Price", menu_frame)
        price_label.setObjectName("default_label")
        price_label.setFont(Theme.DONGLE_BOLD_65)
        price_label.setGeometry(QRect(33, 301, 111, 41))

        self.hot_checkBox = QCheckBox("Hot", menu_frame)
        self.hot_checkBox.setObjectName("default_checkbox")
        self.hot_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_checkBox.setGeometry(QRect(194, 281, 141, 71))

        self.cold_checkBox = QCheckBox("Cold", menu_frame)
        self.cold_checkBox.setObjectName("default_checkbox")
        self.cold_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_checkBox.setGeometry(QRect(194, 370, 151, 61))

        self.blended_checkBox = QCheckBox("Blended", menu_frame)
        self.blended_checkBox.setObjectName("default_checkbox")
        self.blended_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_checkBox.setGeometry(QRect(194, 459, 211, 61))

        self.hot_price = QLineEdit(menu_frame)
        self.hot_price.setObjectName("input_bar")
        self.hot_price.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_price.setGeometry(QRect(480, 281, 200, 60))
        self.hot_price.setAlignment(Qt.AlignCenter)
        self.hot_price.setEnabled(False)

        self.cold_price = QLineEdit(menu_frame)
        self.cold_price.setObjectName("input_bar")
        self.cold_price.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_price.setGeometry(QRect(480, 370, 200, 60))
        self.cold_price.setAlignment(Qt.AlignCenter)
        self.cold_price.setEnabled(False)

        self.blended_price = QLineEdit(menu_frame)
        self.blended_price.setObjectName("input_bar")
        self.blended_price.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_price.setGeometry(QRect(480, 459, 200, 60))
        self.blended_price.setAlignment(Qt.AlignCenter)
        self.blended_price.setEnabled(False)

        self.bakery_price = QLineEdit(menu_frame)
        self.bakery_price.setObjectName("input_bar")
        self.bakery_price.setFont(Theme.DONGLE_REGULAR_65)
        self.bakery_price.setGeometry(QRect(210, 281, 200, 60))
        self.bakery_price.setAlignment(Qt.AlignCenter)

        self.cancel_button = QPushButton("Cancel", menu_frame)
        self.cancel_button.setObjectName("default_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(33, 730, 200, 80))

        self.save_button = QPushButton("Save", menu_frame)
        self.save_button.setObjectName("default_button")
        self.save_button.setFont(Theme.DONGLE_REGULAR_65)
        self.save_button.setGeometry(QRect(257, 730, 200, 80))

        self.delete_button = QPushButton("Delete", menu_frame)
        self.delete_button.setObjectName("default_button")
        self.delete_button.setFont(Theme.DONGLE_REGULAR_65)
        self.delete_button.setGeometry(QRect(480, 730, 200, 80))

        self.drink_button.clicked.connect(self.show_drink_info)
        self.bakery_button.clicked.connect(self.show_bakery_info)

        self.setStyleSheet(Theme.get_stylesheet())

    def set_name(self, name: str) -> None:
        self.name_bar.setText(name)

    def show_drink_info(self) -> None:
        self.hot_checkBox.show()
        self.cold_checkBox.show()
        self.blended_checkBox.show()
        self.hot_price.show()
        self.cold_price.show()
        self.blended_price.show()
        self.bakery_price.hide()

    def show_bakery_info(self) -> None:
        self.hot_checkBox.hide()
        self.cold_checkBox.hide()
        self.blended_checkBox.hide()
        self.hot_price.hide()
        self.cold_price.hide()
        self.blended_price.hide()
        self.bakery_price.show()

    def fill_drink_info(self, hprice: float = 0, cprice: float = 0, bprice: float = 0) -> None:
        if hprice != 0:
            self.hot_checkBox.setChecked(True)
            self.hot_price.setText(f"{hprice:.02f}")

        if cprice != 0:
            self.cold_checkBox.setChecked(True)
            self.cold_price.setText(f"{cprice:.02f}")

        if bprice != 0:
            self.blended_checkBox.setChecked(True)
            self.blended_price.setText(f"{bprice:.02f}")

    def fill_bakery_info(self, price: float = 0) -> None:
        if price != 0:
            self.bakery_price.setText(f"{price:.02f}")

    def set_save_button_listener(self, function):
        self.save_button.clicked.connect(function)

    def set_cancel_button_listener(self, function):
        self.cancel_button.clicked.connect(function)

    def set_delete_button_listener(self, function):
        self.delete_button.clicked.connect(function)

# List item (Sub view for menu view and account view)


class AdminListItem(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(860, 80)

        self.name_button = QPushButton("List Name", self)
        self.name_button.setObjectName("white_list_button")
        self.name_button.setFont(Theme.DONGLE_REGULAR_65)
        self.name_button.setGeometry(QRect(50, 10, 780, 50))

        brown_line = QFrame(self)
        brown_line.setObjectName("brown_line")
        brown_line.setGeometry(QRect(30, 70, 820, 3))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_itemname(self, item_name: str) -> None:
        self.name_button.setText(item_name)

    def set_button_listener(self, function) -> None:
        self.name_button.clicked.connect(function)


"""
Account management for admin
"""

"""
class AccountView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        admin_frame = QFrame(self)
        admin_frame.setObjectName("dark_brown_border_frame")
        admin_frame.setGeometry(75, 115, 1000, 850)

        user_label = QLabel("User", admin_frame)
        user_label.setObjectName("default_label")
        user_label.setFont(Theme.DONGLE_BOLD_80)
        user_label.setGeometry(QRect(55, 70, 130, 51))

        # self.search_bar = QLineEdit(admin_frame)
        # self.search_bar.setObjectName("search_bar")
        # self.search_bar.setFont(Theme.DONGLE_REGULAR_65)
        # self.search_bar.setGeometry(QRect(260, 53, 680, 80))

        self.admin_scrollArea = QScrollArea(admin_frame)
        self.admin_scrollArea.setObjectName("default_scrollArea")
        self.admin_scrollArea.setGeometry(QRect(55, 182, 890, 480))
        self.admin_scrollArea.setWidgetResizable(True)
        self.admin_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.admin_scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.admin_scrollAreaContents = QWidget(self.admin_scrollArea)
        self.admin_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.admin_scrollAreaContents.setGeometry(QRect(0, 0, 888, 478))

        vBox = QVBoxLayout()
        self.admin_scrollAreaContents.setLayout(vBox)
        self.admin_scrollArea.setWidget(self.admin_scrollAreaContents)

        add_button = QPushButton("+", self)
        add_button.setObjectName("default_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(915, 820, 100, 100))

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setGeometry(QRect(1130, 115, 720, 850))
        # self.stacked_widget.setStyleSheet("background: black")

        self.setStyleSheet(Theme.get_stylesheet())

    # def get_searched_item(self) -> str:
    #     return self.search_bar.text()

# Create account (Sub view for account view)


class AccountCreateView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)

        acc_frame = QFrame(self)
        acc_frame.setObjectName("brown_frame")
        acc_frame.setGeometry(0, 0, 720, 850)

        name_label = QLabel("Name", acc_frame)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name = QLineEdit(acc_frame)
        self.name.setObjectName("input_bar")
        self.name.setFont(Theme.DONGLE_REGULAR_65)
        self.name.setGeometry(QRect(250, 50, 430, 60))

        surname_label = QLabel("Surname", acc_frame)
        surname_label.setObjectName("default_label")
        surname_label.setFont(Theme.DONGLE_BOLD_65)
        surname_label.setGeometry(QRect(33, 180, 171, 41))

        self.surname = QLineEdit(acc_frame)
        self.surname.setObjectName("input_bar")
        self.surname.setFont(Theme.DONGLE_REGULAR_65)
        self.surname.setGeometry(QRect(250, 155, 430, 60))

        username_label = QLabel("Username", acc_frame)
        username_label.setObjectName("default_label")
        username_label.setFont(Theme.DONGLE_BOLD_65)
        username_label.setGeometry(QRect(33, 390, 191, 41))

        self.username = QLineEdit(acc_frame)
        self.username.setObjectName("input_bar")
        self.username.setFont(Theme.DONGLE_REGULAR_65)
        self.username.setGeometry(QRect(250, 365, 430, 60))

        password_label = QLabel("Password", acc_frame)
        password_label.setObjectName("default_label")
        password_label.setFont(Theme.DONGLE_BOLD_65)
        password_label.setGeometry(QRect(33, 285, 201, 41))

        self.password = QLineEdit(acc_frame)
        self.password.setObjectName("input_bar")
        self.password.setFont(Theme.DONGLE_REGULAR_65)
        self.password.setGeometry(QRect(250, 260, 430, 60))

        position_label = QLabel("Position", acc_frame)
        position_label.setObjectName("default_label")
        position_label.setFont(Theme.DONGLE_BOLD_65)
        position_label.setGeometry(QRect(33, 495, 191, 41))

        self.admin_button = QRadioButton("Admin", acc_frame)
        self.admin_button.setObjectName("default_radio")
        self.admin_button.setFont(Theme.DONGLE_REGULAR_65)
        self.admin_button.setGeometry(QRect(250, 495, 161, 41))

        self.staff_button = QRadioButton("Staff", acc_frame)
        self.staff_button.setObjectName("default_radio")
        self.staff_button.setFont(Theme.DONGLE_REGULAR_65)
        self.staff_button.setGeometry(QRect(540, 495, 141, 41))

        position_buttonGroup = QButtonGroup(acc_frame)
        position_buttonGroup.setObjectName("position_buttonGroup")
        position_buttonGroup.addButton(self.admin_button)
        position_buttonGroup.addButton(self.staff_button)

        self.cancel_button = QPushButton("Cancel", acc_frame)
        self.cancel_button.setObjectName("default_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(124, 730, 200, 80))

        self.add_button = QPushButton("Add", acc_frame)
        self.add_button.setObjectName("default_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(394, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())

    def set_fname(self, fname: str = None) -> None:
        if fname is None:
            return
        self.name.setText(fname)

    def get_fname(self) -> str:
        return self.name.text()

    def set_lname(self, lname: str = None) -> None:
        if lname is None:
            return
        self.surname.setText(lname)

    def get_lname(self) -> str:
        return self.surname.text()

    def set_username(self, username: str = None) -> None:
        if username is None:
            return
        self.username.setText(username)

    def get_username(self) -> str:
        return self.username.text()

    def set_password(self, password: str = None) -> None:
        if password is None:
            return
        self.password.setText(password)

    def get_password(self) -> str:
        return self.password.text()

    def set_access_level(self, access_level: str = None) -> None:
        if access_level is None:
            return

        if access_level == "admin":
            self.admin_button.setChecked(True)
        elif access_level == "staff":
            self.staff_button.setChecked(True)

    def get_access_level(self) -> str:
        if self.admin_button.isChecked():
            return "admin"
        if self.staff_button.isChecked():
            return "staff"
        return

    def set_add_button_listener(self, function) -> None:
        self.add_button.clicked.connect(function)

    def set_cancel_button_listener(self, function) -> None:
        self.cancel_button.clicked.connect(function)

# Edit account (Sub view for account view)


class AccountEditView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)
        
        acc_frame = QFrame(self)
        acc_frame.setObjectName("brown_frame")
        acc_frame.setGeometry(0, 0, 720, 850)

        name_label = QLabel("Name", acc_frame)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name = QLineEdit(acc_frame)
        self.name.setObjectName("input_bar")
        self.name.setFont(Theme.DONGLE_REGULAR_65)
        self.name.setGeometry(QRect(250, 50, 430, 60))

        surname_label = QLabel("Surname", acc_frame)
        surname_label.setObjectName("default_label")
        surname_label.setFont(Theme.DONGLE_BOLD_65)
        surname_label.setGeometry(QRect(33, 180, 171, 41))

        self.surname = QLineEdit(acc_frame)
        self.surname.setObjectName("input_bar")
        self.surname.setFont(Theme.DONGLE_REGULAR_65)
        self.surname.setGeometry(QRect(250, 155, 430, 60))

        username_label = QLabel("Username", acc_frame)
        username_label.setObjectName("default_label")
        username_label.setFont(Theme.DONGLE_BOLD_65)
        username_label.setGeometry(QRect(33, 390, 191, 41))

        self.username = QLineEdit(acc_frame)
        self.username.setObjectName("input_bar")
        self.username.setFont(Theme.DONGLE_REGULAR_65)
        self.username.setGeometry(QRect(250, 365, 430, 60))

        password_label = QLabel("Password", acc_frame)
        password_label.setObjectName("default_label")
        password_label.setFont(Theme.DONGLE_BOLD_65)
        password_label.setGeometry(QRect(33, 285, 201, 41))

        self.password = QLineEdit(acc_frame)
        self.password.setObjectName("input_bar")
        self.password.setFont(Theme.DONGLE_REGULAR_65)
        self.password.setGeometry(QRect(250, 260, 430, 60))

        position_label = QLabel("Position", acc_frame)
        position_label.setObjectName("default_label")
        position_label.setFont(Theme.DONGLE_BOLD_65)
        position_label.setGeometry(QRect(33, 495, 191, 41))

        self.admin_button = QRadioButton("Admin", acc_frame)
        self.admin_button.setObjectName("default_radio")
        self.admin_button.setFont(Theme.DONGLE_REGULAR_65)
        self.admin_button.setGeometry(QRect(250, 495, 161, 41))

        self.staff_button = QRadioButton("Staff", acc_frame)
        self.staff_button.setObjectName("default_radio")
        self.staff_button.setFont(Theme.DONGLE_REGULAR_65)
        self.staff_button.setGeometry(QRect(540, 495, 141, 41))

        position_buttonGroup = QButtonGroup(acc_frame)
        position_buttonGroup.setObjectName("position_buttonGroup")
        position_buttonGroup.addButton(self.admin_button)
        position_buttonGroup.addButton(self.staff_button)

        self.cancel_button = QPushButton("Cancel", acc_frame)
        self.cancel_button.setObjectName("default_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(33, 730, 200, 80))

        self.save_button = QPushButton("Save", acc_frame)
        self.save_button.setObjectName("default_button")
        self.save_button.setFont(Theme.DONGLE_REGULAR_65)
        self.save_button.setGeometry(QRect(257, 730, 200, 80))

        self.delete_button = QPushButton("Delete", acc_frame)
        self.delete_button.setObjectName("default_button")
        self.delete_button.setFont(Theme.DONGLE_REGULAR_65)
        self.delete_button.setGeometry(QRect(480, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())
"""
