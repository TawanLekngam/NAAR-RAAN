from abc import ABC


class Product(ABC):
    __id: int
    __name: str

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id


class Drink(Product):

    def __init__(self) -> None:
        super().__init__()