import sqlite3
import os.path
from data_classes import *
from access_level import *


class AppDAO:

    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__ROOT_DIR, "perd_raan.db")

    def __init__(self):
        self.connection = sqlite3.connect(AppDAO.__DB_PATH)
        self.__user_dao = UserDAO(self.connection)
        self.__drink_dao = DrinkDAO(self.connection)
        self.__log_entry_dao = LogEntryDAO(self.connection, self.__user_dao)

    def close_database(self) -> None:
        self.connection.close()

    # UserDAO
    def add_user(self, user: User) -> None:
        self.__user_dao.add_user(user)

    def get_all_users(self) -> list[User]:
        return self.__user_dao.get_all_users()

    def get_user_by_id(self, id: int) -> User:
        return self.__user_dao.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        return self.__user_dao.get_user_by_username(username)

    # DrinkDAP
    def add_drink(self, drink: Drink) -> None:
        self.__drink_dao.add_drink(drink)

    def get_all_drinks(self) -> list[Drink]:
        return self.__drink_dao.get_all_drinks()

    def add_log_entry(self, log_entry: LogEntry) -> None:
        self.__log_entry_dao.add_log_entry(log_entry)


class UserDAO:
    __table_name = "USERS"
    __COLUMN_ID = "id"                             # int
    __COLUMN_FIRSTNAME = "first_name"              # str
    __COLUMN_LASTNAME = "last_name"                # str
    __COLUMN_USERNAME = "username"                 # str
    __COLUMN_PASSWORD = "password"                 # str
    __COLUMN_PHONE_NUMBER = "phone_number"         # str
    __COLUMN_ACCESSLEVEL = "access_level"          # str

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query = list()
        self.__create_table()

    def __create_table(self) -> None:
        self.__cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.__table_name} (
            {self.__COLUMN_ID} INTEGER PRIMARY KEY,
            {self.__COLUMN_FIRSTNAME} TEXT,
            {self.__COLUMN_LASTNAME} TEXT,
            {self.__COLUMN_USERNAME} TEXT,
            {self.__COLUMN_PASSWORD} TEXT,
            {self.__COLUMN_PHONE_NUMBER} TEXT,
            {self.__COLUMN_ACCESSLEVEL} TEXT
        )""")
        self.__connection.commit()

    def __convert_data_to_object(self) -> None:
        # convert raw data in query to User object
        convert_data = list()
        for data in self.__query:
            access_level = AdminAccess(
            ) if data[6] == "Admin" else EmployeeAccess()
            user = User(data[0], data[1], data[2], data[3],
                        data[4], data[5], access_level)
            convert_data.append(user)
        self.__query = convert_data

    def get_all_users(self) -> list[User]:
        self.__cursor.execute(f"SELECT * FROM {UserDAO.__table_name}")
        self.__query = self.__cursor.fetchall()
        self.__convert_data_to_object()
        return self.__query

    def get_user_by_id(self, id: int) -> User:
        self.__cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        data = self.__cursor.fetchone()
        if data is None:
            return None
        access_level = AdminAccess(
        ) if data[6] == "Admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3],
                    data[4], data[5], access_level)

    def get_user_by_username(self, username: str) -> User:
        self.__cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_USERNAME}='{username}'")
        data = self.__cursor.fetchone()
        if data is None:
            return None
        access_level = AdminAccess(
        ) if data[6] == "Admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3],
                    data[4], data[5], access_level)

    def add_user(self, user: User) -> None:
        access_level = "Admin" if isinstance(
            user.get_access_level(), AdminAccess) else "Employee"

        self.__cursor.execute(
            f"""INSERT INTO {UserDAO.__table_name}(
            {UserDAO.__COLUMN_FIRSTNAME},
            {UserDAO.__COLUMN_LASTNAME},
            {UserDAO.__COLUMN_USERNAME},
            {UserDAO.__COLUMN_PASSWORD},
            {UserDAO.__COLUMN_PHONE_NUMBER},
            {UserDAO.__COLUMN_ACCESSLEVEL})
            VALUES
            ('{user.get_firstname()}',
            '{user.get_lastname()}',
            '{user.get_username()}',
            '{user.get_password()}',
            '{user.get_phone_number()}',
            '{access_level}')""")

        self.__connection.commit()


class DrinkDAO:
    __table_name = "DRINKS"
    __COLUMN_ID = "id"
    __COLUMN_NAME = "name"
    __COLUMN_HOT = "hot"
    __COLUMN_COLD = "cold"
    __COLUMN_BLENDED = "blended"

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query = list()
        self.__create_table()

    def __create_table(self) -> None:
        self.__cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.__table_name} (
            {self.__COLUMN_ID} INTEGER PRIMARY KEY,
            {self.__COLUMN_NAME} TEXT,
            {self.__COLUMN_HOT} REAL,
            {self.__COLUMN_COLD} REAL,
            {self.__COLUMN_BLENDED} REAL
        )""")
        self.__connection.commit()

    def __convert_data_to_object(self) -> None:
        convert_data = list()
        for data in self.__query:
            drink = Drink(data[0], data[1], data[2], data[3], data[4])
            convert_data.append(drink)
        self.__query = convert_data

    def get_all_drinks(self) -> list[Drink]:
        self.__cursor.execute(f"SELECT * FROM {DrinkDAO.__table_name}")
        self.__query = self.__cursor.fetchall()
        self.__convert_data_to_object()
        return self.__query

    def get_drink_by_id(self, id: int) -> Drink:
        self.__cursor.execute(
            f"SELECT * FROM {DrinkDAO.__table_name} WHERE {DrinkDAO.__COLUMN_ID}={id}")
        data = self.__cursor.fetchone()
        if data is None:
            return None
        return Drink(data[0], data[1], data[2], data[3], data[4])

    def add_drink(self, drink: Drink):
        self.__cursor.execute(
            f"""INSERT INTO {DrinkDAO.__table_name}(
            {DrinkDAO.__COLUMN_ID},
            {DrinkDAO.__COLUMN_NAME},
            {DrinkDAO.__COLUMN_HOT},
            {DrinkDAO.__COLUMN_COLD},
            {DrinkDAO.__COLUMN_BLENDED})
            VALUES
            ('{drink.get_id()}',
            '{drink.get_name()}',
            '{drink.get_hot_price()}',
            '{drink.get_cold_price()}',
            '{drink.get_blended_price()}')""")

        self.__connection.commit()


class BakeryDAO:
    __table_name = "BAKERIES"


class LogEntryDAO:
    __table_name = "LOGENTRY"
    __COLUMN_ID = "id"
    __COLUMN_DATE = "date"
    __COLUMN_TIME = "time"
    __COLUMN_OPERATOR = "operator"
    __COLUMN_DESCRIPTION = "description"

    def __init__(self, connection: sqlite3.Connection, user_dao: UserDAO):
        self.__connection = connection
        self.__user_dao = user_dao
        self.__cursor = self.__connection.cursor()
        self.__query = list()
        self.__create_table()

    def __create_table(self) -> None:
        self.__cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.__table_name} (
            {self.__COLUMN_ID} INTEGER PRIMARY KEY,
            {self.__COLUMN_DATE} TEXT,
            {self.__COLUMN_TIME} TEXT,
            {self.__COLUMN_OPERATOR} INTEGER,
            {self.__COLUMN_DESCRIPTION} TEXT
        )""")
        self.__connection.commit()

    def __convert_data_to_object(self) -> None:
        convert_data = list()
        for data in self.__query:
            user = self.__user_dao.get_user_by_id(data[3])
            log_entry = LogEntry(data[0], data[1], data[2], user, data[4])
            convert_data.append(log_entry)
        self.__query = convert_data

    def get_all_log_entry(self) -> list[LogEntry]:
        self.__cursor.execute(f"SELETE * FROM {LogEntryDAO.__table_name}")
        self.__query = self.__cursor.fetchall()
        self.__convert_data_to_object()
        return self.__query

    def add_log_entry(self, log_entry: LogEntry) -> None:
        user = log_entry.get_operator()
        self.__cursor.execute(
            f"""INSERT INTO {LogEntryDAO.__table_name}(
            {LogEntryDAO.__COLUMN_ID},
            {LogEntryDAO.__COLUMN_DATE},
            {LogEntryDAO.__COLUMN_TIME},
            {LogEntryDAO.__COLUMN_OPERATOR},
            {LogEntryDAO.__COLUMN_DESCRIPTION})
            VALUES
            ('{log_entry.get_id()}',
            '{log_entry.get_date()}',
            '{log_entry.get_time()}',
            '{user.get_id()}',
            '{log_entry.get_description()}')""")
        self.__connection.commit()


class StockDAO:
    __table_name = "STOCKS"


if __name__ == "__main__":
    app = AppDAO()

    user = app.get_user_by_id(3)
    log_en = LogEntry(7, "16/12/2001", "13:50", user, "test")
    app.add_log_entry(log_en)
    app.close_database()
