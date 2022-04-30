import sys
from PySide6.QtWidgets import *
from src.view import *
from src.controller import *


def test_widget() -> int:
    app = QApplication(sys.argv)
    w = BaseView()  # change widget here
    w.showFullScreen()
    return app.exec()

def test_controller() -> int:
    app = QApplication(sys.argv)
    c = LIC()

if __name__ == "__main__":
    sys.exit(test_widget())