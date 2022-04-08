import os.path
from PySide6.QtWidgets import *
from PySide6.QtGui import (QFont, QMouseEvent)
from PySide6.QtCore import (QRect)


class Widget(QWidget):  # base Widget for dymamic widget

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

    def _set_stylesheet(self, filename: str) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        theme_dir = os.path.join(base_dir, "themes")
        real_path = os.path.join(theme_dir, filename)
        with open(real_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)
        file.close()


class UserTab(Widget):  # for show current user and go to another views

    def __init__(self, parent: QWidget = None):
        Widget.__init__(self, parent)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.underMouse():
            print("Log: On me.")


class MenuItem(Widget):

    def __init__(self, parent: QWidget):
        Widget.__init__(self, parent)


class OrderItem(Widget):

    def __init__(self, parent: QWidget):
        Widget.__init__(self, parent)


class OrderDetails(Widget):  # order detail for menu order view

    def __init__(self, parent: QWidget = None):
        Widget.__init__(self, parent)
        self.setFixedSize(1000, 850)

        menu_name = QLabel("Test One Two", self)
        menu_name.setObjectName("menu_name")
        menu_name.setFont(self._get_font(80))
        menu_name.setGeometry(QRect(93, 57, 830, 77))

        hot_button = QPushButton("Hot", self)
        hot_button.setObjectName("default_button")
        hot_button.setFont(self._get_font(65))
        hot_button.setGeometry(QRect(93, 134, 200, 60))

        cold_button = QPushButton("Cold", self)
        cold_button.setObjectName("default_button")
        cold_button.setFont(self._get_font(65))
        cold_button.setGeometry(QRect(408, 134, 200, 60))

        blended_button = QPushButton("Blended", self)
        blended_button.setObjectName("default_button")
        blended_button.setFont(self._get_font(65))
        blended_button.setGeometry(QRect(723, 134, 200, 60))

        sweetness_label = QLabel("Sweetness", self)
        sweetness_label.setObjectName("sweetness_label")
        sweetness_label.setFont(self._get_font(65))
        sweetness_label.setGeometry(QRect(93, 241, 200, 103))

        sweet0_button = QPushButton("0", self)
        sweet0_button.setObjectName("default_button")
        sweet0_button.setFont(self._get_font(65))
        sweet0_button.setGeometry(QRect(343, 258, 100, 60))

        sweet25_button = QPushButton("25", self)
        sweet25_button.setObjectName("default_button")
        sweet25_button.setFont(self._get_font(65))
        sweet25_button.setGeometry(QRect(503, 258, 100, 60))

        sweet50_button = QPushButton("50", self)
        sweet50_button.setObjectName("default_button")
        sweet50_button.setFont(self._get_font(65))
        sweet50_button.setGeometry(QRect(663, 258, 100, 60))

        sweet100_button = QPushButton("100", self)
        sweet100_button.setObjectName("default_button")
        sweet100_button.setFont(self._get_font(65))
        sweet100_button.setGeometry(QRect(823, 258, 100, 60))

        addOn_label = QPushButton("Add-On", self)
        addOn_label.setObjectName("addOn_label")
        addOn_label.setFont(self._get_font(65))
        addOn_label.setGeometry(QRect(93, 344, 147, 57))

        topping1_button = QPushButton("Topping1", self)
        topping1_button.setObjectName("default_button")
        topping1_button.setFont(self._get_font(65))
        topping1_button.setGeometry(QRect(93, 439, 200, 60))

        topping2_button = QPushButton("Topping2", self)
        topping2_button.setObjectName("default_button")
        topping2_button.setFont(self._get_font(65))
        topping2_button.setGeometry(QRect(304, 439, 200, 60))

        topping3_button = QPushButton("Topping3", self)
        topping3_button.setObjectName("default_button")
        topping3_button.setFont(self._get_font(65))
        topping3_button.setGeometry(QRect(514, 439, 200, 60))

        topping4_button = QPushButton("Topping4", self)
        topping4_button.setObjectName("default_button")
        topping4_button.setFont(self._get_font(65))
        topping4_button.setGeometry(QRect(723, 439, 200, 60))

        topping5_button = QPushButton("Topping5", self)
        topping5_button.setObjectName("default_button")
        topping5_button.setFont(self._get_font(65))
        topping5_button.setGeometry(QRect(93, 536, 200, 60))

        topping6_button = QPushButton("Topping6", self)
        topping6_button.setObjectName("default_button")
        topping6_button.setFont(self._get_font(65))
        topping6_button.setGeometry(QRect(304, 536, 200, 60))

        topping7_button = QPushButton("Topping7", self)
        topping7_button.setObjectName("default_button")
        topping7_button.setFont(self._get_font(65))
        topping7_button.setGeometry(QRect(514, 536, 200, 60))

        topping8_button = QPushButton("Topping8", self)
        topping8_button.setObjectName("default_button")
        topping8_button.setFont(self._get_font(65))
        topping8_button.setGeometry(QRect(723, 536, 200, 60))

        cancel_button = QPushButton("Cancel", self)
        cancel_button.setObjectName("cancel_add_button")
        cancel_button.setFont(self._get_font(65))
        cancel_button.setGeometry(QRect(270, 726, 200, 80))

        add_button = QPushButton("Add", self)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(self._get_font(65))
        add_button.setGeometry(QRect(551, 726, 200, 80))

        self.show()

class OrderTracking(Widget):
    def __init__(self, parent: QWidget = None):
        Widget.__init__(self, parent)
        self.resize(1920, 1080)

        self.scrollArea_todo = QScrollArea(self)
        self.scrollArea_todo.setObjectName(u"scrollArea_todo")
        self.scrollArea_todo.setGeometry(QRect(81, 273, 500, 600))
        self.scrollArea_todo.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 598))

        self.listView_todo_1 = QListView(self.scrollAreaWidgetContents)
        self.listView_todo_1.setObjectName(u"listView_todo_1")
        self.listView_todo_1.setGeometry(QRect(25, 35, 450, 300))

        self.listView_todo_2 = QListView(self.scrollAreaWidgetContents)
        self.listView_todo_2.setObjectName(u"listView_todo_2")
        self.listView_todo_2.setGeometry(QRect(25, 375, 450, 300))

        self.scrollArea_todo.setWidget(self.scrollAreaWidgetContents)

        self.label_todo = QLabel("TO DO",self)
        self.label_todo.setObjectName("label_todo")
        self.label_todo.setGeometry(QRect(118, 197, 200, 61))
        self.label_todo.setFont(self._get_font(65))
        

        self.label_doing = QLabel("DOING",self)
        self.label_doing.setObjectName(u"label_doing")
        self.label_doing.setGeometry(QRect(760, 197, 200, 61))
        self.label_doing.setFont(self._get_font(65))
        

        self.scrollArea_doing = QScrollArea(self)
        self.scrollArea_doing.setObjectName(u"scrollArea_doing")
        self.scrollArea_doing.setGeometry(QRect(729, 273, 500, 750))
        self.scrollArea_doing.setWidgetResizable(True)

        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 498, 748))

        self.listView_doing_1 = QListView(self.scrollAreaWidgetContents_2)
        self.listView_doing_1.setObjectName(u"listView_doing_1")
        self.listView_doing_1.setGeometry(QRect(25, 35, 450, 300))
        self.listView_doing_2 = QListView(self.scrollAreaWidgetContents_2)
        self.listView_doing_2.setObjectName(u"listView_doing_2")
        self.listView_doing_2.setGeometry(QRect(25, 375, 450, 300))

        self.scrollArea_doing.setWidget(self.scrollAreaWidgetContents_2)

        self.label_done = QLabel("DONE",self)
        self.label_done.setObjectName(u"label_done")
        self.label_done.setGeometry(QRect(1377, 197, 171, 61))
        self.label_done.setFont(self._get_font(65))
        

        self.scrollArea_done = QScrollArea(self)
        self.scrollArea_done.setObjectName(u"scrollArea_done")
        self.scrollArea_done.setGeometry(QRect(1345, 273, 500, 500))
        self.scrollArea_done.setWidgetResizable(True)

        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 498, 498))

        self.listView_done_1 = QListView(self.scrollAreaWidgetContents_3)
        self.listView_done_1.setObjectName(u"listView_done_1")
        self.listView_done_1.setGeometry(QRect(25, 35, 450, 300))

        self.scrollArea_done.setWidget(self.scrollAreaWidgetContents_3)

        self.show()

class TargetRevenue(Widget):
    def __init__(self, parent: QWidget = None):
        Widget.__init__(self, parent)

        self.resize(1920, 1080)
        
        self.widget_date = QWidget(self)
        self.widget_date.setObjectName(u"widget_date")
        self.widget_date.setGeometry(QRect(80, 90, 625, 900))
        
        self.listWidget_date = QListWidget(self.widget_date)
        self.listWidget_date.setObjectName(u"listWidget_date")
        self.listWidget_date.setGeometry(QRect(13, 130, 600, 750))
        
        self.label_month = QLabel("Month",self.widget_date)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setGeometry(QRect(60, 40, 171, 61))
        self.label_month.setFont(self._get_font(65))
        
        self.label_revenue = QLabel("Revenue",self.widget_date)
        self.label_revenue.setObjectName(u"label_revenue")
        self.label_revenue.setGeometry(QRect(390, 40, 211, 61))
        self.label_revenue.setFont(self._get_font(65))

        self.widget_report = QWidget(self)
        self.widget_report.setObjectName(u"widget_report")
        self.widget_report.setGeometry(QRect(840, 115, 1000, 720))
        
        self.label_target = QLabel("Target",self.widget_report)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setGeometry(QRect(200, 470, 171, 61))
        self.label_target.setFont(self._get_font(65))
        
        self.label_revenue_pie = QLabel("Revenue",self.widget_report)
        self.label_revenue_pie.setObjectName(u"label_revenue_pie")
        self.label_revenue_pie.setGeometry(QRect(200, 565, 221, 51))
        self.label_revenue_pie.setFont(self._get_font(65))
        
        self.label_amount_left = QLabel("Amount Left",self.widget_report)
        self.label_amount_left.setObjectName(u"label_amount_left")
        self.label_amount_left.setGeometry(QRect(200, 650, 341, 61))
        self.label_amount_left.setFont(self._get_font(65))
        
        self.label_money_target = QLabel("9000",self.widget_report)
        self.label_money_target.setObjectName(u"label_money_target")
        self.label_money_target.setGeometry(QRect(670, 470, 131, 61))
        self.label_money_target.setFont(self._get_font(65))
        
        self.label_money_revenue = QLabel("5000",self.widget_report)
        self.label_money_revenue.setObjectName(u"label_money_revenue")
        self.label_money_revenue.setGeometry(QRect(670, 565, 131, 51))
        self.label_money_revenue.setFont(self._get_font(65))
       
        self.label_money_left = QLabel("4000",self.widget_report)
        self.label_money_left.setObjectName(u"label_money_left")
        self.label_money_left.setGeometry(QRect(670, 650, 131, 51))
        self.label_money_left.setFont(self._get_font(65))
        
        self.pushButton_edit = QPushButton(self)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(1620, 878, 220, 80))
        self.pushButton_edit.setFont(self._get_font(65))
        
        self.show()