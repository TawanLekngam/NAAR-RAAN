from PySide6.QtWidgets import (QWidget, QFrame, QVBoxLayout, QPushButton)
from PySide6.QtCore import (QRect)
from PySide6.QtGui import (QMouseEvent)


class UserTab(QWidget):
    __extend: bool
    __area: QRect

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)
        button_layout = QVBoxLayout()
        self.extend_frame = QFrame(self)
        self.extend_frame.setLayout(button_layout)

        self.setStyleSheet(u"background-color: #4A321C")


    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        self.__area = QRect(self.x, self.y, self.width, self.height)

        if self.__area.contains(e.pos().x(),e.pos().y()):
            print("Passed")


    
