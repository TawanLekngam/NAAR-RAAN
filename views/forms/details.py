# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'details.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 850)
        Form.setStyleSheet(u"background-color: #F9F5F0;")
        self.menu_name = QLabel(Form)
        self.menu_name.setObjectName(u"menu_name")
        self.menu_name.setGeometry(QRect(93, 57, 830, 77))
        font = QFont()
        font.setFamilies([u"Dongle"])
        font.setPointSize(80)
        font.setBold(True)
        self.menu_name.setFont(font)
        self.menu_name.setStyleSheet(u"color: #4A321C;")
        self.hot_button = QPushButton(Form)
        self.drinkType_buttonGroup = QButtonGroup(Form)
        self.drinkType_buttonGroup.setObjectName(u"drinkType_buttonGroup")
        self.drinkType_buttonGroup.addButton(self.hot_button)
        self.hot_button.setObjectName(u"hot_button")
        self.hot_button.setGeometry(QRect(93, 134, 200, 60))
        font1 = QFont()
        font1.setFamilies([u"Dongle"])
        font1.setPointSize(65)
        self.hot_button.setFont(font1)
        self.hot_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.hot_button.setCheckable(True)
        self.blended_button = QPushButton(Form)
        self.drinkType_buttonGroup.addButton(self.blended_button)
        self.blended_button.setObjectName(u"blended_button")
        self.blended_button.setGeometry(QRect(723, 134, 200, 60))
        self.blended_button.setFont(font1)
        self.blended_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}")
        self.blended_button.setCheckable(True)
        self.cold_button = QPushButton(Form)
        self.drinkType_buttonGroup.addButton(self.cold_button)
        self.cold_button.setObjectName(u"cold_button")
        self.cold_button.setGeometry(QRect(408, 134, 200, 60))
        self.cold_button.setFont(font1)
        self.cold_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}")
        self.cold_button.setCheckable(True)
        self.sweetness_label = QLabel(Form)
        self.sweetness_label.setObjectName(u"sweetness_label")
        self.sweetness_label.setGeometry(QRect(93, 241, 200, 103))
        self.sweetness_label.setFont(font1)
        self.sweetness_label.setStyleSheet(u"color: #754926;")
        self.sweet0_button = QPushButton(Form)
        self.sweetness_buttonGroup = QButtonGroup(Form)
        self.sweetness_buttonGroup.setObjectName(u"sweetness_buttonGroup")
        self.sweetness_buttonGroup.addButton(self.sweet0_button)
        self.sweet0_button.setObjectName(u"sweet0_button")
        self.sweet0_button.setGeometry(QRect(343, 258, 100, 60))
        self.sweet0_button.setFont(font1)
        self.sweet0_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.sweet0_button.setCheckable(True)
        self.sweet25_button = QPushButton(Form)
        self.sweetness_buttonGroup.addButton(self.sweet25_button)
        self.sweet25_button.setObjectName(u"sweet25_button")
        self.sweet25_button.setGeometry(QRect(503, 258, 100, 60))
        self.sweet25_button.setFont(font1)
        self.sweet25_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.sweet25_button.setCheckable(True)
        self.sweet50_button = QPushButton(Form)
        self.sweetness_buttonGroup.addButton(self.sweet50_button)
        self.sweet50_button.setObjectName(u"sweet50_button")
        self.sweet50_button.setGeometry(QRect(663, 258, 100, 60))
        self.sweet50_button.setFont(font1)
        self.sweet50_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.sweet50_button.setCheckable(True)
        self.sweet100_button = QPushButton(Form)
        self.sweetness_buttonGroup.addButton(self.sweet100_button)
        self.sweet100_button.setObjectName(u"sweet100_button")
        self.sweet100_button.setGeometry(QRect(823, 258, 100, 60))
        self.sweet100_button.setFont(font1)
        self.sweet100_button.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.sweet100_button.setCheckable(True)
        self.addOn_label = QLabel(Form)
        self.addOn_label.setObjectName(u"addOn_label")
        self.addOn_label.setGeometry(QRect(93, 344, 147, 57))
        self.addOn_label.setFont(font1)
        self.addOn_label.setStyleSheet(u"color: #754926;")
        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(270, 726, 200, 80))
        self.cancel_button.setFont(font1)
        self.cancel_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: #754926;;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #4A321C;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.add_button = QPushButton(Form)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(551, 726, 200, 80))
        self.add_button.setFont(font1)
        self.add_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #4A321C;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping1 = QPushButton(Form)
        self.topping1.setObjectName(u"topping1")
        self.topping1.setGeometry(QRect(93, 439, 200, 60))
        self.topping1.setFont(font1)
        self.topping1.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping1.setCheckable(True)
        self.topping2 = QPushButton(Form)
        self.topping2.setObjectName(u"topping2")
        self.topping2.setGeometry(QRect(304, 439, 200, 60))
        self.topping2.setFont(font1)
        self.topping2.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping2.setCheckable(True)
        self.topping3 = QPushButton(Form)
        self.topping3.setObjectName(u"topping3")
        self.topping3.setGeometry(QRect(514, 439, 200, 60))
        self.topping3.setFont(font1)
        self.topping3.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping3.setCheckable(True)
        self.topping4 = QPushButton(Form)
        self.topping4.setObjectName(u"topping4")
        self.topping4.setGeometry(QRect(723, 439, 200, 60))
        self.topping4.setFont(font1)
        self.topping4.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping4.setCheckable(True)
        self.topping6 = QPushButton(Form)
        self.topping6.setObjectName(u"topping6")
        self.topping6.setGeometry(QRect(304, 536, 200, 60))
        self.topping6.setFont(font1)
        self.topping6.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping6.setCheckable(True)
        self.topping7 = QPushButton(Form)
        self.topping7.setObjectName(u"topping7")
        self.topping7.setGeometry(QRect(514, 536, 200, 60))
        self.topping7.setFont(font1)
        self.topping7.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping7.setCheckable(True)
        self.topping5 = QPushButton(Form)
        self.topping5.setObjectName(u"topping5")
        self.topping5.setGeometry(QRect(93, 536, 200, 60))
        self.topping5.setFont(font1)
        self.topping5.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping5.setCheckable(True)
        self.topping8 = QPushButton(Form)
        self.topping8.setObjectName(u"topping8")
        self.topping8.setGeometry(QRect(723, 536, 200, 60))
        self.topping8.setFont(font1)
        self.topping8.setStyleSheet(u"QPushButton{\n"
"background-color: #D8B797;\n"
"border-radius: 20px;\n"
"color: #4A321C;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #754926;\n"
"border-radius: 20px;\n"
"color: #F9F5F0;\n"
"}\n"
"")
        self.topping8.setCheckable(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.menu_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.hot_button.setText(QCoreApplication.translate("Form", u"Hot", None))
        self.blended_button.setText(QCoreApplication.translate("Form", u"Blended", None))
        self.cold_button.setText(QCoreApplication.translate("Form", u"Cold", None))
        self.sweetness_label.setText(QCoreApplication.translate("Form", u"Sweetness", None))
        self.sweet0_button.setText(QCoreApplication.translate("Form", u"0", None))
        self.sweet25_button.setText(QCoreApplication.translate("Form", u"25", None))
        self.sweet50_button.setText(QCoreApplication.translate("Form", u"50", None))
        self.sweet100_button.setText(QCoreApplication.translate("Form", u"100", None))
        self.addOn_label.setText(QCoreApplication.translate("Form", u"Add-On", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"Add", None))
        self.topping1.setText(QCoreApplication.translate("Form", u"Button1", None))
        self.topping2.setText(QCoreApplication.translate("Form", u"Button2", None))
        self.topping3.setText(QCoreApplication.translate("Form", u"Button3", None))
        self.topping4.setText(QCoreApplication.translate("Form", u"Button4", None))
        self.topping6.setText(QCoreApplication.translate("Form", u"Button6", None))
        self.topping7.setText(QCoreApplication.translate("Form", u"Button7", None))
        self.topping5.setText(QCoreApplication.translate("Form", u"Button5", None))
        self.topping8.setText(QCoreApplication.translate("Form", u"Buttom8", None))
    # retranslateUi

