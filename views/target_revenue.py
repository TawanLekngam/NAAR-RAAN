# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'financial.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet(u"background-color: rgb(249, 245, 240);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 90, 625, 900))
        self.widget.setStyleSheet(u"background-color: rgb(216, 183, 151);\n"
"")
        self.listWidget = QListWidget(self.widget)
        brush = QBrush(QColor(216, 183, 151, 255))
        brush.setStyle(Qt.NoBrush)
        font = QFont()
        font.setPointSize(65)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font);
        __qlistwidgetitem.setBackground(brush);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(13, 130, 600, 750))
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(u"border-top: 5px solid #4A321C;")
        self.label_month = QLabel(self.widget)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setGeometry(QRect(60, 40, 171, 61))
        font1 = QFont()
        font1.setFamilies([u"Dongle"])
        font1.setPointSize(65)
        self.label_month.setFont(font1)
        self.label_revenue = QLabel(self.widget)
        self.label_revenue.setObjectName(u"label_revenue")
        self.label_revenue.setGeometry(QRect(390, 40, 211, 61))
        self.label_revenue.setFont(font1)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(840, 115, 1000, 720))
        self.widget_2.setStyleSheet(u"")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 470, 171, 61))
        font2 = QFont()
        font2.setPointSize(65)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 565, 221, 51))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 650, 341, 61))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(670, 470, 131, 61))
        font3 = QFont()
        font3.setPointSize(65)
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(670, 565, 131, 51))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(670, 650, 131, 51))
        self.label_6.setFont(font)
        self.pushButton_edit = QPushButton(Form)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(1620, 878, 220, 80))
        self.pushButton_edit.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"  JAN. 2022      1000", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_month.setText(QCoreApplication.translate("Form", u"Month", None))
        self.label_revenue.setText(QCoreApplication.translate("Form", u"Revenue", None))
        self.label.setText(QCoreApplication.translate("Form", u"Target", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Revenue", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Amount Left", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"9000", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"5000", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"4000", None))
        self.pushButton_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
    # retranslateUi

