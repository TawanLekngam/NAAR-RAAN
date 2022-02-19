import sys
from PySide6.QtWidgets import (QApplication)
from controllers import *


def main() -> int:
    app = QApplication(sys.argv)
    # win = LogInController()       # For test LogIn Page
    win = MenuOrderController()     # For test Menu Order Page
    win.show_page()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
