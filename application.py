import sys
from PySide6.QtWidgets import (QApplication)
from controllers import *
from views.utility_widget import OrderDetails


def main() -> int:
    app = QApplication(sys.argv)
    # win = LogInController()       # For test LogIn Page
    # win = MenuOrderController()     # For test Menu Order Page

    od = OrderDetails(None)

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
