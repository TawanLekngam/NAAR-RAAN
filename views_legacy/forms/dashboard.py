# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
        Form.resize(1920, 1080)
        Form.setMaximumSize(QSize(1920, 1080))
        font = QFont()
        font.setFamilies([u"Dongle"])
        font.setPointSize(80)
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #F9F5F0;")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(75, 115, 1000, 850))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: #D8B797;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.menu_label = QLabel(self.frame)
        self.menu_label.setObjectName(u"menu_label")
        self.menu_label.setGeometry(QRect(54, 26, 128, 116))
        self.menu_label.setMaximumSize(QSize(128, 116))
        self.menu_label.setFont(font)
        self.menu_label.setStyleSheet(u"color:  #4A321C;")
        self.search_bar = QLineEdit(self.frame)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(272, 40, 677, 80))
        self.search_bar.setMaximumSize(QSize(677, 80))
        font1 = QFont()
        font1.setFamilies([u"Dongle"])
        font1.setPointSize(65)
        font1.setBold(False)
        self.search_bar.setFont(font1)
        self.menu_scrollArea = QScrollArea(self.frame)
        self.menu_scrollArea.setObjectName(u"menu_scrollArea")
        self.menu_scrollArea.setGeometry(QRect(57, 169, 885, 630))
        self.menu_scrollArea.setMaximumSize(QSize(885, 630))
        font2 = QFont()
        font2.setFamilies([u"Dongle"])
        font2.setPointSize(65)
        font2.setBold(True)
        self.menu_scrollArea.setFont(font2)
        self.menu_scrollArea.setAutoFillBackground(False)
        self.menu_scrollArea.setWidgetResizable(True)
        self.menu_scrollAreaWidgetContents = QWidget()
        self.menu_scrollAreaWidgetContents.setObjectName(u"menu_scrollAreaWidgetContents")
        self.menu_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 883, 628))
        self.menu_scrollArea.setWidget(self.menu_scrollAreaWidgetContents)
        self.user_frame = QFrame(Form)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setGeometry(QRect(1590, 0, 330, 65))
        self.user_frame.setMaximumSize(QSize(330, 65))
        self.user_frame.setFont(font2)
        self.user_frame.setStyleSheet(u"background-color: #4A321C;\n"
"color: #D8B797;")
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.order_frame = QFrame(Form)
        self.order_frame.setObjectName(u"order_frame")
        self.order_frame.setGeometry(QRect(1143, 115, 700, 720))
        self.order_frame.setMaximumSize(QSize(700, 720))
        self.order_frame.setFrameShape(QFrame.StyledPanel)
        self.order_frame.setFrameShadow(QFrame.Raised)
        self.order_scrollArea = QScrollArea(self.order_frame)
        self.order_scrollArea.setObjectName(u"order_scrollArea")
        self.order_scrollArea.setGeometry(QRect(25, 40, 650, 580))
        self.order_scrollArea.setWidgetResizable(True)
        self.order_scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.order_scrollAreaWidgetContents = QWidget()
        self.order_scrollAreaWidgetContents.setObjectName(u"order_scrollAreaWidgetContents")
        self.order_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 648, 578))
        self.order_scrollArea.setWidget(self.order_scrollAreaWidgetContents)
        self.total_label = QLabel(self.order_frame)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setGeometry(QRect(420, 660, 110, 40))
        self.total_label.setFont(font2)
        self.total_label.setStyleSheet(u"color: #4A321C;")
        self.total_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line = QFrame(self.order_frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(25, 634, 650, 5))
        self.line.setStyleSheet(u"background-color: #D8B797;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.number_label = QLabel(self.order_frame)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setGeometry(QRect(540, 660, 115, 40))
        self.number_label.setFont(font2)
        self.number_label.setStyleSheet(u"color: #4A321C;")
        self.number_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_scrollArea.raise_()
        self.total_label.raise_()
        self.number_label.raise_()
        self.line.raise_()
        self.order_button = QPushButton(Form)
        self.order_button.setObjectName(u"order_button")
        self.order_button.setGeometry(QRect(1145, 885, 700, 80))
        font3 = QFont()
        font3.setFamilies([u"Dongle"])
        font3.setPointSize(65)
        self.order_button.setFont(font3)
        self.order_button.setStyleSheet(u"background-color: #754926;\n"
"color: #F9F5F0;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.menu_label.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.total_label.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.number_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.order_button.setText(QCoreApplication.translate("Form", u"Order", None))
    # retranslateUi

