import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Target_Revenue(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.resize(1920, 1080)
        
        self.widget_date = QWidget(self)
        self.widget_date.setObjectName(u"widget_date")
        self.widget_date.setGeometry(QRect(80, 90, 625, 900))
        self.widget_date.setStyleSheet(u"")
        
        self.listWidget_date = QListWidget(self.widget_date)
        self.listWidget_date.setObjectName(u"listWidget_date")
        self.listWidget_date.setGeometry(QRect(13, 130, 600, 750))
        
        
        self.label_month = QLabel("Month",self.widget_date)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setGeometry(QRect(60, 40, 171, 61))
        
        self.label_revenue = QLabel("Revenue",self.widget_date)
        self.label_revenue.setObjectName(u"label_revenue")
        self.label_revenue.setGeometry(QRect(390, 40, 211, 61))

        self.widget_report = QWidget(self)
        self.widget_report.setObjectName(u"widget_report")
        self.widget_report.setGeometry(QRect(840, 115, 1000, 720))
        
        self.label_target = QLabel("Target",self.widget_report)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setGeometry(QRect(200, 470, 171, 61))
        
        self.label_revenue_pie = QLabel("Revenue",self.widget_report)
        self.label_revenue_pie.setObjectName(u"label_revenue_pie")
        self.label_revenue_pie.setGeometry(QRect(200, 565, 221, 51))
        
        self.label_amount_left = QLabel("Amount Left",self.widget_report)
        self.label_amount_left.setObjectName(u"label_amount_left")
        self.label_amount_left.setGeometry(QRect(200, 650, 341, 61))
        
        self.label_money_target = QLabel("9000",self.widget_report)
        self.label_money_target.setObjectName(u"label_money_target")
        self.label_money_target.setGeometry(QRect(670, 470, 131, 61))
        
        
        self.label_money_revenue = QLabel("5000",self.widget_report)
        self.label_money_revenue.setObjectName(u"label_money_revenue")
        self.label_money_revenue.setGeometry(QRect(670, 565, 131, 51))
       
        self.label_money_left = QLabel("4000",self.widget_report)
        self.label_money_left.setObjectName(u"label_money_left")
        self.label_money_left.setGeometry(QRect(670, 650, 131, 51))
        
        self.pushButton_edit = QPushButton(self)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(1620, 878, 220, 80))
        
        self.show()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    target_revenue = Target_Revenue()
    sys.exit(app.exec())

    