import sys
from PySide6.QtWidgets import *
from src.views import *
from src.controllers import *
from src.models import *


def test_widget() -> int:
    app = QApplication(sys.argv)
    w = MainView()  # change widget here
    w.showFullScreen()
    return app.exec()


if __name__ == "__main__":
    sys.exit(test_widget())
