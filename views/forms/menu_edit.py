# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 850)
        Form.setStyleSheet(u"background-color: #D8B797;\n"
"border-radius: 20px;")
        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(33, 75, 111, 41))
        font = QFont()
        font.setFamilies([u"Dongle"])
        font.setPointSize(65)
        font.setBold(True)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"color: #4A321C;")
        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(210, 49, 470, 60))
        font1 = QFont()
        font1.setFamilies([u"Dongle"])
        font1.setPointSize(65)
        self.name.setFont(font1)
        self.name.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;\n"
"padding-left: 30px;\n"
"padding-right: 30px;")
        self.addOn_button = QRadioButton(Form)
        self.type_buttonGroup = QButtonGroup(Form)
        self.type_buttonGroup.setObjectName(u"type_buttonGroup")
        self.type_buttonGroup.addButton(self.addOn_button)
        self.addOn_button.setObjectName(u"addOn_button")
        self.addOn_button.setGeometry(QRect(33, 177, 191, 41))
        self.addOn_button.setFont(font)
        self.addOn_button.setStyleSheet(u"QRadioButton{\n"
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
        self.drink_button = QRadioButton(Form)
        self.type_buttonGroup.addButton(self.drink_button)
        self.drink_button.setObjectName(u"drink_button")
        self.drink_button.setGeometry(QRect(290, 177, 151, 41))
        self.drink_button.setFont(font)
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
        self.bakery_button = QRadioButton(Form)
        self.type_buttonGroup.addButton(self.bakery_button)
        self.bakery_button.setObjectName(u"bakery_button")
        self.bakery_button.setGeometry(QRect(500, 177, 171, 41))
        self.bakery_button.setFont(font)
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
        self.price_label = QLabel(Form)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setGeometry(QRect(33, 301, 111, 41))
        self.price_label.setFont(font)
        self.price_label.setStyleSheet(u"color: #4A321C;")
        self.hot_checkBox = QCheckBox(Form)
        self.hot_checkBox.setObjectName(u"hot_checkBox")
        self.hot_checkBox.setGeometry(QRect(194, 281, 141, 71))
        self.hot_checkBox.setFont(font1)
        self.hot_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width: 50px;\n"
"height: 50px;\n"
"background: #F9F5F0;\n"
"border: 5px solid #754926;\n"
"border-radius: 20px;\n"
"}")
        self.hot_checkBox.setCheckable(True)
        self.hot_checkBox.setChecked(False)
        self.cold_checkBox = QCheckBox(Form)
        self.cold_checkBox.setObjectName(u"cold_checkBox")
        self.cold_checkBox.setGeometry(QRect(194, 370, 151, 61))
        self.cold_checkBox.setFont(font1)
        self.cold_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width: 50px;\n"
"height: 50px;\n"
"background: #F9F5F0;\n"
"border: 5px solid #754926;\n"
"border-radius: 20px;\n"
"}")
        self.blended_checkBox = QCheckBox(Form)
        self.blended_checkBox.setObjectName(u"blended_checkBox")
        self.blended_checkBox.setGeometry(QRect(194, 459, 211, 61))
        self.blended_checkBox.setFont(font1)
        self.blended_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width: 50px;\n"
"height: 50px;\n"
"background: #F9F5F0;\n"
"border: 5px solid #754926;\n"
"border-radius: 20px;\n"
"}")
        self.hot_price = QLineEdit(Form)
        self.hot_price.setObjectName(u"hot_price")
        self.hot_price.setGeometry(QRect(480, 281, 200, 60))
        self.hot_price.setFont(font1)
        self.hot_price.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;")
        self.hot_price.setAlignment(Qt.AlignCenter)
        self.cold_price = QLineEdit(Form)
        self.cold_price.setObjectName(u"cold_price")
        self.cold_price.setGeometry(QRect(480, 370, 200, 60))
        self.cold_price.setFont(font1)
        self.cold_price.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;")
        self.cold_price.setAlignment(Qt.AlignCenter)
        self.blended_price = QLineEdit(Form)
        self.blended_price.setObjectName(u"blended_price")
        self.blended_price.setGeometry(QRect(480, 459, 200, 60))
        self.blended_price.setFont(font1)
        self.blended_price.setStyleSheet(u"background: #F9F5F0;\n"
"border-radius: 20px;\n"
"color:  #4A321C;")
        self.blended_price.setAlignment(Qt.AlignCenter)
        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(33, 730, 200, 80))
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
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
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet(u"QPushButton{\n"
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
        self.save_button.setFont(font)
        self.save_button.setStyleSheet(u"QPushButton{\n"
"	background: #754926;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::Pressed {\n"
"	background: #4A321C;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.addOn_button.setText(QCoreApplication.translate("Form", u"Add-On", None))
        self.drink_button.setText(QCoreApplication.translate("Form", u"Drink", None))
        self.bakery_button.setText(QCoreApplication.translate("Form", u"Bakery", None))
        self.price_label.setText(QCoreApplication.translate("Form", u"Price", None))
        self.hot_checkBox.setText(QCoreApplication.translate("Form", u"Hot", None))
        self.cold_checkBox.setText(QCoreApplication.translate("Form", u"Cold", None))
        self.blended_checkBox.setText(QCoreApplication.translate("Form", u"Blended", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

