from data import *

if __name__ == "__main__":
    data_access = AppDAO.get_dao("user")
    print(type(data_access).__name__)
