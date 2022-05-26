from abc import ABC
from sqlalchemy import desc
from .schema import Session, engine
from .schema import User, Drink, Bakery, Log, Receipt


class DAO(ABC):
    "data access object (base model)."

    def __init__(self, session: Session):
        self.session = session


class AppDAO:
    local_session = Session(bind=engine)

    @staticmethod
    def get_dao(type: str) -> DAO:
        pass


class UserDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_user(self, user: User) -> None:
        if self.exist(user):
            return

        self.session.add(user)
        self.session.commit()

    def get_all_users(self) -> list[User]:
        return self.session.query(User).all()

    def get_user_by_id(self, id: int) -> User:
        return self.session.query(User).filter(User.id == id).first()

    def get_user_by_username(self, username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()

    def exist(self, user: User) -> bool:
        "return True if User exist in the database."
        if user is None:
            return False

        query = self.session.query(User).filter(
            User.fname == user.get_fname(),
            User.lname == user.get_lname(),
            User.username == user.get_username(),
            User.password == user.get_password(),
            User.access_level == user.get_access_level()
        ).first()
        return query is not None

    def delete_user_by_id(self, id: int):
        user: User = self.session.query(User).filter(User.id == id).first()
        if user is None:
            return

        self.session.delete(user)
        self.session.commit()

    def update_user(
            self, id: int,
            fname: str = None,
            lname: str = None,
            username: str = None,
            password: str = None,
            access_level: str = None) -> bool:
        """update user data."""
        user: User = self.session.query(User).filter(User.id == id).first()

        if user is None:
            return False

        if id is not None:
            user.id = id

        if fname is not None:
            user.fname = fname

        if lname is not None:
            user.lname = lname

        if username is not None:
            user.username = username

        if password is not None:
            user.password = password

        if access is not None:
            user.access_level = access_level

        self.session.commit()
        return True


class DrinkDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)
