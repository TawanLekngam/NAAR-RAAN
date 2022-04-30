import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Audit_Log(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.resize(1920, 1080)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 120, 1800, 960))

        self.label_date = QLabel(self.widget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(100, 70, 151, 61))

        self.label_time = QLabel(self.widget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(400, 70, 151, 61))
        
        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(640, 70, 171, 61))
        
        self.label_actvity = QLabel(self.widget)
        self.label_actvity.setObjectName(u"label_actvity")
        self.label_actvity.setGeometry(QRect(1080, 70, 231, 61))
        
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(39, 150, 1722, 810))

        self.show()

        
if __name__ =="__main__":
    app = QApplication(sys.argv)
    audit_log = Audit_Log()
    sys.exit(app.exec())

