from abc import ABC, abstractmethod


class Access_level(ABC):

    @abstractmethod
    def get_access_level() -> str:
        pass


class Admin_level(Access_level):

    def get_access_level() -> str:
        return "Admin"


class Employee_level(Access_level):

    def get_access_level() -> str:
        return "Employee"
