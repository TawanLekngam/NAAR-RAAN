# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 850)
        Form.setStyleSheet(u"background-color: #D8B797;\n"
"border-radius: 20px;")
        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(250, 50, 430, 60))
        font = QFont()
        font.setFamilies([u"Dongle"])
        font.setPointSize(65)
        self.name.setFont(font)
        self.name.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;\n"
"padding-left: 30px;\n"
"padding-right: 30px;")
        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(33, 75, 111, 41))
        font1 = QFont()
        font1.setFamilies([u"Dongle"])
        font1.setPointSize(65)
        font1.setBold(True)
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"color: #4A321C;")
        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(33, 730, 200, 80))
        self.cancel_button.setFont(font1)
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
"	background: #754926;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::Pressed {\n"
"	background: #4A321C;\n"
"}")
        self.save_button = QPushButton(Form)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(257, 730, 200, 80))
        self.save_button.setFont(font1)
        self.save_button.setStyleSheet(u"QPushButton{\n"
"	background: #754926;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::Pressed {\n"
"	background: #4A321C;\n"
"}")
        self.delete_button = QPushButton(Form)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(480, 730, 200, 80))
        self.delete_button.setFont(font1)
        self.delete_button.setStyleSheet(u"QPushButton{\n"
"	background: #754926;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::Pressed {\n"
"	background: #4A321C;\n"
"}")
        self.name_2 = QLineEdit(Form)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setGeometry(QRect(250, 155, 430, 60))
        self.name_2.setFont(font)
        self.name_2.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;\n"
"padding-left: 30px;\n"
"padding-right: 30px;")
        self.name_label_2 = QLabel(Form)
        self.name_label_2.setObjectName(u"name_label_2")
        self.name_label_2.setGeometry(QRect(33, 180, 171, 41))
        self.name_label_2.setFont(font1)
        self.name_label_2.setStyleSheet(u"color: #4A321C;")
        self.name_3 = QLineEdit(Form)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setGeometry(QRect(250, 365, 430, 60))
        self.name_3.setFont(font)
        self.name_3.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;\n"
"padding-left: 30px;\n"
"padding-right: 30px;")
        self.name_label_3 = QLabel(Form)
        self.name_label_3.setObjectName(u"name_label_3")
        self.name_label_3.setGeometry(QRect(30, 390, 191, 41))
        self.name_label_3.setFont(font1)
        self.name_label_3.setStyleSheet(u"color: #4A321C;")
        self.name_4 = QLineEdit(Form)
        self.name_4.setObjectName(u"name_4")
        self.name_4.setGeometry(QRect(250, 260, 430, 60))
        self.name_4.setFont(font)
        self.name_4.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;\n"
"padding-left: 30px;\n"
"padding-right: 30px;")
        self.name_label_4 = QLabel(Form)
        self.name_label_4.setObjectName(u"name_label_4")
        self.name_label_4.setGeometry(QRect(30, 285, 201, 41))
        self.name_label_4.setFont(font1)
        self.name_label_4.setStyleSheet(u"color: #4A321C;")
        self.bakery_button = QRadioButton(Form)
        self.bakery_button.setObjectName(u"bakery_button")
        self.bakery_button.setGeometry(QRect(540, 495, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"Dongle"])
        font2.setPointSize(65)
        font2.setBold(False)
        self.bakery_button.setFont(font2)
        self.bakery_button.setStyleSheet(u"QRadioButton{\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"background: #F9F5F0;\n"
"width: 30px;\n"
"height: 30px;\n"
"border: 5px solid #754926;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  #754926;\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	border-radius: 20px;\n"
"}")
        self.type_label = QLabel(Form)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setGeometry(QRect(30, 495, 151, 41))
        self.type_label.setFont(font1)
        self.type_label.setStyleSheet(u"color: #4A321C;")
        self.drink_button = QRadioButton(Form)
        self.drink_button.setObjectName(u"drink_button")
        self.drink_button.setGeometry(QRect(250, 495, 161, 41))
        self.drink_button.setFont(font2)
        self.drink_button.setStyleSheet(u"QRadioButton{\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"background: #F9F5F0;\n"
"width: 30px;\n"
"height: 30px;\n"
"border: 5px solid #754926;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  #754926;\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	border-radius: 20px;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"Save", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.name_label_2.setText(QCoreApplication.translate("Form", u"Surname", None))
        self.name_label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.name_label_4.setText(QCoreApplication.translate("Form", u"Username", None))
        self.bakery_button.setText(QCoreApplication.translate("Form", u"Staff", None))
        self.type_label.setText(QCoreApplication.translate("Form", u"Position", None))
        self.drink_button.setText(QCoreApplication.translate("Form", u"Admin", None))
    # retranslateUi

