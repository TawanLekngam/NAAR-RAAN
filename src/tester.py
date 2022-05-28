import sys
from PySide6.QtWidgets import *
from views import *
from controllers import *
from models import *


def test_widget() -> int:
    app = QApplication(sys.argv)
    w = LoginView()  # change widget here
    w.showFullScreen()
    return app.exec()


if __name__ == "__main__":
    sys.exit(test_widget())
