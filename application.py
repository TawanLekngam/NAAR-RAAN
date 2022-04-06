"""
    
"""

import sys
from PySide6.QtWidgets import (QApplication)

from controllers.controller import (Controller, LogInPage, MenuOrderPage)
from views.view import (LoginView, MenuOrderView)
from models.model import (LoginModel, MenuOrderModel)
from data.data_classes import (User)


class Application:
    __current_user: User
    __current_page: Controller

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.__current_user = None

        self.__login_page = LogInPage(
            LoginView(),
            LoginModel())

        self.__menuorder_page = MenuOrderPage(
            MenuOrderView(),
            MenuOrderModel())


        self.__current_page = self.__login_page

    def start(self) -> None:
        self.__current_page.show_page()
        sys.exit(self.app.exec_())

    def update(self) -> None:
        self.__current_page.update()



if __name__ == "__main__":
    app = Application()
    app.start()
