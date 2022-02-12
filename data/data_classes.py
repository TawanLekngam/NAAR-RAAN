

from dataclasses import dataclass
from access_level import AccessLevel


class Data:
    pass


@dataclass
class User:

    __id: int
    __firstname: str
    __lastname: str
    __username: str
    __password: str         # MayBe Hashing
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


@dataclass
class Product:

    __id: int
    __name: str

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_name(self, name: str) -> None:
        self.__name = name


class ProductAddon:

    pass
