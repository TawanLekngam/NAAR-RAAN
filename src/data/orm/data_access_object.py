from abc import ABC, abstractmethod
from sqlalchemy import desc
from data.orm.schema import Session, engine
from data.orm.schema import User, Drink, Bakery, Log, Receipt


class DAO(ABC):
    "data access object (base model)."

    def __init__(self, session: Session):
        self.session = session


class AppDAO:

    local_session = Session(bind=engine)

    @staticmethod
    def get_dao(type: str) -> DAO:
        """
        return the data access object.\n
        user -> UserDAO\n
        drink -> DrinkDAO\n
        bakery -> BakeryDAO\n
        log -> LogDAO\n
        receipt -> ReceiptDAO
        """
        if type == "user":
            return UserDAO(AppDAO.local_session)
        elif type == "drink":
            return DrinkDAO(AppDAO.local_session)
        elif type == "bakery":
            return BakeryDAO(AppDAO.local_session)
        elif type == "log":
            return LogDAO(AppDAO.local_session)
        elif type == "receipt":
            return ReceiptDAO(AppDAO.local_session)

        else:
            return None

class UserDAO(DAO):

    def __init__(self, session: Session):
        super().__init__(session)

    def add_user(self, user: User) -> None:
        if user is None or self.__exist(user):
            return

        self.session.add(user)
        self.session.commit()

    def get_all_users(self) -> list[User]:
        return self.session.query(User).all()

    def get_user_by_id(self, id: int) -> User:
        return self.session.query(User).filter(User.id == id).first()

    def get_user_by_username(self, username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()

    def delete_user_by_id(self, id: int):
        user: User = self.session.query(User).filter(User.id == id).first()
        if user is None:
            return

        self.session.delete(user)
        self.session.commit()

    def update_user(
            self,
            id: int,
            fname: str = None,
            lname: str = None,
            username: str = None,
            password: str = None,
            access_level: str = None) -> bool:
        """update user data."""
        user: User = self.session.query(User).filter(User.id == id).first()

        if user is None:
            return False

        if fname is not None:
            user.fname = fname

        if lname is not None:
            user.lname = lname

        if username is not None:
            user.username = username

        if password is not None:
            user.password = password

        if access_level is not None:
            user.access_level = access_level

        self.session.commit()
        return True

    def __exist(self, user: User) -> bool:
        "return True if User __exist in the database."
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


class DrinkDAO(DAO):

    def __init__(self, session: Session):
        super().__init__(session)

    def add_drink(self, drink: Drink) -> None:
        if drink is None or self.__exist(drink):
            return

        self.session.add(drink)
        self.session.commit()

    def get_all_drinks(self) -> list[Drink]:
        return self.session.query(Drink).all()

    def get_drink_by_id(self, id: int) -> Drink:
        return self.session.query(Drink).filter(Drink.id == id).first()

    def delete_drink_by_id(self, id: int):
        drink: Drink = self.session.query(Drink).filter(Drink.id == id).first()
        if drink is None:
            return

        self.session.delete(drink)
        self.session.commit()

    def update_drink(
            self,
            id: int,
            name: str = None,
            hprice: float = None,
            cprice: float = None,
            bprice: float = None) -> bool:
        """update drink data."""
        drink: Drink = self.session.query(Drink).filter(Drink.id == id).first()

        if drink is None:
            return False

        if name is not None:
            drink.name = name

        if hprice is not None:
            drink.hprice = hprice

        if cprice is not None:
            drink.cprice = cprice

        if bprice is not None:
            drink.bprice = bprice
        self.session.commit()
        return True

    def __exist(self, drink: Drink) -> bool:
        if drink is None:
            return False

        query = self.session.query(Drink).filter(
            Drink.name == drink.get_name(),
            Drink.hprice == drink.get_hprice(),
            Drink.cprice == drink.get_cprice(),
            Drink.bprice == drink.get_bprice()
        ).first()
        return query is not None


class BakeryDAO(DAO):

    def __init__(self, session: Session):
        self.session = session

    def add_bakery(self, bakery, Bakery) -> None:
        if bakery is None or self.__exist(bakery):
            return

        self.session.add(bakery)
        self.session.commit()

    def get_all_bakeries(self) -> list[Bakery]:
        return self.session.query(Bakery).all()

    def get_bakery_by_id(self, id: int) -> Bakery:
        return self.session.query(Bakery).filter(Bakery.id == id).first()

    def delete_bakery_by_id(self, id: int) -> None:
        bakery: Bakery = self.session.query(
            Bakery).filter(User.id == id).first()
        if bakery is None:
            return

        self.session.delete(bakery)
        self.session.commit()

    def update_bakery(
            self,
            id: int,
            name: str = None,
            price: float = None) -> bool:
        bakery: Bakery = self.session.query(
            Bakery).filter(User.id == id).first()

        if bakery is None:
            return False

        if name is not None:
            bakery.name == name

        if price is not None:
            bakery.price == price

        self.session.commit()
        return True

    def __exist(self, bakery: Bakery) -> bool:
        if bakery is None:
            return None

        query = self.session.query(Bakery).filter(
            Bakery.name == bakery.get_name(),
            Bakery.price == bakery.get_price()
        ).first()
        return query is not None


class LogDAO(DAO):
    LOG_LIMIT = 50

    def __init__(self, session: Session):
        super().__init__(session)

    def add_log(self, log: Log) -> None:
        if log is None:
            return

        self.session.add(log)
        self.session.commit()

    def get_all_logs(self) -> list[Log]:
        return self.session.query(Log).order_by(desc(Log.id)).limit(LogDAO.LOG_LIMIT).all()


class ReceiptDAO(DAO):
    RECEIPT_LIMIT = 100

    def __init__(self, session: Session):
        super().__init__(session)

    def add_receipt(self, receipt: Receipt) -> None:
        if receipt is not None:
            return

        self.session.add(receipt)
        self.session.commit()

    def get_all_receipts(self) -> list[Receipt]:
        return self.session.query(Receipt).order_by(desc(Receipt.id)).limit(ReceiptDAO.RECEIPT_LIMIT).all()
