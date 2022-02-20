from abc import ABC



class Model(ABC):
    pass


class MenuModel(Model):

    def __init__(self):
        print("Log: Load" + type(self).__name__)
