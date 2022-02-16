from abc import ABC
from dataclasses import dataclass

from access_level import AccessLevel


@dataclass
class User:
    __id: int
    __firstname: str
    __lastname: str
    __username: str
    __password: str
    __phone_number: str
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

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_access_level(self) -> AccessLevel:
        return self.__access_level


class Product(ABC):
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

    def get_hot_price(self) -> float:
        return self.__hot_price

    def get_cold_price(self) -> float:
        return self.__cold_price

    def get_blended_price(self) -> float:
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
class LogEntry:
    __id: int
    __date: str
    __time: str
    __operator: User
    __description: str

    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_operator(self) -> User:
        return self.__operator

    def get_description(self) -> str:
        return self.__description
