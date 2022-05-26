"""
    contain all view and utility widget.
"""

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from.theme import Theme

class UserTab(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)


class OrderDetail(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1000, 850)

        menu_name = QLabel("Name Test", self)
        menu_name.setObjectName("menu_name")
        menu_name.setFont(Theme.DONGLE_BOLD_80)
        menu_name.setGeometry(QRect(93, 57, 830, 77))

        hot_button = QPushButton("Hot", self)
        hot_button.setObjectName("default_button")
        hot_button.setFont(Theme.DONGLE_REGULAR_65)
        hot_button.setGeometry(QRect(93, 134, 200, 60))
        hot_button.setCheckable(True)

        cold_button = QPushButton("Cold", self)
        cold_button.setObjectName("default_button")
        cold_button.setFont(Theme.DONGLE_REGULAR_65)
        cold_button.setGeometry(QRect(408, 134, 200, 60))
        cold_button.setCheckable(True)

        blended_button = QPushButton("Blended", self)
        blended_button.setObjectName("default_button")
        blended_button.setFont(Theme.DONGLE_REGULAR_65)
        blended_button.setGeometry(QRect(723, 134, 200, 60))
        blended_button.setCheckable(True)

        drinkType_buttonGroup = QButtonGroup(self)
        drinkType_buttonGroup.setObjectName("drinkType_ButtonGroup")
        drinkType_buttonGroup.addButton(hot_button)
        drinkType_buttonGroup.addButton(cold_button)
        drinkType_buttonGroup.addButton(blended_button)

        sweetness_label = QLabel("Sweetness", self)
        sweetness_label.setObjectName("sweetness_label")
        sweetness_label.setFont(Theme.DONGLE_REGULAR_65)
        sweetness_label.setGeometry(QRect(93, 241, 200, 103))

        sweet0_button = QPushButton("0", self)
        sweet0_button.setObjectName("default_button")
        sweet0_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet0_button.setGeometry(QRect(343, 258, 100, 60))
        sweet0_button.setCheckable(True)

        sweet25_button = QPushButton("25", self)
        sweet25_button.setObjectName("default_button")
        sweet25_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet25_button.setGeometry(QRect(503, 258, 100, 60))
        sweet25_button.setCheckable(True)

        sweet50_button = QPushButton("50", self)
        sweet50_button.setObjectName("default_button")
        sweet50_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet50_button.setGeometry(QRect(663, 258, 100, 60))
        sweet50_button.setCheckable(True)

        sweet100_button = QPushButton("100", self)
        sweet100_button.setObjectName("default_button")
        sweet100_button.setFont(Theme.DONGLE_REGULAR_65)
        sweet100_button.setGeometry(QRect(823, 258, 100, 60))
        sweet100_button.setCheckable(True)

        sweetness_buttonGroup = QButtonGroup(self)
        sweetness_buttonGroup.setObjectName("sweetness_buttonGroup")
        sweetness_buttonGroup.addButton(sweet0_button)
        sweetness_buttonGroup.addButton(sweet25_button)
        sweetness_buttonGroup.addButton(sweet50_button)
        sweetness_buttonGroup.addButton(sweet100_button)

        cancel_button = QPushButton("Cancel", self)
        cancel_button.setObjectName("cancel_add_button")
        cancel_button.setFont(Theme.DONGLE_REGULAR_65)
        cancel_button.setGeometry(QRect(270, 726, 200, 80))

        add_button = QPushButton("Add", self)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(Theme.DONGLE_REGULAR_65)
        add_button.setGeometry(QRect(551, 726, 200, 80))

        self.setStyleSheet(Theme.get_stylesheet())


"""
    application view.
"""


class BaseView(QWidget):
    """
    run another widget on stackwidget.
    """
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        self.resize(1920, 1080)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 1920, 94))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.pushButton = QPushButton("Tawan L.",self.frame)
        self.pushButton.setObjectName("pushButton_base_page")
        self.pushButton.setGeometry(QRect(1421, 5, 500, 94))
        self.pushButton.setFont(Theme.DONGLE_BOLD_65)

        self.pushButton_home = QPushButton(self.frame)
        self.pushButton_home.setObjectName("pushButton_base_page")
        self.pushButton_home.setGeometry(QRect(1321, 5, 100, 94))
        icon_home = QIcon()
        icon_home.addFile("src/data/asset/Image/home.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_home.setIcon(icon_home)
        self.pushButton_home.setIconSize(QSize(55,55))
        
        self.pushButton_home.setIcon(QIcon("src/data/asset/Image/home.png"))

        self.pushButton_target = QPushButton(self.frame)
        self.pushButton_target.setObjectName("pushButton_base_page")
        self.pushButton_target.setGeometry(QRect(1221, 5, 100, 94))
        icon_target = QIcon()
        icon_target.addFile("src/data/asset/Image/target.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_target.setIcon(icon_target)
        self.pushButton_target.setIconSize(QSize(55,55))

        self.pushButton_auditlog = QPushButton(self.frame)
        self.pushButton_auditlog.setObjectName("pushButton_base_page")
        self.pushButton_auditlog.setGeometry(QRect(1121, 5, 100, 94))
        icon_auditlog = QIcon()
        icon_auditlog.addFile("src/data/asset/Image/history.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_auditlog.setIcon(icon_auditlog)
        self.pushButton_auditlog.setIconSize(QSize(55,55))

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 84, 1920, 1071))

        self.target_revenue_page = AuditLogView()
        self.target_revenue_page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.target_revenue_page)

        self.setStyleSheet(Theme.get_stylesheet())

    def add_view(self, view: QWidget) -> None:
        self.stackedWidget.addWidget(view)


class LoginView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        label_logo = QLabel(self)
        label_logo.setObjectName("label_logo")
        label_logo.setGeometry(QRect(846, 158, 252, 252))
        label_logo.setPixmap(QPixmap("src/data/asset/Image/logo.png"))

        label_username = QLabel("Username", self)
        label_username.setObjectName("label_username")
        label_username.setFont(Theme.DONGLE_BOLD_65)
        label_username.setGeometry(QRect(523, 587, 321, 72))

        label_password = QLabel("Password", self)
        label_password.setObjectName("label_password")
        label_password.setFont(Theme.DONGLE_BOLD_65)
        label_password.setGeometry(QRect(523, 726, 291, 72))

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_username.setFont(Theme.DONGLE_BOLD_65)
        self.lineEdit_username.setGeometry(QRect(980, 570, 600, 80))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setFont(Theme.DONGLE_REGULAR_50)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setGeometry(QRect(980, 715, 600, 80))

        self.login_button = QPushButton(self)
        self.login_button.setObjectName("pushButton")
        self.login_button.setGeometry(QRect(860, 860, 200, 80))

        icon = QIcon()
        icon.addFile("src/data/asset/Image/coffee.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(55, 55))
        self.setStyleSheet(Theme.get_stylesheet())

    def login_button_emit(self, function) -> None:
        self.login_button.clicked.connect(function)


class MenuOrderView(QWidget):
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
        line.setObjectName("line")
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
        self.order_button.setObjectName("order_button")
        self.order_button.setFont(Theme.DONGLE_BOLD_65)
        self.order_button.setGeometry(QRect(1145, 885, 700, 80))

        self.setStyleSheet(Theme.get_stylesheet())


class TargetRevenueView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        self.resize(1920, 1080)

        self.widget_date = QWidget(self)
        self.widget_date.setObjectName("widget_date")
        self.widget_date.setGeometry(QRect(80, 65, 625, 900))

        self.listWidget_date = QListWidget(self.widget_date)
        self.listWidget_date.setObjectName("listWidget_date")
        self.listWidget_date.setGeometry(QRect(13, 130, 600, 750))

        self.label_month = QLabel("Month", self.widget_date)
        self.label_month.setObjectName("label_date_target")
        self.label_month.setGeometry(QRect(60, 40, 171, 61))
        self.label_month.setFont(Theme.DONGLE_BOLD_65)

        self.label_revenue = QLabel("Revenue", self.widget_date)
        self.label_revenue.setObjectName("label_date_target")
        self.label_revenue.setGeometry(QRect(390, 40, 211, 61))
        self.label_revenue.setFont(Theme.DONGLE_BOLD_65)

        self.widget_report = QWidget(self)
        self.widget_report.setObjectName("widget_report")
        self.widget_report.setGeometry(QRect(840, 100, 1000, 720))

        self.label_target = QLabel("Target", self.widget_report)
        self.label_target.setObjectName("label_target")
        self.label_target.setGeometry(QRect(200, 470, 171, 61))
        self.label_target.setFont(Theme.DONGLE_BOLD_65)

        self.label_revenue_pie = QLabel("Revenue", self.widget_report)
        self.label_revenue_pie.setObjectName("label_target")
        self.label_revenue_pie.setGeometry(QRect(200, 565, 221, 51))
        self.label_revenue_pie.setFont(Theme.DONGLE_BOLD_65)

        self.label_amount_left = QLabel("Amount Left", self.widget_report)
        self.label_amount_left.setObjectName("label_target")
        self.label_amount_left.setGeometry(QRect(200, 650, 341, 61))
        self.label_amount_left.setFont(Theme.DONGLE_BOLD_65)

        self.label_money_target = QLabel("9000", self.widget_report)
        self.label_money_target.setObjectName("label_target")
        self.label_money_target.setGeometry(QRect(670, 470, 131, 61))
        self.label_money_target.setFont(Theme.DONGLE_REGULAR_65)

        self.label_money_revenue = QLabel("5000", self.widget_report)
        self.label_money_revenue.setObjectName("label_target")
        self.label_money_revenue.setGeometry(QRect(670, 565, 131, 51))
        self.label_money_revenue.setFont(Theme.DONGLE_REGULAR_65)

        self.label_money_left = QLabel("4000", self.widget_report)
        self.label_money_left.setObjectName("label_target")
        self.label_money_left.setGeometry(QRect(670, 650, 131, 51))
        self.label_money_left.setFont(Theme.DONGLE_REGULAR_65)

        self.pushButton_edit = QPushButton("Edit", self)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(1620, 870, 220, 80))
        self.pushButton_edit.setFont(Theme.DONGLE_BOLD_65)

        self.setStyleSheet(Theme.get_stylesheet())


class AuditLogView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.resize(1920, 1080)
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
        name_label.setObjectName("menu_name")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name_bar = QLineEdit(self)
        self.name_bar.setObjectName("input_bar")
        self.name_bar.setFont(Theme.DONGLE_REGULAR_65)
        self.name_bar.setGeometry(QRect(210, 49, 470, 60))

        type_label = QLabel("Type", self)
        type_label.setObjectName("menu_name")
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
        price_label.setObjectName("menu_name")
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
        name_label.setObjectName("menu_name")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name_bar = QLineEdit(self)
        self.name_bar.setObjectName("input_bar")
        self.name_bar.setFont(Theme.DONGLE_REGULAR_65)
        self.name_bar.setGeometry(QRect(210, 49, 470, 60))

        type_label = QLabel("Type", self)
        type_label.setObjectName("menu_name")
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
        price_label.setObjectName("menu_name")
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

class EmployeeEdit(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(720, 850)
        self.setObjectName("admin_widget")

        name_label = QLabel("Name", self)
        name_label.setObjectName("menu_name")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name = QLineEdit(self)
        self.name.setObjectName("input_bar")
        self.name.setFont(Theme.DONGLE_REGULAR_65)
        self.name.setGeometry(QRect(250, 50, 430, 60))

        surname_label = QLabel("Surname", self)
        surname_label.setObjectName("menu_name")
        surname_label.setFont(Theme.DONGLE_BOLD_65)
        surname_label.setGeometry(QRect(33, 180, 171, 41))

        self.surname = QLineEdit(self)
        self.surname.setObjectName("input_bar")
        self.surname.setFont(Theme.DONGLE_REGULAR_65)
        self.surname.setGeometry(QRect(250, 155, 430, 60))

        username_label = QLabel("Username", self)
        username_label.setObjectName("menu_name")
        username_label.setFont(Theme.DONGLE_BOLD_65)
        username_label.setGeometry(QRect(33, 390, 191, 41))

        self.username = QLineEdit(self)
        self.username.setObjectName("input_bar")
        self.username.setFont(Theme.DONGLE_REGULAR_65)
        self.username.setGeometry(QRect(250, 365, 430, 60))

        password_label = QLabel("Password", self)
        password_label.setObjectName("menu_name")
        password_label.setFont(Theme.DONGLE_BOLD_65)
        password_label.setGeometry(QRect(33, 285, 201, 41))

        self.password = QLineEdit(self)
        self.password.setObjectName("input_bar")
        self.password.setFont(Theme.DONGLE_REGULAR_65)
        self.password.setGeometry(QRect(250, 260, 430, 60))

        position_label = QLabel("Position", self)
        position_label.setObjectName("menu_name")
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
        name_label.setObjectName("menu_name")
        name_label.setFont(Theme.DONGLE_BOLD_65)
        name_label.setGeometry(QRect(33, 75, 111, 41))

        self.name = QLineEdit(self)
        self.name.setObjectName("input_bar")
        self.name.setFont(Theme.DONGLE_REGULAR_65)
        self.name.setGeometry(QRect(250, 50, 430, 60))

        surname_label = QLabel("Surname", self)
        surname_label.setObjectName("menu_name")
        surname_label.setFont(Theme.DONGLE_BOLD_65)
        surname_label.setGeometry(QRect(33, 180, 171, 41))

        self.surname = QLineEdit(self)
        self.surname.setObjectName("input_bar")
        self.surname.setFont(Theme.DONGLE_REGULAR_65)
        self.surname.setGeometry(QRect(250, 155, 430, 60))

        username_label = QLabel("Username", self)
        username_label.setObjectName("menu_name")
        username_label.setFont(Theme.DONGLE_BOLD_65)
        username_label.setGeometry(QRect(33, 390, 191, 41))

        self.username = QLineEdit(self)
        self.username.setObjectName("input_bar")
        self.username.setFont(Theme.DONGLE_REGULAR_65)
        self.username.setGeometry(QRect(250, 365, 430, 60))

        password_label = QLabel("Password", self)
        password_label.setObjectName("menu_name")
        password_label.setFont(Theme.DONGLE_BOLD_65)
        password_label.setGeometry(QRect(33, 285, 201, 41))

        self.password = QLineEdit(self)
        self.password.setObjectName("input_bar")
        self.password.setFont(Theme.DONGLE_REGULAR_65)
        self.password.setGeometry(QRect(250, 260, 430, 60))

        position_label = QLabel("Position", self)
        position_label.setObjectName("menu_name")
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

