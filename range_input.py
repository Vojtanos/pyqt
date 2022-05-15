from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RangeInput(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.label_x = QLabel()
        self.label_x.setText('Rozsah osy X:')
        self.line_x = QLineEdit()
        self.button = QPushButton("ok")
        self.button.setAutoDefault(False)
        self.label_y = QLabel()
        self.label_y.setText('Rozsah osy Y:')
        self.line_y = QLineEdit()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label_x, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.line_x, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_y, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.line_y, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.parent().evt_range_clicked)