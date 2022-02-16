import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Log_in(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.resize(1920, 1080)

        self.label_circle = QLabel(self)
        self.label_circle.setObjectName("label_circle")
        self.label_circle.setGeometry(QRect(753, 112, 400, 400))
        self.label_circle.setPixmap(QPixmap("assets/Image/circle.png"))

        self.label_logo = QLabel(self)
        self.label_logo.setObjectName("label_logo")
        self.label_logo.setGeometry(QRect(846, 158, 252, 252))
        self.label_logo.setPixmap(QPixmap("assets/Image/logo.png"))

        self.label_username = QLabel("Username",self)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(523, 587, 321, 72))
        
        self.label_password = QLabel("Password",self)
        self.label_password.setObjectName("label_password")
        self.label_password.setGeometry(QRect(523, 726, 291, 72))
        
        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(980, 570, 600, 80))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(980, 715, 600, 80))

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(860, 860, 200, 80))

        icon = QIcon()
        icon.addFile("assets/svgs/coffee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(55, 55))

        self.show()
    
    
    def set_styleSheet(self, file_name: str):
        with open("themes/" + file_name, "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
            f.close

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Log_in()
    login.set_styleSheet("log_in_theme.qss")

    sys.exit(app.exec())
