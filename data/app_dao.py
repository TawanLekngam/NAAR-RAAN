import sqlite3
import os
from abc import ABC, abstractmethod
from data.data_classes import *
from data.access_level import *


class DAO(ABC):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = self.connection.cursor()


class AppDAO:
    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__ROOT_DIR, "naar_raan.db")
    __connection: sqlite3.Connection = sqlite3.connect(__DB_PATH)

    @staticmethod
    def get_dao(database: str = None) -> DAO:
        if database == "user":
            return UserDAO(AppDAO.__connection)
        if database == "product":
            return ProductDAO(AppDAO.__connection)
        return None

    @staticmethod
    def close_database() -> None:
        """ disconnect database."""
        AppDAO.__connection.close()


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
        self.cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {UserDAO.__table_name} (
            {UserDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {UserDAO.__COLUMN_FIRSTNAME} TEXT,
            {UserDAO.__COLUMN_LASTNAME} TEXT,
            {UserDAO.__COLUMN_USERNAME} TEXT,
            {UserDAO.__COLUMN_PASSWORD} TEXT,
            {UserDAO.__COLUMN_ACCESSLEVEL} TEXT)""")
        self.connection.commit()

    def add_user(self, user: User) -> None:
        """ add user data to users table."""
        access_level = user.get_access_level_str()
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
            level = access.get_access_level_str()
            query += f'{UserDAO.__COLUMN_ACCESSLEVEL}="{level}"'

        if query[-2] == ',':
            query = query[:-2]

        query += f" WHERE {UserDAO.__COLUMN_ID}={id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_users(self) -> list[User]:
        self.execute(f"SELECT * FROM {UserDAO.__table_name}")
        query = self.cursor.fetchall()
        # convert data
        convert_data = list()
        for data in query:
            access_level = AdminAccess(
            ) if data[5] == "admin" else StaffAccess()
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
        access_level = AdminAccess() if data[5] == "admin" else StaffAccess()
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
        access_level = AdminAccess() if data[5] == "admin" else StaffAccess()
        return User(data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    access_level)

    def delete_user_by_id(self, id: int) -> None:
        """ delete user data at given id."""
        self.cursor.execute(
            f"DELETE FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        self.connection.commit()


class DrinkDAO(DAO):
    __table_name = "DRINKS"
    __COLUMN_ID = "id"
    __COLUMN_NAME = "name"
    __COLUMN_HP = "hot_price"
    __COLUMN_CP = "cold_price"
    __COLUMN_BP = "blended_price"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()

    def __create_table(self) -> None:
        self.cursor.execute(
            f"""CREATE TABLE IF NOT EIXSTS {DrinkDAO.__table_name} (
            {DrinkDAO.__COLUMN_ID} INTEGER PRIMARY KEY),
            {DrinkDAO.__COLUMN_NAME} TEXT,
            {DrinkDAO.__COLUMN_HP} REAL,
            {DrinkDAO.__COLUMN_CP} REAL,
            {DrinkDAO.__COLUMN_HP} REAL)""")
        self.connection.commit()

    def add_drink(self, drink: Drink) -> None:
        pass

    def get_all_drinks(self) -> list[Drink]:
        self.cursor.execute(f"""SELETE * FROM {DrinkDAO.__table_name}""")
        query = self.cursor.fetchall()
        convert_data = list()
        for data in query:
            drink = Drink(data[0], data[1], data[2], data[3], data[4])
            convert_data.append(drink)
        return convert_data

    def get_drink_by_id(self, id: int) -> Drink:
        pass

    def get_drink_by_name(self, name: str) -> Drink:
        pass

    def update_drink(self, id: int, name: str = None, hprice: float = None, cprice: float = None, bprice: float = None) -> None:
        pass

    def delete_drink(self, id: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {DrinkDAO.__table_name} WHERE {DrinkDAO.__COLUMN_ID}={id}")
        self.connection.commit()


class BakeryPriceDAO(DAO):
    __table_name = "PRICE_BAKERIES"
    __COLUMN_ID = "id"
    __COLUMN_PRICE = "price"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()

    def __create_table(self) -> None:
        self.cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {BakeryPriceDAO.__table_name} (
            {BakeryPriceDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {BakeryPriceDAO.__COLUMN_PRICE} REAL)""")
        self.connection.commit()

    def add_bakery_price(self, id: int, price: float) -> None:
        self.cursor.execute(f"""INSERT INTO {BakeryPriceDAO.__table_name} (
            {BakeryPriceDAO.__COLUMN_ID},
            {BakeryPriceDAO.__COLUMN_PRICE})
            VALUES
            ({id},
            {price})""")
        self.connection.commit()

    def get_bakery_price(self, id: int) -> float:
        self.cursor.execute(
            f"SELETE * FROM {BakeryPriceDAO.__table_name} WHERE {BakeryPriceDAO.__COLUMN_ID}={id}")
        query = self.cursor.fetchone()
        return query

    def update_bakery_price(self, id: int, price: float = None) -> None:
        if price is None:
            return
        self.cursor.execute(
            f"""UPDATE {BakeryPriceDAO.__table_name} SET {BakeryPriceDAO.__COLUMN_PRICE}={price} WHERE {BakeryPriceDAO.__COLUMN_ID}={id}""")
        self.connection.commit()

    def delete_bakery_price(self, id: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {BakeryPriceDAO.__table_name} WHERE {BakeryPriceDAO.__COLUMN_ID}={id}")
        self.connection.commit()


class ProductDAO(DAO):
    __table_name = "PRODUCTS"
    __COLUMN_ID = "id"
    __COLUMN_NAME = "name"
    __COLUMN_TYPE = "type"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__create_table()
        self.__DP_DAO = DrinkPriceDAO(connection)
        self.__BP_DAO = BakeryPriceDAO(connection)

    def __create_table(self) -> None:
        self.cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {ProductDAO.__table_name} (
            {ProductDAO.__COLUMN_ID} INTEGER PRIMARY KEY,
            {ProductDAO.__COLUMN_NAME} TEXT,
            {ProductDAO.__COLUMN_TYPE} TEXT)""")
        self.connection.commit()

    def add_product(self, product: Product) -> None:
        product_type = "drink" if isinstance(product, Drink) else "bakery"
        self.cursor.execute(f"""INSERT INTO {ProductDAO.__table_name}(
            {ProductDAO.__COLUMN_NAME},
            {ProductDAO.__COLUMN_TYPE},)
            VALUES
            ('{product.get_name()}',
            '{product_type}')""")
        self.connection.commit()

    def get_all_products(self, filter=None) -> list[Product]:
        pass

    def get_product_by_id(self, id: int) -> Product:
        self.cursor.execute(
            f"SELETE * FROM {ProductDAO.__table_name} WHERE {ProductDAO.__COLUMN_ID}={id}")
        query = self.cursor.fetchone()

        if query[2] == "drink":
            return
        elif query[2] == "bakery":
            return

        return None

    def update_product(self) -> None:
        pass

    def delete_product(self, id: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {ProductDAO.__table_name} WHERE {ProductDAO.__COLUMN_ID}={id}")
        self.connection.commit()
