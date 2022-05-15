from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Input(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = QLabel()
        self.label.setText('Vlastní funkce:')
        self.line = QLineEdit()
        self.line.setFixedWidth(180)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.line, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

        self.line.returnPressed.connect(self.parent().evt_input_enter)

