from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QMouseEvent


class UserTab(QWidget):
    __extend: bool
    __area: QRect

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)
        self.__extend = False
        self.__area = QRect(self.x, self.y, self.width, self.height)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        pass
