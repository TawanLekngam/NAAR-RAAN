import sys
from PySide6.QtWidgets import (QApplication)

from controllers import *

if __name__ == "__main__":
    # data_access = AppDAO.get_dao("logentry")
    # print(type(data_access).__name__)

    app = QApplication(sys.argv)
    w = LogInController()
    sys.exit(app.exec_())