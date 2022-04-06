"""
    contain all view and utility widget.
"""

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from views.theme import Theme

"""
    utility widget.
"""


class UserTab(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)


class OrderDetail(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1000, 850)

        menu_name = QLabel("Name Test", self)
        menu_name.setObjectName("menu_name")
        menu_name.setFont(Theme.DONGLE_BOLD_80)
        menu_name.setGeometry(QRect(93, 57, 830, 77))

        hot_button = QPushButton("Hot", self)
        hot_button.setObjectName("default_button")
        hot_button.setFont(Theme.DONGLE_REGULAR_65)
        hot_button.setGeometry(QRect(93, 134, 200, 60))
        hot_button.setCheckable(True)

        cold_button = QPushButton("Cold", self)
        cold_button.setObjectName("default_button")
        cold_button.setFont(Theme.DONGLE_REGULAR_65)
        cold_button.setGeometry(QRect(408, 134, 200, 60))
        cold_button.setCheckable(True)

        blended_button = QPushButton("Blended", self)
        blended_button.setObjectName("default_button")
        blended_button.setFont(Theme.DONGLE_REGULAR_65)
        blended_button.setGeometry(QRect(723, 134, 200, 60))
        blended_button.setCheckable(True)

        drinkType_buttonGroup = QButtonGroup(self)
        drinkType_buttonGroup.setObjectName("drinkType_ButtonGroup")
        drinkType_buttonGroup.addButton(hot_button)
        drinkType_buttonGroup.addButton(cold_button)
        drinkType_buttonGroup.addButton(blended_button)

        sweetness_label = QLabel("Sweetness", self)
        sweetness_label.setObjectName("sweetness_label")
        sweetness_label.setFont(Theme.DONGLE_REGULAR_65)
        sweetness_label.setGeometry(QRect(93, 241, 200, 103))

        sweet0_button = QPushButton("0", self)
        sweet0_button.setObjectName("default_button")
        sweet0_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet0_button.setGeometry(QRect(343, 258, 100, 60))
        sweet0_button.setCheckable(True)

        sweet25_button = QPushButton("25", self)
        sweet25_button.setObjectName("default_button")
        sweet25_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet25_button.setGeometry(QRect(503, 258, 100, 60))
        sweet25_button.setCheckable(True)

        sweet50_button = QPushButton("50", self)
        sweet50_button.setObjectName("default_button")
        sweet50_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet50_button.setGeometry(QRect(663, 258, 100, 60))
        sweet50_button.setCheckable(True)

        sweet100_button = QPushButton("100", self)
        sweet100_button.setObjectName("default_button")
        sweet100_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet100_button.setGeometry(QRect(823, 258, 100, 60))
        sweet100_button.setCheckable(True)

        sweetness_buttonGroup = QButtonGroup(self)
        sweetness_buttonGroup.setObjectName("sweetness_buttonGroup")
        sweetness_buttonGroup.addButton(sweet0_button)
        sweetness_buttonGroup.addButton(sweet25_button)
        sweetness_buttonGroup.addButton(sweet50_button)
        sweetness_buttonGroup.addButton(sweet100_button)

        addOn_label = QLabel("Add-On", self)
        addOn_label.setObjectName("addOn_label")
        addOn_label.setFont(Theme.DONGLE_REGULAR_65)
        addOn_label.setGeometry(QRect(93, 344, 147, 57))

        topping1_button = QPushButton("Topping1", self)
        topping1_button.setObjectName("default_button")
        topping1_button.setFont(Theme.DONGLE_REGULAR_65)
        topping1_button.setGeometry(QRect(93, 439, 200, 60))
        topping1_button.setCheckable(True)

        topping2_button = QPushButton("Topping2", self)
        topping2_button.setObjectName("default_button")
        topping2_button.setFont(Theme.DONGLE_REGULAR_65)
        topping2_button.setGeometry(QRect(304, 439, 200, 60))
        topping2_button.setCheckable(True)

        topping3_button = QPushButton("Topping3", self)
        topping3_button.setObjectName("default_button")
        topping3_button.setFont(Theme.DONGLE_REGULAR_65)
        topping3_button.setGeometry(QRect(514, 439, 200, 60))
        topping3_button.setCheckable(True)

        topping4_button = QPushButton("Topping4", self)
        topping4_button.setObjectName("default_button")
        topping4_button.setFont(Theme.DONGLE_REGULAR_65)
        topping4_button.setGeometry(QRect(723, 439, 200, 60))
        topping4_button.setCheckable(True)

        topping5_button = QPushButton("Topping5", self)
        topping5_button.setObjectName("default_button")
        topping5_button.setFont(Theme.DONGLE_REGULAR_65)
        topping5_button.setGeometry(QRect(93, 536, 200, 60))
        topping5_button.setCheckable(True)

        topping6_button = QPushButton("Topping6", self)
        topping6_button.setObjectName("default_button")
        topping6_button.setFont(Theme.DONGLE_REGULAR_65)
        topping6_button.setGeometry(QRect(304, 536, 200, 60))
        topping6_button.setCheckable(True)

        topping7_button = QPushButton("Topping7", self)
        topping7_button.setObjectName("default_button")
        topping7_button.setFont(Theme.DONGLE_REGULAR_65)
        topping7_button.setGeometry(QRect(514, 536, 200, 60))
        topping7_button.setCheckable(True)

        topping8_button = QPushButton("Topping8", self)
        topping8_button.setObjectName("default_button")
        topping8_button.setFont(Theme.DONGLE_REGULAR_65)
        topping8_button.setGeometry(QRect(723, 536, 200, 60))
        topping8_button.setCheckable(True)

        cancel_button = QPushButton("Cancel", self)
        cancel_button.setObjectName("cancel_add_button")
        cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        cancel_button.setGeometry(QRect(270, 726, 200, 80))

        add_button = QPushButton("Add", self)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(551, 726, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())

"""
    application view.
"""


class LoginView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        label_circle = QLabel(self)
        label_circle.setObjectName("label_circle")
        label_circle.setGeometry(QRect(753, 112, 400, 400))
        label_circle.setPixmap(QPixmap("assets/Image/circle.png"))

        label_logo = QLabel(self)
        label_logo.setObjectName("label_logo")
        label_logo.setGeometry(QRect(846, 158, 252, 252))
        label_logo.setPixmap(QPixmap("assets/Image/logo.png"))

        label_username = QLabel("Username", self)
        label_username.setObjectName("label_username")
        label_username.setFont(Theme.DONGLE_BOLD_65)
        label_username.setGeometry(QRect(523, 587, 321, 72))

        label_password = QLabel("Password", self)
        label_password.setObjectName("label_password")
        label_password.setFont(Theme.DONGLE_BOLD_65)
        label_password.setGeometry(QRect(523, 726, 291, 72))

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_username.setFont(Theme.DONGLE_BOLD_65)
        self.lineEdit_username.setGeometry(QRect(980, 570, 600, 80))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setFont(Theme.DONGLE_REGULAR_50)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setGeometry(QRect(980, 715, 600, 80))

        self.login_button = QPushButton(self)
        self.login_button.setObjectName("pushButton")
        self.login_button.setGeometry(QRect(860, 860, 200, 80))

        icon = QIcon()
        icon.addFile("assets/svgs/coffee.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(55, 55))
        self.setStyleSheet(Theme.get_stylesheet())

    def login_button_emit(self, function) -> None:
        self.login_button.clicked.connect(function)


class MenuOrderView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        menu_frame = QFrame(self)
        menu_frame.setObjectName("menu_frame")
        menu_frame.setGeometry(75, 115, 1000, 850)

        menu_label = QLabel("Menu", menu_frame)
        menu_label.setObjectName("menu_label")
        menu_label.setFont(Theme.DONGLE_BOLD_80)
        menu_label.setGeometry(QRect(54, 26, 128, 116))

        self.search_bar = QLineEdit(menu_frame)
        self.search_bar.setObjectName("search_bar")
        self.search_bar.setFont(Theme.DONGLE_BOLD_65)
        self.search_bar.setGeometry(QRect(272, 40, 677, 80))

        menu_scrollArea = QScrollArea(menu_frame)
        menu_scrollArea.setObjectName("menu_scrollArea")
        menu_scrollArea.setGeometry(QRect(57, 169, 885, 630))

        menu_scrollAreaContents = QWidget(menu_scrollArea)
        menu_scrollAreaContents.setObjectName("menu_scrollAreaContents")
        menu_scrollAreaContents.setGeometry(QRect(0, 0, 883, 628))
        menu_scrollArea.setWidget(menu_scrollAreaContents)

        order_frame = QFrame(self)
        order_frame.setObjectName("order_frame")
        order_frame.setGeometry(QRect(1143, 115, 700, 720))

        order_scrollArea = QScrollArea(order_frame)
        order_scrollArea.setObjectName("order_scrollArea")
        order_scrollArea.setGeometry(QRect(25, 40, 650, 580))

        order_scrollAreaContents = QWidget(order_scrollArea)
        order_scrollAreaContents.setObjectName("order_scrollAreaContents")
        order_scrollAreaContents.setGeometry(QRect(0, 0, 648, 578))
        order_scrollArea.setWidget(order_scrollAreaContents)

        line = QFrame(order_frame)
        line.setObjectName("line")
        line.setGeometry(QRect(25, 634, 650, 5))

        total_label = QLabel("Total", order_frame)
        total_label.setObjectName("default_label")
        total_label.setFont(Theme.DONGLE_BOLD_65)
        total_label.setGeometry(QRect(420, 660, 110, 40))

        number_label = QLabel("0", order_frame)
        number_label.setObjectName("default_label")
        number_label.setFont(Theme.DONGLE_BOLD_65)
        number_label.setGeometry(QRect(540, 660, 115, 40))

        self.order_button = QPushButton("Order", self)
        self.order_button.setObjectName("order_button")
        self.order_button.setFont(Theme.DONGLE_BOLD_65)
        self.order_button.setGeometry(QRect(1145, 885, 700, 80))

        self.setStyleSheet(Theme.get_stylesheet())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mo = LogInPage()
    sys.exit(app.exec())
