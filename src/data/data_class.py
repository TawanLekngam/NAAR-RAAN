from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.data.access_level import AccessLevel


@dataclass
class User:
    __id: int
    __firstname: str
    __lastname: str
    __username: str
    __password: str
    __access_level: AccessLevel

    def get_id(self) -> int:
        return self.__id

    def get_firstname(self) -> str:
        return self.__firstname

    def get_lastname(self) -> str:
        return self.__lastname

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_access_level(self) -> AccessLevel:
        return self.__access_level

    def get_access_level_str(self) -> str:
        return self.__access_level.get_access_level()


class Product(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass


@dataclass
class Drink(Product):
    __id: int
    __name: str
    __hot_price: float
    __cold_price: float
    __blended_price: float

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_h_price(self) -> float:
        return self.__hot_price

    def get_c_price(self) -> float:
        return self.__cold_price

    def get_b_price(self) -> float:
        return self.__blended_price


@dataclass
class Bakery(Product):
    __id: int
    __name: str
    __price: float

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price


@dataclass
class Addon(Product):
    __id: int
    __name: str
    __price: float

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price


@dataclass
class Receipt:
    __id: int
    __date: str
    __time: str
    __detail: str

    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_detail(self) -> str:
        return self.__detail


@dataclass
class Receipt_Item:
    """
    class that contain the detail of item in the receipt.
    """
    __id: int
    __date: str
    __time: str
    __item: str
    __cost: float
    __quantity: int

    def __str__(self) -> str:
        return f"{self.__item:<15} x {self.__quantity:>5} : {self.__cost * self.__quantity:.2f}"

    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_detail(self) -> str:
        """
        return detail of receipt item.
        """
        return self.__str__()


@dataclass
class LogEntry:
    __id: int
    __date: str
    __time: str
    __operator: int
    __description: str

    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_operator(self) -> str:
        return self.__operator

    def get_description(self) -> str:
        return self.__description


@dataclass
class TargetRevenue:
    __year: str
    __month: str
    __target_revenue: int

    def get_year(self) -> str:
        return self.__year

    def get_month(self) -> str:
        return self.__month

    def get_target_revenue(self) -> int:
        return self.__target_revenue
