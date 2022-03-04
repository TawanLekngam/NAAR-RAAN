from abc import ABC
from data import AppDAO, Drink


__APP_DAO = AppDAO()


class Model(ABC):
    pass


class MenuModel(Model):
    def get_all_drinks() -> list[Drink]:
        return __APP_DAO.get_all_drinks()
