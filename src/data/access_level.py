from abc import ABC, abstractmethod


class AccessLevel(ABC):
    @abstractmethod
    def get_access_level() -> str:
        pass


class AdminAccess(AccessLevel):

    level: str = "admin"

    def get_access_level() -> str:
        return AdminAccess.level


class StaffAccess(AccessLevel):

    level: str = "staff"

    def get_access_level() -> str:
        return StaffAccess.level
