import sys
from PySide6.QtWidgets import *
from views.view import *


def main() -> int:
    app = QApplication(sys.argv)
    w = OrderDetail()   # change widget here
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())