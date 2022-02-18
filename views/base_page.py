import os
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont



class BasePage(QWidget):

    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __THEME_PATH = os.path.join(__ROOT_DIR, "themes")

    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)
        self.setFixedSize(1920, 1080)

        self._set_stylesheet()

    def _get_font(self, size: int) -> QFont():
        font = QFont()
        font.setPixelSize(size)
        return font

    def _set_stylesheet(self):
        file_name = type(self).__name__.lower() + ".qss"
        real_path = os.path.join(BasePage.__THEME_PATH, file_name)
        with open(real_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)
        file.close()
        # Check Log
        print(f"Log: Load {file_name} to {type(self).__name__}")
