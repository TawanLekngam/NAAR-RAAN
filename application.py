"""
    
"""

import sys
from PySide6.QtWidgets import (QApplication)

from controllers.controller import (AuditLogPage, Controller, LogInPage, MenuOrderPage, OrderTrackingPage, TargetRevenuePage)
from views.view import (AuditLogView, LoginView, MenuOrderView, OrderTrackingView, TargetRevenueView)
from models.model import (AuditLogModel, LoginModel, MenuOrderModel, OrderTrackingModel, TargetRevenueModel)
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
        self.__target_revenue = TargetRevenuePage(
            TargetRevenueView(),
            TargetRevenueModel()
        )

        self.__audit_log = AuditLogPage(
            AuditLogView(),
            AuditLogModel()
        )


        self.__current_page = self.__audit_log

    def start(self) -> None:
        self.__current_page.show_page()
        sys.exit(self.app.exec_())

    def update(self) -> None:
        self.__current_page.update()



if __name__ == "__main__":
    app = Application()
    app.start()
