import sqlite3
import os.path
from data_classes import *
from access_level import *


class AppDAO:

    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__ROOT_DIR, "perd_raan.db")

    def __init__(self) -> None:
        self.connection = sqlite3.connect(AppDAO.__DB_PATH)
        self.__user_dao = UserDAO(self.connection)
        self.__user_dao.create_table()

    def close_database(self) -> None:
        self.connection.close()

    def add_user(self, user: User) -> None:
        self.__user_dao.add_user(user)

    def get_all_users(self) -> list[User]:
        return self.__user_dao.get_all_users()

    def get_user_by_id(self, id: int) -> User:
        return self.__user_dao.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        return self.__user_dao.get_user_by_username(username)


class UserDAO:

    __table_name = "USERS"
    __COLUMN_ID = "id"                             # int
    __COLUMN_FIRSTNAME = "first_name"              # str
    __COLUMN_LASTNAME = "last_name"                # str
    __COLUMN_USERNAME = "username"                 # str
    __COLUMN_PASSWORD = "password"                 # str
    __COLUMN_PHONE_NUMBER = "phone_number"         # str
    __COLUMN_ACCESSLEVEL = "access_level"          # str

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.__connection = connection
        self.__curcor = self.__connection.cursor()
        self.__query = list()

    def create_table(self) -> None:
        self.__curcor.execute(f"""CREATE TABLE IF NOT EXISTS {self.__table_name} (
            {self.__COLUMN_ID} INTEGER PRIMARY KEY,
            {self.__COLUMN_FIRSTNAME} TEXT,
            {self.__COLUMN_LASTNAME} TEXT,
            {self.__COLUMN_USERNAME} TEXT,
            {self.__COLUMN_PASSWORD} TEXT,
            {self.__COLUMN_PHONE_NUMBER} TEXT,
            {self.__COLUMN_ACCESSLEVEL} TEXT
        )""")
        self.__connection.commit()

    def __convert_to_object(self) -> None:
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
        self.__curcor.execute(f"SELECT * FROM {UserDAO.__table_name}")
        self.__query = self.__curcor.fetchall()
        self.__convert_to_object()
        return self.__query

    def get_user_by_id(self, id: int) -> User:
        self.__curcor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        data = self.__curcor.fetchall()
        if data is None:
            return None
        access_level = AdminAccess(
        ) if data[6] == "Admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3],
                    data[4], data[5], access_level)

    def get_user_by_username(self, username: str) -> User:
        self.__curcor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_USERNAME}='{username}'")
        data = self.__curcor.fetchall()
        if data is None:
            return None
        access_level = AdminAccess(
        ) if data[6] == "Admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3],
                    data[4], data[5], access_level)

    def add_user(self, user: User) -> None:
        access_level = "Admin" if isinstance(
            user.get_access_level(), AdminAccess) else "Employee"

        self.__curcor.execute(
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


class ProductDAO:
    __table_name = "PRODUCTS"


class LogEntryDAO:
    __table_name = "LOGENTRIES"


class StockDAO:
    __table_name = "STOCKS"


if __name__ == "__main__":
    app = AppDAO()
    user1 = User(1,"natcha","teekayu","snowball","fay","0000000000",AdminAccess())
    user2 = User(1,"prima","sirinapapant","kon suay","nene","0000000001",EmployeeAccess())
    app.add_user(user1)
    app.add_user(user2)
    app.close_database()
