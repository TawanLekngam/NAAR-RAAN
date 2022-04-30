# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1333, 980)
        Form.setStyleSheet(u"background-color : #F9F5F0")
        self.menu_frame = QFrame(Form)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(70, 115, 1000, 850))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.menu_label = QLabel(self.menu_frame)
        self.menu_label.setObjectName(u"menu_label")
        self.menu_label.setGeometry(QRect(55, 70, 131, 51))
        font = QFont()
        font.setFamilies([u"Dongle"])
        font.setPointSize(80)
        font.setBold(True)
        self.menu_label.setFont(font)
        self.menu_label.setStyleSheet(u"color: #4A321C")
        self.search_bar = QLineEdit(self.menu_frame)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(260, 53, 680, 80))
        self.search_bar.setStyleSheet(u"padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: #4A321C;\n"
"    background: #F9F5F0;\n"
"    border: 5px solid #754926;\n"
"    border-radius: 20px;")
        self.scrollArea = QScrollArea(self.menu_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(55, 182, 890, 440))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 888, 438))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.add_button = QPushButton(self.menu_frame)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(836, 690, 100, 100))
        self.add_button.setFont(font)
        self.add_button.setStyleSheet(u"background-color: #754926;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 50px;\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1130, 115, 720, 850))
        self.widget.setStyleSheet(u"background-color: #D8B797;\n"
"border-radius: 20px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.menu_label.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

