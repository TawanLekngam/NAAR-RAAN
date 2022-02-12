import sqlite3
import os.path


class AppDAO:

    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__ROOT_DIR, "pred_raan.db")

    def __init__(self) -> None:
        self.connection = sqlite3.connect(AppDAO.__DB_PATH)


class UserDAO:

    __table_name = "USERS"
    __COLUMN_NAME = ""
    __COLUMN_LASTNAME = ""
    __COLUMN_PASSWORD = ""
    __COLUMN_DATE_EMP = ""
    __COLUMN_STATUS = ""

    def __init__(self,connection:sqlite3.Connection) -> None:
        self.__connection = connection
        self.__curcor = self.__connection.cursor()
        self.__query = list()

    def get_all_users(self) -> list:
        self.__curcor.execute(f"SELECT * FROM {UserDAO.__table_name}")
        raw_data = self.__curcor.fetchall()

class ProductDAO:
    pass
