import sys
from PySide6.QtWidgets import *
from views.view import *


def main() -> int:
    app = QApplication(sys.argv)
    w = BasePageView()  # change widget here
    w.showFullScreen()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())