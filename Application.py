import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import data


def main() -> int:
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.showFullScreen()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
