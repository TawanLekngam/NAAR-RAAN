import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from views.utility_widget import Widget


class Order_details(Widget):
    def __init__(self, parent: QWidget = None):
        Widget.__init__(self, parent)
        self.setFixedSize(1000, 850)

        menu_name = QLabel("Name Test", self)
        menu_name.setObjectName("menu_name")
        menu_name.setFont(self._get_font(80))
        menu_name.setGeometry(QRect(93, 57, 830, 77))

        hot_button = QPushButton("Hot", self)
        hot_button.setObjectName("default_button")
        hot_button.setFont(self._get_font(65))
        hot_button.setGeometry(QRect(93, 134, 200, 60))
        hot_button.setCheckable(True)

        cold_button = QPushButton("Cold", self)
        cold_button.setObjectName("default_button")
        cold_button.setFont(self._get_font(65))
        cold_button.setGeometry(QRect(408, 134, 200, 60))
        cold_button.setCheckable(True)

        blended_button = QPushButton("Blended", self)
        blended_button.setObjectName("default_button")
        blended_button.setFont(self._get_font(65))
        blended_button.setGeometry(QRect(723, 134, 200, 60))
        blended_button.setCheckable(True)

        drinkType_buttonGroup = QButtonGroup(self)
        drinkType_buttonGroup.setObjectName("drinkType_ButtonGroup")
        drinkType_buttonGroup.addButton(hot_button)
        drinkType_buttonGroup.addButton(cold_button)
        drinkType_buttonGroup.addButton(blended_button)

        sweetness_label = QLabel("Sweetness", self)
        sweetness_label.setObjectName("sweetness_label")
        sweetness_label.setFont(self._get_font(65))
        sweetness_label.setGeometry(QRect(93, 241, 200, 103))

        sweet0_button = QPushButton("0", self)
        sweet0_button.setObjectName("default_button")
        sweet0_button.setFont(self._get_font(65))
        sweet0_button.setGeometry(QRect(343, 258, 100, 60))
        sweet0_button.setCheckable(True)

        sweet25_button = QPushButton("25", self)
        sweet25_button.setObjectName("default_button")
        sweet25_button.setFont(self._get_font(65))
        sweet25_button.setGeometry(QRect(503, 258, 100, 60))
        sweet25_button.setCheckable(True)

        sweet50_button = QPushButton("50", self)
        sweet50_button.setObjectName("default_button")
        sweet50_button.setFont(self._get_font(65))
        sweet50_button.setGeometry(QRect(663, 258, 100, 60))
        sweet50_button.setCheckable(True)

        sweet100_button = QPushButton("100", self)
        sweet100_button.setObjectName("default_button")
        sweet100_button.setFont(self._get_font(65))
        sweet100_button.setGeometry(QRect(823, 258, 100, 60))
        sweet100_button.setCheckable(True)

        sweetness_buttonGroup = QButtonGroup(self)
        sweetness_buttonGroup.setObjectName("sweetness_buttonGroup")
        sweetness_buttonGroup.addButton(sweet0_button)
        sweetness_buttonGroup.addButton(sweet25_button)
        sweetness_buttonGroup.addButton(sweet50_button)
        sweetness_buttonGroup.addButton(sweet100_button)

        addOn_label = QLabel("Add-On", self)
        addOn_label.setObjectName("addOn_label")
        addOn_label.setFont(self._get_font(65))
        addOn_label.setGeometry(QRect(93, 344, 147, 57))

        topping1_button = QPushButton("Topping1", self)
        topping1_button.setObjectName("default_button")
        topping1_button.setFont(self._get_font(65))
        topping1_button.setGeometry(QRect(93, 439, 200, 60))
        topping1_button.setCheckable(True)

        topping2_button = QPushButton("Topping2", self)
        topping2_button.setObjectName("default_button")
        topping2_button.setFont(self._get_font(65))
        topping2_button.setGeometry(QRect(304, 439, 200, 60))
        topping2_button.setCheckable(True)

        topping3_button = QPushButton("Topping3", self)
        topping3_button.setObjectName("default_button")
        topping3_button.setFont(self._get_font(65))
        topping3_button.setGeometry(QRect(514, 439, 200, 60))
        topping3_button.setCheckable(True)

        topping4_button = QPushButton("Topping4", self)
        topping4_button.setObjectName("default_button")
        topping4_button.setFont(self._get_font(65))
        topping4_button.setGeometry(QRect(723, 439, 200, 60))
        topping4_button.setCheckable(True)

        topping5_button = QPushButton("Topping5", self)
        topping5_button.setObjectName("default_button")
        topping5_button.setFont(self._get_font(65))
        topping5_button.setGeometry(QRect(93, 536, 200, 60))
        topping5_button.setCheckable(True)

        topping6_button = QPushButton("Topping6", self)
        topping6_button.setObjectName("default_button")
        topping6_button.setFont(self._get_font(65))
        topping6_button.setGeometry(QRect(304, 536, 200, 60))
        topping6_button.setCheckable(True)

        topping7_button = QPushButton("Topping7", self)
        topping7_button.setObjectName("default_button")
        topping7_button.setFont(self._get_font(65))
        topping7_button.setGeometry(QRect(514, 536, 200, 60))
        topping7_button.setCheckable(True)

        topping8_button = QPushButton("Topping8", self)
        topping8_button.setObjectName("default_button")
        topping8_button.setFont(self._get_font(65))
        topping8_button.setGeometry(QRect(723, 536, 200, 60))
        topping8_button.setCheckable(True)

        cancel_button = QPushButton("Cancel", self)
        cancel_button.setObjectName("cancel_add_button")
        cancel_button.setFont(self._get_font(65))
        cancel_button.setGeometry(QRect(270, 726, 200, 80))

        add_button = QPushButton("Add", self)
        add_button.setObjectName("cancel_add_button")
        add_button.setFont(self._get_font(65))
        add_button.setGeometry(QRect(551, 726, 200, 80))

        self._set_stylesheet("order_details.qss")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    od = Order_details()

    sys.exit(app.exec())
