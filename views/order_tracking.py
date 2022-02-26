import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Order_tracking(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.resize(1920, 1080)

        self.scrollArea_todo = QScrollArea(self)
        self.scrollArea_todo.setObjectName(u"scrollArea_todo")
        self.scrollArea_todo.setGeometry(QRect(183, 273, 400, 600))
        self.scrollArea_todo.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 398, 598))

        self.listView_todo_1 = QListView(self.scrollAreaWidgetContents)
        self.listView_todo_1.setObjectName(u"listView_todo_1")
        self.listView_todo_1.setGeometry(QRect(25, 35, 350, 250))
        self.listView_todo_2 = QListView(self.scrollAreaWidgetContents)
        self.listView_todo_2.setObjectName(u"listView_todo_2")
        self.listView_todo_2.setGeometry(QRect(25, 320, 350, 250))

        self.scrollArea_todo.setWidget(self.scrollAreaWidgetContents)

        self.label_todo = QLabel("TO DO",self)
        self.label_todo.setObjectName("label_todo")
        self.label_todo.setGeometry(QRect(217, 198, 200, 61))
        

        self.label_doing = QLabel("DOING",self)
        self.label_doing.setObjectName(u"label_doing")
        self.label_doing.setGeometry(QRect(835, 198, 200, 61))
        

        self.scrollArea_doing = QScrollArea(self)
        self.scrollArea_doing.setObjectName(u"scrollArea_doing")
        self.scrollArea_doing.setGeometry(QRect(805, 273, 400, 750))
        self.scrollArea_doing.setWidgetResizable(True)

        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 398, 748))

        self.listView_doing_1 = QListView(self.scrollAreaWidgetContents_2)
        self.listView_doing_1.setObjectName(u"listView_doing_1")
        self.listView_doing_1.setGeometry(QRect(25, 35, 350, 250))
        self.listView_doing_2 = QListView(self.scrollAreaWidgetContents_2)
        self.listView_doing_2.setObjectName(u"listView_doing_2")
        self.listView_doing_2.setGeometry(QRect(25, 320, 350, 250))

        self.scrollArea_doing.setWidget(self.scrollAreaWidgetContents_2)

        self.label_done = QLabel("DONE",self)
        self.label_done.setObjectName(u"label_done")
        self.label_done.setGeometry(QRect(1449, 198, 171, 61))
        

        self.scrollArea_done = QScrollArea(self)
        self.scrollArea_done.setObjectName(u"scrollArea_done")
        self.scrollArea_done.setGeometry(QRect(1414, 273, 400, 450))
        self.scrollArea_done.setWidgetResizable(True)

        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 398, 448))

        self.listView_done_1 = QListView(self.scrollAreaWidgetContents_3)
        self.listView_done_1.setObjectName(u"listView_done_1")
        self.listView_done_1.setGeometry(QRect(25, 35, 350, 250))

        self.scrollArea_done.setWidget(self.scrollAreaWidgetContents_3)

        self.show()
    def set_styleSheet(self, file_name: str):
        with open("themes/" + file_name, "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
            f.close

if __name__ == "__main__":
    app = QApplication(sys.argv)
    order_tracking = Order_tracking()
    order_tracking.set_styleSheet("order_tracking.qss")
    sys.exit(app.exec())      

