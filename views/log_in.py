import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Log_In(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.setFixedSize(1920, 1080)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_username = QLabel("USERNAME",self)
        self.label_username.setObjectName(u"label_username")
        

        self.gridLayout.addWidget(self.label_username, 0, 0, 1, 1)

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout.addWidget(self.lineEdit_username, 0, 1, 1, 1)

        self.label_password = QLabel("PASSWORD",self)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 1, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)

        self.pushButton_login = QPushButton(self)
        self.pushButton_login.setObjectName(u"pushButton_login")
        pixmap = QPixmap("views/assets/Image/coffee.png")
        self.pushButton_login.setIcon(pixmap)
        self.pushButton_login.setIconSize(QSize(55,55))

        self.gridLayout.addWidget(self.pushButton_login, 2, 2, 1, 1)

        self.show()
    def set_styleSheet(self, file_name: str):
        with open("themes/" + file_name, "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
            f.close

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Log_In()
    login.set_styleSheet("log_in_theme.qss")
    sys.exit(app.exec())

