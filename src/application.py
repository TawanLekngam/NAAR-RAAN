from PySide6.QtWidgets import QStackedWidget

from models import *
from views import *
from controllers import *


class Application(QStackedWidget):

    def __init__(self):
        QStackedWidget.__init__(self, None)
        self.setFixedSize(1920, 1080)
        self.setWindowTitle("Naar Raan")

        self.current_user = None

        # Login Page
        self.login_page = LoginPage(self, LoginView(), LoginModel())


        # main page
        # home Page
        self.home_page = None

        # sub page
        # Staff Page Application
        self.menu_order_page = None

        # Admin Page Application
        self.menu_edit_page = None
        self.user_edit_page = None
        self.audit_log_page = None
        self.revenue_page = None


        # start page
        self.addWidget(self.login_page.view)

    def initialize_page(self) -> None:
        "set up method for user."
        if self.current_user is None:
            return

        self.home_page = HomePage(HomeView(), HomeModel(self.current_user),self.current_user)

    def set_current_user(self, user: User) -> None:
        self.current_user = user

    def start(self) -> None:
        "driver method."
        self.showFullScreen()
