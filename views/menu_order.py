import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from base_page import BasePage


class Menu_order(BasePage):
    def __init__(self):
        BasePage.__init__(self, None)

        self.setFixedSize(1920, 1080)

        user_frame = QFrame(self)
        user_frame.setObjectName("user_frame")
        user_frame.setGeometry(QRect(1590, 0, 330, 65))

        menu_frame = QFrame(self)
        menu_frame.setObjectName("menu_frame")
        menu_frame.setGeometry(75, 115, 1000, 850)

        menu_label = QLabel("Menu", menu_frame)
        menu_label.setObjectName("menu_label")
        menu_label.setGeometry(QRect(54, 26, 128, 116))

        search_bar = QLineEdit(menu_frame)
        search_bar.setObjectName("search_bar")
        search_bar.setGeometry(QRect(272, 40, 677, 80))

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
        total_label.setObjectName("total_label")
        total_label.setGeometry(QRect(420, 660, 110, 40))

        number_label = QLabel("0", order_frame)
        number_label.setObjectName("number_label")
        number_label.setGeometry(QRect(540, 660, 115, 40))

        order_button = QPushButton("Order", self)
        order_button.setObjectName("order_button")
        order_button.setGeometry(QRect(1145, 885, 700, 80))

        self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mo = Menu_order()

    sys.exit(app.exec())
