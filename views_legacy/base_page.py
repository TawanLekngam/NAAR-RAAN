import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class BasePageView(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.resize(1920, 1080)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 1920, 94))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 84, 1920, 1071))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

      

