"""
    contain all views and utility widgets.
"""

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from theme import Theme


"""
    application view.
"""


class LoginView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1920, 1080)

        label_logo = QLabel(self)
        label_logo.setObjectName("label_logo")
        label_logo.setGeometry(QRect(846, 158, 252, 252))
        label_logo.setPixmap(QPixmap("src/asset/Image/logo.png"))

        label_username = QLabel("Username", self)
        label_username.setObjectName("label_username")
        label_username.setFont(Theme.DONGLE_BOLD_65)
        label_username.setGeometry(QRect(583, 537, 321, 72))

        label_password = QLabel("Password", self)
        label_password.setObjectName("label_password")
        label_password.setFont(Theme.DONGLE_BOLD_65)
        label_password.setGeometry(QRect(583, 706, 291, 72))

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_username.setFont(Theme.DONGLE_BOLD_65)
        self.lineEdit_username.setGeometry(QRect(806, 520, 600, 80))

        self.error = QLabel("Incorrect username or password", self)
        self.error.setObjectName("default_label")
        self.error.setFont(Theme.DONGLE_REGULAR_50)
        self.error.setGeometry(QRect(836, 600, 600, 50))
        

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setFont(Theme.DONGLE_REGULAR_50)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setGeometry(QRect(806, 685, 600, 80))

        # self.password_error = QLabel("Error2 nah nah nah nah nah", self)
        # self.password_error.setObjectName("default_label")
        # self.password_error.setFont(Theme.DONGLE_REGULAR_50)
        # self.password_error.setGeometry(QRect(836, 765, 600, 50))

        self.login_button = QPushButton(self)
        self.login_button.setObjectName("logIn_button")
        self.login_button.setGeometry(QRect(860, 860, 200, 80))

        self.hide_error_label()
        self.setStyleSheet(Theme.get_stylesheet())

    def reset(self) -> None:
        self.clear_info()
        self.hide_error_label()

    def clear_info(self) -> None:
        self.lineEdit_username.setText("")
        self.lineEdit_password.setText("")

    def show_error_label(self) -> None:
        self.error.show()

    def hide_error_label(self) -> None:
        self.error.hide()

    def get_username(self) -> str:
        return self.lineEdit_username.text()

    def get_password(self) -> str:
        return self.lineEdit_password.text()

    def set_login_button_listener(self, function) -> None:
        self.login_button.clicked.connect(function)


class HomeView(QWidget):

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1920, 1080)

        self.tab_frame = QFrame(self)
        self.tab_frame.setObjectName("tab_frame")
        self.tab_frame.setGeometry(QRect(0, 0, 1920, 100))

        self.user_button = QPushButton("User Name", self.tab_frame)
        self.user_button.setObjectName("user_base_page")
        self.user_button.setGeometry(QRect(1552, 0, 300, 100))
        self.user_button.setFont(Theme.DONGLE_BOLD_65)

        self.home_button = QPushButton(self.tab_frame)
        self.home_button.setObjectName("home_button_base_page")
        self.home_button.setGeometry(QRect(36, 0, 100, 100))

        self.auditLog_button = QPushButton(self.tab_frame)
        self.auditLog_button.setObjectName("history_button_base_page")
        self.auditLog_button.setGeometry(QRect(136, 0, 100, 100))

        self.receipt_button = QPushButton(self.tab_frame)
        self.receipt_button.setObjectName("receipt_button_base_page")
        self.receipt_button.setGeometry(QRect(236, 0, 100, 100))

        self.menu_button = QPushButton(self.tab_frame)
        self.menu_button.setObjectName("menu_button_base_page")
        self.menu_button.setGeometry(QRect(336, 0, 100, 100))

        self.employee_button = QPushButton(self.tab_frame)
        self.employee_button.setObjectName("employee_button_base_page")
        self.employee_button.setGeometry(QRect(436, 0, 100, 100))

        self.stacked_frame = QFrame(self)
        self.stacked_frame.setObjectName("stacked_frame")
        self.stacked_frame.setGeometry(QRect(0, 100, 1920, 980))

        self.stacked_widget = QStackedWidget(self.stacked_frame)
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setGeometry(QRect(0, -50, 1200, 1000))

        # self.drink_detail = DrinkDetailView()
        # self.drink_detail.setObjectName("drink_detail_page")
        # self.stacked_widget.addWidget(self.drink_detail)

        # self.bakery_detail = BakeryDetailView()
        # self.bakery_detail.setObjectName("bakery_detail_page")
        # self.stacked_widget.addWidget(self.bakery_detail)

        # self.menu_list_page = MenuListView()
        # self.menu_list_page.setObjectName("menu_list_page")
        # self.stacked_widget.addWidget(self.menu_list_page)

        self.setStyleSheet(Theme.get_stylesheet())

    def add_view(self, view: QWidget) -> None:
        self.stackedWidget.addWidget(view)

    def show_admin_menu(self) -> None:
        pass

    def set_username(self, username: str) -> None:
        self.user_button.setText(username)


class OrderView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        order_frame = QFrame(self)
        order_frame.setObjectName("order_frame")
        order_frame.setGeometry(QRect(1143, 115, 700, 720))

        order_scrollArea = QScrollArea(order_frame)
        order_scrollArea.setObjectName("order_scrollArea")
        order_scrollArea.setGeometry(QRect(25, 40, 650, 580))

        order_scrollAreaContents = QWidget(order_scrollArea)
        order_scrollAreaContents.setObjectName("order_scrollAreaContents")
        order_scrollAreaContents.setGeometry(QRect(0, 0, 648, 578))
        order_scrollArea.setWidget(order_scrollAreaContents)

        line = QFrame(order_frame)
        line.setObjectName("order_line")
        line.setGeometry(QRect(25, 634, 650, 5))

        total_label = QLabel("Total", order_frame)
        total_label.setObjectName("default_label")
        total_label.setFont(Theme.DONGLE_BOLD_65)
        total_label.setGeometry(QRect(420, 660, 110, 40))

        number_label = QLabel("0", order_frame)
        number_label.setObjectName("default_label")
        number_label.setFont(Theme.DONGLE_BOLD_65)
        number_label.setGeometry(QRect(540, 660, 115, 40))

        self.order_button = QPushButton("Order", self)
        self.order_button.setObjectName("cancel_add_button")
        self.order_button.setFont(Theme.DONGLE_BOLD_65)
        self.order_button.setGeometry(QRect(1145, 885, 700, 80))

        self.setStyleSheet(Theme.get_stylesheet())

        def set_orderview(self, widget: QWidget) -> None:
            pass


class OrderList(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(620, 85)

        self.name_label = QLabel("Menu Name", self)
        self.name_label.setObjectName("default_label")
        self.name_label.setFont(Theme.DONGLE_BOLD_65)
        self.name_label.setGeometry(QRect(20, 25, 230, 40))

        self.minus_button = QPushButton("-", self)
        self.minus_button.setObjectName("cancel_add_button")
        self.minus_button.setFont(Theme.DONGLE_REGULAR_65)
        self.minus_button.setGeometry(QRect(290, 15, 50 , 50))

        self.quantity_label = QLabel("1", self)
        self.quantity_label.setObjectName("default_label")
        self.quantity_label.setFont(Theme.DONGLE_REGULAR_65)
        self.quantity_label.setGeometry(QRect(390, 25, 230, 40))

        self.plus_button = QPushButton("+", self)
        self.plus_button.setObjectName("cancel_add_button")
        self.plus_button.setFont(Theme.DONGLE_REGULAR_65)
        self.plus_button.setGeometry(QRect(460, 15, 50 , 50))

        self.price_label = QLabel("00", self)
        self.price_label.setObjectName("default_label")
        self.price_label.setFont(Theme.DONGLE_REGULAR_65)
        self.price_label.setGeometry(QRect(550, 25, 230, 40))

        self.setStyleSheet(Theme.get_stylesheet())


class MenuListView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        menu_frame = QFrame(self)
        menu_frame.setObjectName("menu_frame")
        menu_frame.setGeometry(75, 115, 1000, 850)

        menu_label = QLabel("Menu", menu_frame)
        menu_label.setObjectName("menu_label")
        menu_label.setFont(Theme.DONGLE_BOLD_80)
        menu_label.setGeometry(QRect(54, 26, 128, 116))

        self.search_bar = QLineEdit(menu_frame)
        self.search_bar.setObjectName("search_bar")
        self.search_bar.setFont(Theme.DONGLE_BOLD_65)
        self.search_bar.setGeometry(QRect(272, 40, 677, 80))

        menu_scrollArea = QScrollArea(menu_frame)
        menu_scrollArea.setObjectName("menu_scrollArea")
        menu_scrollArea.setGeometry(QRect(57, 169, 885, 630))

        menu_scrollAreaContents = QWidget(menu_scrollArea)
        menu_scrollAreaContents.setObjectName("menu_scrollAreaContents")
        menu_scrollAreaContents.setGeometry(QRect(0, 0, 883, 628))
        menu_scrollArea.setWidget(menu_scrollAreaContents)

        self.setStyleSheet(Theme.get_stylesheet())


class MenuListItem(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(880, 80)
        self.setObjectName("menu_list_widget")

        self.name_button = QPushButton("Menu Name", self)
        self.name_button.setObjectName("list_button")
        self.name_button.setFont(Theme.DONGLE_REGULAR_65)
        self.name_button.setGeometry(QRect(50, 10, 780, 50))

        white_line = QFrame(self)
        white_line.setObjectName("white_line")
        white_line.setGeometry(QRect(30, 70, 820, 3))

        self.setStyleSheet(Theme.get_stylesheet())


class DrinkDetailView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        order_frame = QFrame(self)
        order_frame.setObjectName("order_frame")
        order_frame.setGeometry(75, 115, 1000, 850)

        menu_name = QLabel("Name Test", order_frame)
        menu_name.setObjectName("default_label")
        menu_name.setFont(Theme.DONGLE_BOLD_80)
        menu_name.setGeometry(QRect(100, 70, 830, 77))

        hot_button = QPushButton("Hot", order_frame)
        hot_button.setObjectName("default_button")
        hot_button.setFont(Theme.DONGLE_REGULAR_65)
        hot_button.setGeometry(QRect(100, 147, 200, 60))
        hot_button.setCheckable(True)

        cold_button = QPushButton("Cold", order_frame)
        cold_button.setObjectName("default_button")
        cold_button.setFont(Theme.DONGLE_REGULAR_65)
        cold_button.setGeometry(QRect(415, 147, 200, 60))
        cold_button.setCheckable(True)

        blended_button = QPushButton("Blended", order_frame)
        blended_button.setObjectName("default_button")
        blended_button.setFont(Theme.DONGLE_REGULAR_65)
        blended_button.setGeometry(QRect(730, 147, 200, 60))
        blended_button.setCheckable(True)

        drinkType_buttonGroup = QButtonGroup(order_frame)
        drinkType_buttonGroup.setObjectName("drinkType_ButtonGroup")
        drinkType_buttonGroup.addButton(hot_button)
        drinkType_buttonGroup.addButton(cold_button)
        drinkType_buttonGroup.addButton(blended_button)

        sweetness_label = QLabel("Sweetness", order_frame)
        sweetness_label.setObjectName("sweetness_label")
        sweetness_label.setFont(Theme.DONGLE_REGULAR_65)
        sweetness_label.setGeometry(QRect(100, 258, 200, 103))

        sweet0_button = QPushButton("0", order_frame)
        sweet0_button.setObjectName("default_button")
        sweet0_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet0_button.setGeometry(QRect(358, 271, 100, 60))
        sweet0_button.setCheckable(True)

        sweet25_button = QPushButton("25", order_frame)
        sweet25_button.setObjectName("default_button")
        sweet25_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet25_button.setGeometry(QRect(515, 271, 100, 60))
        sweet25_button.setCheckable(True)

        sweet50_button = QPushButton("50", order_frame)
        sweet50_button.setObjectName("default_button")
        sweet50_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet50_button.setGeometry(QRect(673, 271, 100, 60))
        sweet50_button.setCheckable(True)

        sweet100_button = QPushButton("100", order_frame)
        sweet100_button.setObjectName("default_button")
        sweet100_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet100_button.setGeometry(QRect(830, 271, 100, 60))
        sweet100_button.setCheckable(True)

        sweetness_buttonGroup = QButtonGroup(order_frame)
        sweetness_buttonGroup.setObjectName("sweetness_buttonGroup")
        sweetness_buttonGroup.addButton(sweet0_button)
        sweetness_buttonGroup.addButton(sweet25_button)
        sweetness_buttonGroup.addButton(sweet50_button)
        sweetness_buttonGroup.addButton(sweet100_button)

        cancel_button = QPushButton("Cancel", order_frame)
        cancel_button.setObjectName("cancel_add_button")
        cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        cancel_button.setGeometry(QRect(277, 739, 200, 80))

        add_button = QPushButton("Add", order_frame)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(558, 739, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())

class BakeryDetailView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        order_frame = QFrame(self)
        order_frame.setObjectName("order_frame")
        order_frame.setGeometry(75, 115, 1000, 850)

        menu_name = QLabel("Name Test", order_frame)
        menu_name.setObjectName("default_label")
        menu_name.setFont(Theme.DONGLE_BOLD_80)
        menu_name.setGeometry(QRect(100, 70, 830, 77))

        cancel_button = QPushButton("Cancel", order_frame)
        cancel_button.setObjectName("cancel_add_button")
        cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        cancel_button.setGeometry(QRect(277, 739, 200, 80))

        add_button = QPushButton("Add", order_frame)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(558, 739, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())


# class TargetRevenueView(QWidget):
#     def __init__(self, parent: QWidget = None):
#         QWidget.__init__(self, parent)

#         self.resize(1920, 1080)

#         self.widget_date = QWidget(self)
#         self.widget_date.setObjectName("widget_date")
#         self.widget_date.setGeometry(QRect(80, 65, 625, 900))

#         self.listWidget_date = QListWidget(self.widget_date)
#         self.listWidget_date.setObjectName("listWidget_date")
#         self.listWidget_date.setGeometry(QRect(13, 130, 600, 750))

#         self.label_month = QLabel("Month", self.widget_date)
#         self.label_month.setObjectName("label_date_target")
#         self.label_month.setGeometry(QRect(60, 40, 171, 61))
#         self.label_month.setFont(Theme.DONGLE_BOLD_65)

#         self.label_revenue = QLabel("Revenue", self.widget_date)
#         self.label_revenue.setObjectName("label_date_target")
#         self.label_revenue.setGeometry(QRect(390, 40, 211, 61))
#         self.label_revenue.setFont(Theme.DONGLE_BOLD_65)

#         self.widget_report = QWidget(self)
#         self.widget_report.setObjectName("widget_report")
#         self.widget_report.setGeometry(QRect(840, 100, 1000, 720))

#         self.label_target = QLabel("Target", self.widget_report)
#         self.label_target.setObjectName("label_target")
#         self.label_target.setGeometry(QRect(200, 470, 171, 61))
#         self.label_target.setFont(Theme.DONGLE_BOLD_65)

#         self.label_revenue_pie = QLabel("Revenue", self.widget_report)
#         self.label_revenue_pie.setObjectName("label_target")
#         self.label_revenue_pie.setGeometry(QRect(200, 565, 221, 51))
#         self.label_revenue_pie.setFont(Theme.DONGLE_BOLD_65)

#         self.label_amount_left = QLabel("Amount Left", self.widget_report)
#         self.label_amount_left.setObjectName("label_target")
#         self.label_amount_left.setGeometry(QRect(200, 650, 341, 61))
#         self.label_amount_left.setFont(Theme.DONGLE_BOLD_65)

#         self.label_money_target = QLabel("9000", self.widget_report)
#         self.label_money_target.setObjectName("label_target")
#         self.label_money_target.setGeometry(QRect(670, 470, 131, 61))
#         self.label_money_target.setFont(Theme.DONGLE_REGULAR_65)

#         self.label_money_revenue = QLabel("5000", self.widget_report)
#         self.label_money_revenue.setObjectName("label_target")
#         self.label_money_revenue.setGeometry(QRect(670, 565, 131, 51))
#         self.label_money_revenue.setFont(Theme.DONGLE_REGULAR_65)

#         self.label_money_left = QLabel("4000", self.widget_report)
#         self.label_money_left.setObjectName("label_target")
#         self.label_money_left.setGeometry(QRect(670, 650, 131, 51))
#         self.label_money_left.setFont(Theme.DONGLE_REGULAR_65)

#         self.pushButton_edit = QPushButton("Edit", self)
#         self.pushButton_edit.setObjectName("pushButton_edit")
#         self.pushButton_edit.setGeometry(QRect(1620, 870, 220, 80))
#         self.pushButton_edit.setFont(Theme.DONGLE_BOLD_65)

#         self.setStyleSheet(Theme.get_stylesheet())


class AuditLogView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(1920, 1080)

        self.widget_auditlog = QWidget(self)
        self.widget_auditlog.setObjectName("widget_auditlog")
        self.widget_auditlog.setGeometry(QRect(60, 100, 1800, 980))

        self.label_date = QLabel("Date", self.widget_auditlog)
        self.label_date.setObjectName("label_details")
        self.label_date.setGeometry(QRect(100, 70, 151, 61))
        self.label_date.setFont(Theme.DONGLE_BOLD_70)

        self.label_time = QLabel("Time", self.widget_auditlog)
        self.label_time.setObjectName("label_details")
        self.label_time.setGeometry(QRect(400, 70, 151, 61))
        self.label_time.setFont(Theme.DONGLE_BOLD_70)

        self.label_name = QLabel("Name", self.widget_auditlog)
        self.label_name.setObjectName("label_details")
        self.label_name.setGeometry(QRect(640, 70, 171, 61))
        self.label_name.setFont(Theme.DONGLE_BOLD_70)

        self.label_activity = QLabel("Activity", self.widget_auditlog)
        self.label_activity.setObjectName("label_details")
        self.label_activity.setGeometry(QRect(1080, 70, 231, 61))
        self.label_activity.setFont(Theme.DONGLE_BOLD_70)

        self.listWidget_auditlog = QListWidget(self.widget_auditlog)
        self.listWidget_auditlog.setObjectName("listWidget_auditlog")
        self.listWidget_auditlog.setGeometry(QRect(39, 150, 1722, 810))

        self.setStyleSheet(Theme.get_stylesheet())


class LogItem(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(1725, 80)
        self.setObjectName("menu_list_widget")

        self.date = QLabel("01/01/2022", self)
        self.date.setObjectName("default_label")
        self.date.setFont(Theme.DONGLE_REGULAR_65)
        self.date.setGeometry(QRect(100, 10, 211, 41))
        
        self.time = QLabel("00:00", self)
        self.time.setObjectName("default_label")
        self.time.setFont(Theme.DONGLE_REGULAR_65)
        self.time.setGeometry(QRect(400, 10, 111, 41))

        self.name_act = QLabel("Name Act", self)
        self.name_act.setObjectName("default_label")
        self.name_act.setFont(Theme.DONGLE_REGULAR_65)
        self.name_act.setGeometry(QRect(640, 10, 961, 41))

        line = QFrame(self)
        line.setObjectName("white_line")
        line.setGeometry(QRect(80, 70, 1550, 3))

        self.setStyleSheet(Theme.get_stylesheet())


class MenuAdminView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        admin_frame = QFrame(self)
        admin_frame.setObjectName("admin_frame")
        admin_frame.setGeometry(75, 115, 1000, 850)

        menu_label = QLabel("Menu", admin_frame)
        menu_label.setObjectName("menu_label")
        menu_label.setFont(Theme.DONGLE_BOLD_80)
        menu_label.setGeometry(QRect(55, 70, 130, 51))

        self.search_bar = QLineEdit(admin_frame)
        self.search_bar.setObjectName("search_bar")
        self.search_bar.setFont(Theme.DONGLE_BOLD_65)
        self.search_bar.setGeometry(QRect(260, 53, 680, 80))

        admin_scrollArea = QScrollArea(admin_frame)
        admin_scrollArea.setObjectName("admin_scrollArea")
        admin_scrollArea.setGeometry(QRect(55, 182, 890, 480))

        admin_scrollAreaContents = QWidget(admin_scrollArea)
        admin_scrollAreaContents.setObjectName("admin_scrollAreaContents")
        admin_scrollAreaContents.setGeometry(QRect(0, 0, 888, 478))
        admin_scrollArea.setWidget(admin_scrollAreaContents)

        add_button = QPushButton("+", self)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(915, 820, 100, 100))

        self.setStyleSheet(Theme.get_stylesheet())


class AddMenuAdmin(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)
        self.setObjectName("admin_widget")

        name_label = QLabel("Name", self)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name_bar = QLineEdit(self)
        self.name_bar.setObjectName("input_bar")
        self.name_bar.setFont(Theme.DONGLE_REGULAR_65)
        self.name_bar.setGeometry(QRect(210, 49, 470, 60))

        type_label = QLabel("Type", self)
        type_label.setObjectName("default_label")
        type_label.setFont(Theme.DONGLE_BOLD_65)
        type_label.setGeometry(QRect(33, 185, 111, 41))

        self.drink_button = QRadioButton("Drink", self)
        self.drink_button.setObjectName("default_radio")
        self.drink_button.setFont(Theme.DONGLE_REGULAR_65)
        self.drink_button.setGeometry(QRect(210, 185, 151, 41))

        self.bakery_button = QRadioButton("Bakery", self)
        self.bakery_button.setObjectName("default_radio")
        self.bakery_button.setFont(Theme.DONGLE_REGULAR_65)
        self.bakery_button.setGeometry(QRect(500, 185, 171, 41))

        type_buttonGroup = QButtonGroup(self)
        type_buttonGroup.setObjectName("type_buttonGroup")
        type_buttonGroup.addButton(self.drink_button)
        type_buttonGroup.addButton(self.bakery_button)

        price_label = QLabel("Price", self)
        price_label.setObjectName("default_label")
        price_label.setFont(Theme.DONGLE_BOLD_65)
        price_label.setGeometry(QRect(33, 301, 111, 41))

        self.hot_checkBox = QCheckBox("Hot", self)
        self.hot_checkBox.setObjectName("default_checkbox")
        self.hot_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_checkBox.setGeometry(QRect(194, 281, 141, 71))

        self.cold_checkBox = QCheckBox("Cold", self)
        self.cold_checkBox.setObjectName("default_checkbox")
        self.cold_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_checkBox.setGeometry(QRect(194, 370, 151, 61))

        self.blended_checkBox = QCheckBox("Blended", self)
        self.blended_checkBox.setObjectName("default_checkbox")
        self.blended_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_checkBox.setGeometry(QRect(194, 459, 211, 61))

        self.hot_price = QLineEdit(self)
        self.hot_price.setObjectName("input_bar")
        self.hot_price.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_price.setGeometry(QRect(480, 281, 200, 60))
        self.hot_price.setAlignment(Qt.AlignCenter)

        self.cold_price = QLineEdit(self)
        self.cold_price.setObjectName("input_bar")
        self.cold_price.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_price.setGeometry(QRect(480, 370, 200, 60))
        self.cold_price.setAlignment(Qt.AlignCenter)

        self.blended_price = QLineEdit(self)
        self.blended_price.setObjectName("input_bar")
        self.blended_price.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_price.setGeometry(QRect(480, 459, 200, 60))
        self.blended_price.setAlignment(Qt.AlignCenter)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setObjectName("cancel_add_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(124, 730, 200, 80))

        self.add_button = QPushButton("Add", self)
        self.add_button.setObjectName("cancel_add_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(394, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())


class MenuEdit(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)
        self.setObjectName("admin_widget")

        name_label = QLabel("Name", self)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name_bar = QLineEdit(self)
        self.name_bar.setObjectName("input_bar")
        self.name_bar.setFont(Theme.DONGLE_REGULAR_65)
        self.name_bar.setGeometry(QRect(210, 49, 470, 60))

        type_label = QLabel("Type", self)
        type_label.setObjectName("default_label")
        type_label.setFont(Theme.DONGLE_BOLD_65)
        type_label.setGeometry(QRect(33, 185, 111, 41))

        self.drink_button = QRadioButton("Drink", self)
        self.drink_button.setObjectName("default_radio")
        self.drink_button.setFont(Theme.DONGLE_REGULAR_65)
        self.drink_button.setGeometry(QRect(210, 185, 151, 41))

        self.bakery_button = QRadioButton("Bakery", self)
        self.bakery_button.setObjectName("default_radio")
        self.bakery_button.setFont(Theme.DONGLE_REGULAR_65)
        self.bakery_button.setGeometry(QRect(500, 185, 171, 41))

        type_buttonGroup = QButtonGroup(self)
        type_buttonGroup.setObjectName("type_buttonGroup")
        type_buttonGroup.addButton(self.drink_button)
        type_buttonGroup.addButton(self.bakery_button)

        price_label = QLabel("Price", self)
        price_label.setObjectName("default_label")
        price_label.setFont(Theme.DONGLE_BOLD_65)
        price_label.setGeometry(QRect(33, 301, 111, 41))

        self.hot_checkBox = QCheckBox("Hot", self)
        self.hot_checkBox.setObjectName("default_checkbox")
        self.hot_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_checkBox.setGeometry(QRect(194, 281, 141, 71))

        self.cold_checkBox = QCheckBox("Cold", self)
        self.cold_checkBox.setObjectName("default_checkbox")
        self.cold_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_checkBox.setGeometry(QRect(194, 370, 151, 61))

        self.blended_checkBox = QCheckBox("Blended", self)
        self.blended_checkBox.setObjectName("default_checkbox")
        self.blended_checkBox.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_checkBox.setGeometry(QRect(194, 459, 211, 61))

        self.hot_price = QLineEdit(self)
        self.hot_price.setObjectName("input_bar")
        self.hot_price.setFont(Theme.DONGLE_REGULAR_65)
        self.hot_price.setGeometry(QRect(480, 281, 200, 60))
        self.hot_price.setAlignment(Qt.AlignCenter)

        self.cold_price = QLineEdit(self)
        self.cold_price.setObjectName("input_bar")
        self.cold_price.setFont(Theme.DONGLE_REGULAR_65)
        self.cold_price.setGeometry(QRect(480, 370, 200, 60))
        self.cold_price.setAlignment(Qt.AlignCenter)

        self.blended_price = QLineEdit(self)
        self.blended_price.setObjectName("input_bar")
        self.blended_price.setFont(Theme.DONGLE_REGULAR_65)
        self.blended_price.setGeometry(QRect(480, 459, 200, 60))
        self.blended_price.setAlignment(Qt.AlignCenter)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setObjectName("cancel_add_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(33, 730, 200, 80))

        self.save_button = QPushButton("Save", self)
        self.save_button.setObjectName("cancel_add_button")
        self.save_button.setFont(Theme.DONGLE_REGULAR_65)
        self.save_button.setGeometry(QRect(257, 730, 200, 80))

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setObjectName("cancel_add_button")
        self.delete_button.setFont(Theme.DONGLE_REGULAR_65)
        self.delete_button.setGeometry(QRect(480, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())


class EmployeeAdminView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        admin_frame = QFrame(self)
        admin_frame.setObjectName("admin_frame")
        admin_frame.setGeometry(75, 115, 1000, 850)

        user_label = QLabel("User", admin_frame)
        user_label.setObjectName("menu_label")
        user_label.setFont(Theme.DONGLE_BOLD_80)
        user_label.setGeometry(QRect(55, 70, 130, 51))

        self.search_bar = QLineEdit(admin_frame)
        self.search_bar.setObjectName("search_bar")
        self.search_bar.setFont(Theme.DONGLE_BOLD_65)
        self.search_bar.setGeometry(QRect(260, 53, 680, 80))

        admin_scrollArea = QScrollArea(admin_frame)
        admin_scrollArea.setObjectName("admin_scrollArea")
        admin_scrollArea.setGeometry(QRect(55, 182, 890, 480))

        admin_scrollAreaContents = QWidget(admin_scrollArea)
        admin_scrollAreaContents.setObjectName("admin_scrollAreaContents")
        admin_scrollAreaContents.setGeometry(QRect(0, 0, 888, 478))
        admin_scrollArea.setWidget(admin_scrollAreaContents)

        add_button = QPushButton("+", self)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(915, 820, 100, 100))

        self.setStyleSheet(Theme.get_stylesheet())



class EmployeeEdit(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)
        self.setObjectName("admin_widget")

        name_label = QLabel("Name", self)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name = QLineEdit(self)
        self.name.setObjectName("input_bar")
        self.name.setFont(Theme.DONGLE_REGULAR_65)
        self.name.setGeometry(QRect(250, 50, 430, 60))

        surname_label = QLabel("Surname", self)
        surname_label.setObjectName("default_label")
        surname_label.setFont(Theme.DONGLE_BOLD_65)
        surname_label.setGeometry(QRect(33, 180, 171, 41))

        self.surname = QLineEdit(self)
        self.surname.setObjectName("input_bar")
        self.surname.setFont(Theme.DONGLE_REGULAR_65)
        self.surname.setGeometry(QRect(250, 155, 430, 60))

        username_label = QLabel("Username", self)
        username_label.setObjectName("default_label")
        username_label.setFont(Theme.DONGLE_BOLD_65)
        username_label.setGeometry(QRect(33, 390, 191, 41))

        self.username = QLineEdit(self)
        self.username.setObjectName("input_bar")
        self.username.setFont(Theme.DONGLE_REGULAR_65)
        self.username.setGeometry(QRect(250, 365, 430, 60))

        password_label = QLabel("Password", self)
        password_label.setObjectName("default_label")
        password_label.setFont(Theme.DONGLE_BOLD_65)
        password_label.setGeometry(QRect(33, 285, 201, 41))

        self.password = QLineEdit(self)
        self.password.setObjectName("input_bar")
        self.password.setFont(Theme.DONGLE_REGULAR_65)
        self.password.setGeometry(QRect(250, 260, 430, 60))

        position_label = QLabel("Position", self)
        position_label.setObjectName("default_label")
        position_label.setFont(Theme.DONGLE_BOLD_65)
        position_label.setGeometry(QRect(33, 495, 191, 41))

        self.admin_button = QRadioButton("Admin", self)
        self.admin_button.setObjectName("default_radio")
        self.admin_button.setFont(Theme.DONGLE_REGULAR_65)
        self.admin_button.setGeometry(QRect(250, 495, 161, 41))

        self.staff_button = QRadioButton("Staff", self)
        self.staff_button.setObjectName("default_radio")
        self.staff_button.setFont(Theme.DONGLE_REGULAR_65)
        self.staff_button.setGeometry(QRect(540, 495, 141, 41))

        position_buttonGroup = QButtonGroup(self)
        position_buttonGroup.setObjectName("position_buttonGroup")
        position_buttonGroup.addButton(self.admin_button)
        position_buttonGroup.addButton(self.staff_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setObjectName("cancel_add_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(33, 730, 200, 80))

        self.save_button = QPushButton("Save", self)
        self.save_button.setObjectName("cancel_add_button")
        self.save_button.setFont(Theme.DONGLE_REGULAR_65)
        self.save_button.setGeometry(QRect(257, 730, 200, 80))

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setObjectName("cancel_add_button")
        self.delete_button.setFont(Theme.DONGLE_REGULAR_65)
        self.delete_button.setGeometry(QRect(480, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())


class EmployeeAdd(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)
        self.setObjectName("admin_widget")

        name_label = QLabel("Name", self)
        name_label.setObjectName("default_label")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name = QLineEdit(self)
        self.name.setObjectName("input_bar")
        self.name.setFont(Theme.DONGLE_REGULAR_65)
        self.name.setGeometry(QRect(250, 50, 430, 60))

        surname_label = QLabel("Surname", self)
        surname_label.setObjectName("default_label")
        surname_label.setFont(Theme.DONGLE_BOLD_65)
        surname_label.setGeometry(QRect(33, 180, 171, 41))

        self.surname = QLineEdit(self)
        self.surname.setObjectName("input_bar")
        self.surname.setFont(Theme.DONGLE_REGULAR_65)
        self.surname.setGeometry(QRect(250, 155, 430, 60))

        username_label = QLabel("Username", self)
        username_label.setObjectName("default_label")
        username_label.setFont(Theme.DONGLE_BOLD_65)
        username_label.setGeometry(QRect(33, 390, 191, 41))

        self.username = QLineEdit(self)
        self.username.setObjectName("input_bar")
        self.username.setFont(Theme.DONGLE_REGULAR_65)
        self.username.setGeometry(QRect(250, 365, 430, 60))

        password_label = QLabel("Password", self)
        password_label.setObjectName("default_label")
        password_label.setFont(Theme.DONGLE_BOLD_65)
        password_label.setGeometry(QRect(33, 285, 201, 41))

        self.password = QLineEdit(self)
        self.password.setObjectName("input_bar")
        self.password.setFont(Theme.DONGLE_REGULAR_65)
        self.password.setGeometry(QRect(250, 260, 430, 60))

        position_label = QLabel("Position", self)
        position_label.setObjectName("default_label")
        position_label.setFont(Theme.DONGLE_BOLD_65)
        position_label.setGeometry(QRect(33, 495, 191, 41))

        self.admin_button = QRadioButton("Admin", self)
        self.admin_button.setObjectName("default_radio")
        self.admin_button.setFont(Theme.DONGLE_REGULAR_65)
        self.admin_button.setGeometry(QRect(250, 495, 161, 41))

        self.staff_button = QRadioButton("Staff", self)
        self.staff_button.setObjectName("default_radio")
        self.staff_button.setFont(Theme.DONGLE_REGULAR_65)
        self.staff_button.setGeometry(QRect(540, 495, 141, 41))

        position_buttonGroup = QButtonGroup(self)
        position_buttonGroup.setObjectName("position_buttonGroup")
        position_buttonGroup.addButton(self.admin_button)
        position_buttonGroup.addButton(self.staff_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setObjectName("cancel_add_button")
        self.cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        self.cancel_button.setGeometry(QRect(124, 730, 200, 80))

        self.add_button = QPushButton("Add", self)
        self.add_button.setObjectName("cancel_add_button")
        self.add_button.setFont(Theme.DONGLE_REGULAR_65)
        self.add_button.setGeometry(QRect(394, 730, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())


class AdminListItem(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(880, 80)
        self.setObjectName("admin_list_widget")

        self.name_button = QPushButton("Menu Name", self)
        self.name_button.setObjectName("list_button")
        self.name_button.setFont(Theme.DONGLE_REGULAR_65)
        self.name_button.setGeometry(QRect(50, 10, 780, 50))

        white_line = QFrame(self)
        white_line.setObjectName("brown_line")
        white_line.setGeometry(QRect(30, 70, 820, 3))

        self.setStyleSheet(Theme.get_stylesheet())