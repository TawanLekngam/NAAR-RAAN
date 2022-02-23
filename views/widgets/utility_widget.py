from PySide6.QtWidgets import (QWidget)
from PySide6.QtGui import (QFont)


class Widget(QWidget):

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)

    def _get_font(self,size: int) -> QFont:
        font = QFont()
        font.setPixelSize(size)
        return font
