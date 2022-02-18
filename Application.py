import sys
from PySide6.QtWidgets import (QApplication)
from views import menu_order


def main() -> int:
    app = QApplication(sys.argv)
    win = menu_order.Menu_order()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
