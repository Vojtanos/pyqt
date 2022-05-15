from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Tutorial(QPushButton):
    def __init__(self, parent):
        super().__init__("tutoriál", parent)
        self.setAutoDefault(False)
        self.setFixedWidth(120)
        # button pro začátek vyhledávání
        self.move(40, 40)
        # self.btn_start.resize(120, 50)
        self.clicked.connect(self.parent().evt_tutorial_clicked)