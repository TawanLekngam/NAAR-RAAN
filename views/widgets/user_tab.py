from PySide6.QtWidgets import (QWidget, QFrame, QVBoxLayout, QPushButton)
from PySide6.QtCore import (QRect)
from PySide6.QtGui import (QMouseEvent)


class UserTab(QWidget):
    __extend: bool
    __area: QRect

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)
        button_layout = QVBoxLayout(self)

        self.setStyleSheet(u"background-color: #4A321C")

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if self.childrenRect().contains(e.pos().x(), e.pos().y()):
            print("Passed")
