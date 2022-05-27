from abc import ABC
from datetime import date
from dateutil import relativedelta

from data.orm.schema import *
from data.orm.data_access_object import *


class Model(ABC):
    pass


class LoginModel(Model):

    def __init__(self):
        self.user_dao: UserDAO = AppDAO.get_dao("user")
        self.__current_user: User = None
        self.__current_username = str()
        self.__current_password = str()
        self.valid_login = False

    def get_input(self, username: str, password: str) -> None:
        self.__current_username = username
        self.__current_password = password

    def retrive_user(self, username: str) -> None:
        self.__current_user = self.user_dao.get_user_by_username(username)

    def verify_login(self) -> None:
        if self.__current_user is None:
            self.valid_login = False
            return

        self.valid_login = (self.__current_username == self.__current_user.get_username()
                            and self.__current_password == self.__current_user.get_password())

    def is_valid(self) -> bool:
        return self.valid_login

    def set_current_user(self, username: str) -> None:
        self.__current_user = self.user_dao.get_user_by_username(username)

    def get_current_user(self) -> User:
        return self.__current_user