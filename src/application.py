from PySide6.QtWidgets import QStackedWidget


class Application(QStackedWidget):

    def __init__(self):
        QStackedWidget().__init__(self, None)
        self.setFixedSize(1920, 1080)
        self.setWindowTitle("Naar Raan")

        self.current_user = None


        # Login Page
        self.login_page = None