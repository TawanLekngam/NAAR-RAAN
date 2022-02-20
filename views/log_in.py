import sys
from PySide6.QtCore import *
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton)

from views.base_page import BasePage


class Log_in(BasePage):
    def __init__(self):
        BasePage.__init__(self, None)

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
        label_username.setFont(self._get_font(65))
        label_username.setGeometry(QRect(523, 587, 321, 72))

        label_password = QLabel("Password", self)
        label_password.setObjectName("label_password")
        label_password.setFont(self._get_font(65))
        label_password.setGeometry(QRect(523, 726, 291, 72))

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_username.setFont(self._get_font(65))
        self.lineEdit_username.setGeometry(QRect(980, 570, 600, 80))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setFont(self._get_font(50))
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

        self.show()

    def login_button_emit(self, function) -> None:
        self.login_button.clicked.connect(function)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Log_in()
    sys.exit(app.exec())
