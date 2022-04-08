"""
    contain all model.
"""
from abc import ABC
from data import *
from data.app_dao import *


class Model(ABC):
    pass


class LoginModel(Model):
    def __init__(self):
        self.__userDAO: UserDAO = AppDAO.get_dao("user")

    def login_verify(self, username: str, password: str) -> bool:
        db_user = self.__userDAO.get_user_by_username(username)

        if password == db_user.get_password():
            return True

        return False


class MenuOrderModel(Model):
    def __init__(self) -> None:
        self.__productDAO: ProductDAO = AppDAO.get_dao("drink")


class RevenueModel(Model):
    def __init__(self):
        pass

class OrderTrackingModel(Model):
    def __init__(self):
        pass

class TargetRevenueModel(Model):
    def __init__(self):
        pass