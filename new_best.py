from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NewBest(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.label_x = QLabel()
        self.label_y = QLabel()
        self.label_z = QLabel()
        # comboboxy pro nastavení zobrazované funkce
        self.label_x.setText("X : 0")
        self.label_y.setText("Y : 0")
        self.label_z.setText("Z : 0")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label_x, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_y, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_z, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

        stylesheet = """
        QWidget {
            border: 1px solid black;
            border-radius: 4px;
            background-color: rgb(255, 255, 255);
            }
        """

        self.setStyleSheet(stylesheet)

    def set_null(self):
        self.label_x.setText("X : 0")
        self.label_y.setText("Y : 0")
        self.label_z.setText("Z : 0")

    def set_point(self, point):
        self.label_x.setText(f'X : {round(point[1],2)}')
        self.label_y.setText(f'Y : {round(point[2],2)}')
        self.label_z.setText(f'Z : {round(point[0],2)}')