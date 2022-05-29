import sys
from PySide6.QtWidgets import QApplication

from application import Application


def main() -> int:
    root = QApplication(sys.argv)
    app = Application()
    app.start()
    return root.exec()


if __name__ == "__main__":
    sys.exit(main())
