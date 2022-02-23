from PySide6.QtWidgets import (QWidget)
from PySide6.QtGui import (QFont)


class Widget(QWidget()):

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, QWidget)

    def _get_font(size: font) -> QFont:
        font = QFont()
        font.setPixelSize(size)
        return font
