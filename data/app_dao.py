import sqlite3
import os
from abc import ABC
from data.data_classes import *
from data.access_level import *


class AppDAO:
    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__ROOT_DIR, "naar_raan.db")
    __connection: sqlite3.Connection = sqlite3.connect(__DB_PATH)

    @staticmethod
    def get_dao(database: str = None) -> DAO:
        if database == "user":
            return UserDAO(AppDAO.__connection)
        elif database == "drink":
            return DrinkDAO(AppDAO.__connection)
        elif database == "bakery":
            return BakeryDAO(AppDAO.__connection)
        elif database == "log":
            return LogDAO(AppDAO.__connection)
        return None

    @staticmethod
    def close_database() -> None:
        """ disconnect database."""
        AppDAO.__connection.close()


class DAO(ABC):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = self.connection.cursor()


class UserDAO(DAO):
    __table_name = "USERS"
    __COLUMN_ID = "id"
    __COLUMN_FIRSTNAME = "first_name"
    __COLUMN_LASTNAME = "last_name"
    __COLUMN_USERNAME = "username"
    __COLUMN_PASSWORD = "password"
    __COLUMN_ACCESSLEVEL = "access_level"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()

    def __create_table(self) -> None:
        """ create users table if not exists."""
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {UserDAO.__table_name} (
            {UserDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {UserDAO.__COLUMN_FIRSTNAME} TEXT,
            {UserDAO.__COLUMN_LASTNAME} TEXT,
            {UserDAO.__COLUMN_USERNAME} TEXT,
            {UserDAO.__COLUMN_PASSWORD} TEXT,
            {UserDAO.__COLUMN_ACCESSLEVEL} TEXT)""")
        self.cursor.commit()

    def add_user(self, user: User) -> None:
        """ add user data to users table."""
        access_level = "Admin" if isinstance(
            user.get_access_level(), AdminAccess) else "Staff"
        self.cursor.execute(
            f"""INSERT INTO {UserDAO.__table_name}(
            {UserDAO.__COLUMN_FIRSTNAME},
            {UserDAO.__COLUMN_LASTNAME},
            {UserDAO.__COLUMN_USERNAME},
            {UserDAO.__COLUMN_PASSWORD},
            {UserDAO.__COLUMN_ACCESSLEVEL})
            VALUES
            ('{user.get_firstname()}',
            '{user.get_lastname()}',
            '{user.get_username()}',
            '{user.get_password()}',
            '{access_level}')""")
        self.connection.commit()

    def update_user(
        self,
        id: int,
        firstname: str = None,
        lastname: str = None,
        username: str = None,
        password: str = None,
        access: AccessLevel = None
    ) -> None:
        """ update user data where the given id.
            example:    update_user(10, firstname="natcha", access=AdminAccess())
        """
        query = f"UPDATE {UserDAO.__table_name} SET "

        if firstname is not None:
            query += f'{UserDAO.__COLUMN_FIRSTNAME}="{firstname}", '
        if lastname is not None:
            query += f'{UserDAO.__COLUMN_LASTNAME}="{lastname}", '
        if username is not None:
            query += f'{UserDAO.__COLUMN_USERNAME}="{username}", '
        if password is not None:
            query += f'{UserDAO.__COLUMN_PASSWORD}="{password}", '
        if access is not None:
            level = "admin" if isinstance(access, AdminAccess) else "staff"
            query += f'{UserDAO.__COLUMN_ACCESSLEVEL}="{level}"'

        if query[-2] == ',':
            query = query[:-2]

        query += f" WHERE {UserDAO.__COLUMN_ID}={id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_users(self) -> list[User]:
        self.execute(f"SELECT * FROM {UserDAO.__table_name}")
        raw_query = self.cursor.fetchall()
        # convert data
        convert_data = list()
        for data in raw_query:
            access_level = AdminAccess(
            ) if data[5] == "Admin" else StaffAccess()
            user = User(data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        access_level)
            convert_data.append(user)
        return convert_data

    def get_user_by_id(self, id: int) -> User:
        self.cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        data = self.cursor.fetchone()
        if data is None:
            return None
        access_level = AdminAccess() if data[5] == "Admin" else StaffAccess()
        return User(data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    access_level)

    def get_user_by_username(self, username: str) -> User:
        self.cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_USERNAME}='{username}'")
        data = self.cursor.fetchone()
        if data is None:
            return None
        access_level = AdminAccess() if data[5] == "Admin" else StaffAccess()
        return User(data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    access_level)

    def delete_user_by_id(self, id: int) -> None:
        """ delete user data at given id."""
        self.cursor.execute(
            f"DELETE FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}"
        )
        self.connection.commit()


class DrinkDAO(DAO):
    __table_name = "DRINKS"
    __COLUMN_ID = "id"
    __COLUMN_NAME = "name"
    __COLUMN_HOT = "hot"
    __COLUMN_COLD = "cold"
    __COLUMN_BLENDED = "blended"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()

    def __create_table(self) -> None:
        self.execute(f"""CREATE TABLE IF NOT EXISTS {DrinkDAO.__table_name} (
            {DrinkDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {DrinkDAO.__COLUMN_NAME} TEXT,
            {DrinkDAO.__COLUMN_HOT} REAL,
            {DrinkDAO.__COLUMN_COLD} REAL,
            {DrinkDAO.__COLUMN_BLENDED} REAL)""")
        self.commit()

    def add_drink(self, drink: Drink):
        self.execute(
            f"""INSERT INTO {DrinkDAO.__table_name}(
            {DrinkDAO.__COLUMN_ID},
            {DrinkDAO.__COLUMN_NAME},
            {DrinkDAO.__COLUMN_HOT},
            {DrinkDAO.__COLUMN_COLD},
            {DrinkDAO.__COLUMN_BLENDED})
            VALUES
            ('{drink.get_id()}',
            '{drink.get_name()}',
            '{drink.get_h_price()}',
            '{drink.get_c_price()}',
            '{drink.get_b_price()}')""")
        self.commit()

    def get_all_drinks(self) -> list[Drink]:
        self.execute(f"SELECT * FROM {DrinkDAO.__table_name}")
        raw_query = self.cursor.fetchall()
        # convert data
        convert_data = list()
        for data in raw_query:
            drink = Drink(data[0], data[1], data[2], data[3], data[4])
            convert_data.append(drink)
        return convert_data

    def get_drink_by_id(self, id: int) -> Drink:
        self.execute(
            f"SELECT * FROM {DrinkDAO.__table_name} WHERE {DrinkDAO.__COLUMN_ID}={id}")
        data = self.cursor.fetchone()
        if data is None:
            return None
        return Drink(data[0], data[1], data[2], data[3], data[4])


class BakeryDAO(DAO):
    __table_name = "BAKERIES"
    __COLUMN_ID = "id"
    __COLUMN_NAME = "name"
    __COLUMN_PRICE = "price"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()

    def __create_table(self) -> None:
        self.execute(f"""CREATE TABLE IF NOT EXISTS {BakeryDAO.__table_name} (
            {BakeryDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {BakeryDAO.__COLUMN_NAME} TEXT,
            {BakeryDAO.__COLUMN_PRICE} REAL
        )""")
        self.commit()

    def add_bakery(self, bakery: Bakery) -> None:
        self.execute(
            f"""INSERT INTO {BakeryDAO.__table_name} (
            {BakeryDAO.__COLUMN_ID},
            {BakeryDAO.__COLUMN_NAME},
            {BakeryDAO.__COLUMN_PRICE})
            VALUES
            ('{bakery.get_id()}',
            '{bakery.get_name()}',
            '{bakery.get_price()}')""")
        self.commit()

    def get_all_bakeries(self) -> list[Bakery]:
        self.execute(f"SELECT * FROM {BakeryDAO.__table_name}")
        raw_query = self.cursor.fetchall()
        convert_data = list()
        for data in self.__query:
            bakery = Bakery(data[0], data[1], data[2])
            convert_data.append(bakery)
        return convert_data

    def get_bakery_by_id(self, id: int) -> Bakery:
        self.execute(
            f"SELECT * FROM {BakeryDAO.__table_name} WHERE {BakeryDAO.__COLUMN_ID}={id}")
        data = self.cursor.fetchone()
        if data is None:
            return None
        return Bakery(data[0], data[1], data[2])


class LogDAO(DAO):
    __table_name = "LOGS"
    __COLUMN_ID = "id"
    __COLUMN_DATE = "date"
    __COLUMN_TIME = "time"
    __COLUMN_DESCRIPTION = "description"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()

    def __create_table(self) -> None:
        self.execute(f"""CREATE TABLE IF NOT EXISTS {LogDAO.__table_name} (
            {LogDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {LogDAO.__COLUMN_DATE} TEXT,
            {LogDAO.__COLUMN_TIME} TEXT,
            {LogDAO.__COLUMN_OPERATOR} INTEGER,
            {LogDAO.__COLUMN_DESCRIPTION} TEXT)""")
        self.commit()

    def add_log_entry(self, log: Log) -> None:
        user = log_entry.get_operator()
        self.execute(
            f"""INSERT INTO {LogDAO.__table_name}(
            {LogDAO.__COLUMN_ID},
            {LogDAO.__COLUMN_DATE},
            {LogDAO.__COLUMN_TIME},
            {LogDAO.__COLUMN_DESCRIPTION})
            VALUES
            ('{log.get_id()}',
            '{log.get_date()}',
            '{log.get_time()}',
            '{log.get_description()}')""")
        self.commit()

    def get_all_logs(self) -> list[LogEntry]:
        self.execute(f"SELETE * FROM {LogDAO.__table_name}")
        raw_query = self.cursor.fetchall()
        convert_data = list()
        for data in raw_query:
            log = Log(data[0], data[1], data[2], data[3])
            convert_data.append(log)
        return convert_data

    def get_log__by_id(self, id: int) -> Log:
        self.execute(
            f"SELETE * FROM {LogDAO.__table_name} WHERE {LogDAO.__COLUMN_ID}={id}")
        data = self.cursor.fetchone()
        if data is None:
            return None
        return Log(data[0], data[1], data[2], data[3])
