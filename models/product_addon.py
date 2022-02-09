from dataclasses import dataclass


@dataclass
class AddOn:
    __name: str
    __price: float

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price
