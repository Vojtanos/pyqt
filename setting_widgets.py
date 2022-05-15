from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SettingWidgets(QGroupBox):
    def __init__(self, parent):
        super().__init__("nastavení:",parent)
        self.l1 = QLabel()
        self.l1.setText("Počet vyhledávání: 10")
        self.sld_search = QSlider(Qt.Horizontal)
        self.sld_search.setTickPosition(QSlider.TicksBothSides)
        self.sld_search.setMinimum(1)
        self.sld_search.setMaximum(20)
        self.sld_search.setSliderPosition(2)
        self.sld_search.valueChanged.connect(self.parent().evt_sld_search)

        self.l2 = QLabel()
        self.l2.setText("Mutační koeficient: 5")
        self.sld_mutate = QSlider(Qt.Horizontal)
        self.sld_mutate.setTickPosition(QSlider.TicksBothSides)
        self.sld_mutate.setTickInterval(20)
        self.sld_mutate.setSingleStep(1)
        self.sld_mutate.setMinimum(0)
        self.sld_mutate.setMaximum(25)
        self.sld_mutate.setSliderPosition(5)
        self.sld_mutate.valueChanged.connect(self.parent().evt_sld_mutate)

        self.l3 = QLabel()
        self.l3.setText("Velikost tabu listu: " + str(int(self.parent().state.width / 2)))
        self.sld_tabu = QSlider(Qt.Horizontal)
        self.sld_tabu.setTickPosition(QSlider.TicksBothSides)
        self.sld_tabu.setTickInterval(20)
        self.sld_tabu.setSingleStep(1)
        self.sld_tabu.setMinimum(0)
        self.sld_tabu.setMaximum(self.parent().state.width)
        self.sld_tabu.setSliderPosition(int(self.parent().state.width / 2))
        self.sld_tabu.valueChanged.connect(self.parent().evt_sld_tabu)

        self.sld_mutate.hide()
        self.sld_tabu.hide()
        self.l2.hide()
        self.l3.hide()

        # nastavení - widgety a rozložení
        self.grid = QGridLayout()
        self.grid.addWidget(self.l1, 1, 0)
        self.grid.addWidget(self.sld_search, 2, 0)
        self.grid.addWidget(self.l2, 3, 0)
        self.grid.addWidget(self.sld_mutate, 4, 0)
        self.grid.addWidget(self.l3, 5, 0)
        self.grid.addWidget(self.sld_tabu, 6, 0)
        self.setLayout(self.grid)