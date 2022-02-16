from PySide6.QtWidgets import QWidget


class BasePage(QWidget):
    def __init__(self, parent: QWidget):
        QWidget.__init__(self, parent)
        self.set_stylesheet()

    def set_stylesheet(self):
        file_name = type(self).__name__.lower() + ".qss"
        theme_dir_name = "themes"
        with open(theme_dir_name + '/' + file_name, "r") as file:
            style = file.read()
            self.setStyleSheet(style)
        file.close()
        # Check Log
        print(f"Log: Load {file_name} to {type(self).__name__}")