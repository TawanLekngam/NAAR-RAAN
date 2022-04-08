"""
    
"""

import sys
from PySide6.QtWidgets import (QApplication)

from controllers.controller import (Controller, LogInPage, MenuOrderPage, OrderTrackingPage)
from views.view import (LoginView, MenuOrderView, OrderTrackingView)
from models.model import (LoginModel, MenuOrderModel, OrderTrackingModel)
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
        self.__order_tracking = OrderTrackingPage(
            OrderTrackingView(),
            OrderTrackingModel()
        )


        self.__current_page = self.__order_tracking

    def start(self) -> None:
        self.__current_page.show_page()
        sys.exit(self.app.exec_())

    def update(self) -> None:
        self.__current_page.update()



if __name__ == "__main__":
    app = Application()
    app.start()
