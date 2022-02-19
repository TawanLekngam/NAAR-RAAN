import sys
from PySide6.QtWidgets import (QApplication)
from controllers.controller import MenuOrderController


def main() -> int:
    app = QApplication(sys.argv)
    win = MenuOrderController()
    win.show_page()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
