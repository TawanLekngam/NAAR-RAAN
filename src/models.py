from abc import ABC
from datetime import date
from dateutil import relativedelta
from shiboken6 import delete

from data.orm.schema import *
from data.orm.data_access_object import *


class Model(ABC):
    pass


class AccountModel(Model):
    LENGHT_LIMIT = 4
    __current_user: User
    __user_dao: UserDAO
    __log_dao: LogDAO

    def __init__(self, user: User = None):
        self.__current_user = user
        self.__user_dao = AppDAO.get_dao("user")
        self.__log_dao = AppDAO.get_dao("log")

    def get_all_account(self) -> list[User]:
        return self.__user_dao.get_all_users()

    def create_new_account(self, user: User) -> None:
        self.__user_dao.add_user(user)

        log = Log(
            f"ADMIN: {self.__current_user.get_username()} created new account for {user.get_username()}.")
        self.__log_dao.add_log(log)

    def generate_username(self, fname: str, lname: str) -> str:
        username = str()

        if len(fname) <= AccountModel.LENGHT_LIMIT:
            username += fname.lower()
        else:
            username += fname[0:AccountModel.LENGHT_LIMIT].lower()

        username += "."

        if len(lname) <= AccountModel.LENGHT_LIMIT:
            username += lname.lower()
        else:
            username += lname[0:AccountModel.LENGHT_LIMIT].lower()

        return username


class HomeModel(Model):

    def __init__(self):
        pass

    def logout(self) -> None:
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


class LogModel(Model):
    __log_dao: LogDAO

    def __init__(self):
        self.__log_dao = AppDAO.get_dao("log")

    def get_all_logs(self) -> list[Log]:
        return self.__log_dao.get_all_logs()


class MenuModel(Model):
    __drink_dao: DrinkDAO
    __bakery_dao: BakeryDAO

    def __init__(self):
        self.__drink_dao = AppDAO.get_dao("drink")
        self.__bakery_dao = AppDAO.get_dao("bakery")

    def get_all_products(self) -> list[Drink | Bakery]:
        products = list()
        products.extend(self.__drink_dao.get_all_drinks())
        products.extend(self.__bakery_dao.get_all_bakeries())
        products.sort(key=lambda x: x.name)
        return products

    def update_drink(self, id: int, name: str = None, hprice: float = None, cprice: float = None, bprice: float = None) -> None:
        self.__drink_dao.update_drink(id, name, hprice, cprice, bprice)

    def update_bakery(self, id: int, name: str = None, price: float = None) -> None:
        self.__bakery_dao.update_bakery(id, name, price)


class OrderModel(Model):
    __receipt_dao: ReceiptDAO

    def __init__(self):
        self.__receipt_dao = AppDAO.get_dao("receipt")

    def create_new_receipt(self, receipt: Receipt) -> None:
        self.__receipt_dao.add_receipt(receipt)


class OrderListModel(Model):
    __drink_dao: DrinkDAO
    __bakery_dao: BakeryDAO

    def __init__(self):
        self.__drink_dao = AppDAO.get_dao("drink")
        self.__bakery_dao = AppDAO.get_dao("bakery")

    def get_all_products(self) -> list:
        products = list()
        products.extend(self.__drink_dao.get_all_drinks())
        products.extend(self.__bakery_dao.get_all_bakeries())
        products.sort(key=lambda x: x.name)
        return products


class ReceiptModel(Model):
    __receipt_dao: ReceiptDAO

    def __init__(self):
        self.__receipt_dao = AppDAO.get_dao("receipt")

    def get_all_receipt(self) -> list[Receipt]:
        return self.__receipt_dao.get_all_receipts()


class MenuEditModel(Model):
    __drink_dao: DrinkDAO
    __bakery_dao: BakeryDAO
    __log_dao: LogDAO

    def __init__(self):
        self.__drink_dao = AppDAO.get_dao("drink")
        self.__bakery_dao = AppDAO.get_dao("bakery")
        self.__log_dao = AppDAO.get_dao("log")

    def add(self, item: Drink | Bakery) -> None:
        if isinstance(item, Drink):
            self.__drink_dao.add_drink(item)
        else:
            self.__bakery_dao.add_bakery(item)
            
        self.__log_dao.add_log(Log(f"Add {item.get_name()} to system."))

    def delete(self, item: Drink | Bakery) -> None:
        if isinstance(item, Drink):
            self.__drink_dao.delete_drink_by_id(item.get_id())
        else:
            self.__bakery_dao.delete_bakery_by_id(item.get_id())
        self.__log_dao.add_log(Log(f"Delete {item.get_name()} from system."))

    def save(self, item: Drink | Bakery, name: str = None, hprice: float = None, cprice: float = None, bprice: float = None) -> None:
        if isinstance(item, Drink):
            self.__drink_dao.update_drink(
                item.get_id(), name, hprice, cprice, bprice)
        else:
            self.__bakery_dao.update_bakery(item.get_id(), name, hprice)
        self.__log_dao.add_log(Log(f"Update {item.get_name()} from system."))
