from abc import ABC
from data import *


__APP_DAO = AppDAO()


class Model(ABC):
    pass


class MenuModel(Model):

    def __init__(self):
        print("Log: Load" + type(self).__name__)

    def get_all_drinks() -> list[Drink]:
        return __APP_DAO.get_all_drinks()
