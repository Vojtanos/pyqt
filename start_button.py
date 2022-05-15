from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class StartButton(QPushButton):
    def __init__(self, parent):
        super().__init__("Najdi minimum", parent)
        self.setAutoDefault(False)
        # button pro začátek vyhledávání
        self.setIcon(QIcon(QPixmap("images/icon_start.png")))
        self.move(40, 40)
        # self.btn_start.resize(120, 50)
        self.clicked.connect(self.parent().evt_btn_start)