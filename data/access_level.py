from abc import ABC, abstractmethod


class AccessLevel(ABC):

    @abstractmethod
    def get_access_level() -> str:
        pass


class AdminAccess(AccessLevel):

    def get_access_level() -> str:
        return "Admin"


class EmployeeAccess(AccessLevel):

    def get_access_level() -> str:
        return "Employee"
