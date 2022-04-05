"""
    contain all view and utility widget.
"""

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from theme import Theme


class LogInPage(QWidget):
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
        self.showFullScreen()

    def login_button_emit(self, function) -> None:
        self.login_button.clicked.connect(function)


class MenuOrderPage(QWidget):
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
        self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mo = LogInPage()
    sys.exit(app.exec())
