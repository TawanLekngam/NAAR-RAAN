import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Menu_order_form(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        default_font = QFont("Dongle", 65)
        # self.setFont(default_font)

        self.setFixedSize(1920, 1080)

        menu_label = QLabel("Menu", self)
        menu_label.setGeometry(QRect(54, 26, 128, 116))

        # menu_label.setStyleSheet("color:  #4A321C;")

        menu_frame = QFrame(self)
        menu_frame.setObjectName("menu_frame")
        menu_frame.setGeometry(75, 115, 1000, 850)


        

        self.showFullScreen()

    def set_styleSheet(self, file):
        self.setStyleSheet("theme/menu_order_theme.qss")
        with open("theme/menu_order_theme.qss", "r") as f:
            _style = f.read()
            mo.setStyleSheet(_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mo = Menu_order_form()

    sys.exit(app.exec())