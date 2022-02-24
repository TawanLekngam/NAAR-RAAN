from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton)
from PySide6.QtGui import (QFont, QMouseEvent)


class Widget(QWidget): #Base Widget for dymamic widget

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)

    def _get_font(self, size: int) -> QFont:
        font = QFont()
        font.setPixelSize(size)
        return font


class UserTab(Widget):

    def __init__(self, parent: QWidget):
        Widget.__init__(self, parent)
        layout = QVBoxLayout()
        btn = QPushButton("click me", self)
        layout.addWidget(btn)
        self.setLayout(layout)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.underMouse():
            print("Log: On me.")


class MenuItem(Widget):

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)
