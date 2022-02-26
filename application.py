import sys
from PySide6.QtWidgets import (QApplication)
from controllers import *
from views.order_details import Order_details


def main() -> int:
    app = QApplication(sys.argv)
    # win = LogInController()       # For test LogIn Page
    # win = MenuOrderController()     # For test Menu Order Page

    od = Order_details()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
