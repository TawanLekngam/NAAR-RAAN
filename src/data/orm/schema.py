import os
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, Float, create_engine

# set up database and connection
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection = "sqlite:///" + os.path.join(BASE_DIR, "data.db")
Schema = declarative_base()
engine = create_engine(connection)
Session = sessionmaker()


class User(Schema):
    __tablename__ = "USERS"
    id = Column("id", Integer(), primary_key=True)
    fname = Column("first_name", String(255))
    lname = Column("last_name", String(255))
    username = Column("username", String(255))
    password = Column("password", String(255))
    access_level = Column("access_level", String(5))

    def __init__(self, fname: str, lname: str, username: str, password: str, access_level: str):
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.access_level = access_level

    def __str__(self) -> str:
        return f"<User first_name = {self.fname:<15} last_name = {self.lname:<15} username = {self.username:<15} password = {self.password:<15} access_level = {self.access_level}>"

    def get_id(self) -> int:
        "return user's id."
        return self.id

    def get_fname(self) -> str:
        "return user's firstname."
        return self.fname

    def get_lname(self) -> str:
        "return user's lastname."
        return self.lname

    def get_username(self) -> str:
        "return user's username."
        return self.username

    def get_password(self) -> str:
        "return user's password."
        return self.password

    def get_access_level(self) -> str:
        "return user's access level."
        return self.access_level


class Drink(Schema):
    __tablename__ = "DRINKS"
    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(255))
    hprice = Column("hprice", Float())
    cprice = Column("cprice", Float())
    bprice = Column("bprice", Float())

    def __init__(self, name: str, hprice: float, cprice: float, bprice: float):
        super().__init__()
        self.name = name
        self.hprice = hprice
        self.cprice = cprice
        self.bprice = bprice

    def __str__(self) -> str:
        return f"<Drink {self.name:<15} hot {self.hprice:<4.02f} cold {self.cprice:<4.02f} blend {self.bprice:<4.02f}>"

    def get_id(self) -> int:
        "return drink's id."
        return self.id

    def get_hprice(self) -> float:
        "return hot price."
        return self.hprice

    def get_c_price(self) -> float:
        "return cold price."
        return self.cprice

    def get_bprice(self) -> float:
        "return blend price."
        return self.bprice


class Bakery(Schema):
    __tablename__ = "BAKERIES"
    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(255))
    price = Column("price", Float())

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"<Bakery {self.name:<15} price {self.price:<4.02f}>"

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class Addon(Schema):
    __tablename__ = "ADDONS"
    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(255))
    price = Column("price", Float())

    def __str__(self) -> str:
        return f"<Addon {self.name:<15} price {self.price:<4.02f}>"

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class Log(Schema):
    __tablename__ = "LOGS"
    id = Column("id", Integer(), primary_key=True)
    date = Column("date", String(30))
    time = Column("time", String(30))
    desc = Column("description", String(1000))

    def __init__(self, desc: str, id: int = None, date: str = None, time: str = None):
        self.id = id
        self.date = date
        self.time = time
        self.desc = desc

        if None in [self.date, self.time]:
            now = datetime.now()
            self.date = f"{now.day:02d}-{now.month:02d}-{now.year}"
            self.time = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"

    def __str__(self):
        return f"<Log {self.date} {self.time} description={self.desc}>"

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> str:
        return self.date

    def get_time(self) -> str:
        return self.time

    def get_desc(self) -> str:
        return self.desc

    def get_detail(self) -> tuple:
        return self.date, self.time, self.desc
