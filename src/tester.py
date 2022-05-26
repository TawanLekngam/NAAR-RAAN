import sys
from PySide6.QtWidgets import *
from views import *
from controllers import *
from models import *


def test_widget() -> int:
    app = QApplication(sys.argv)
    w = MainView()  # change widget here
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(test_widget())
