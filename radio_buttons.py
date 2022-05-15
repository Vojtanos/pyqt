from PyQt5.QtWidgets import *

class RadioButtons(QGroupBox):
    def __init__(self, parent):
        super().__init__("vybraná metoda:",parent)
        # tlačítka pro změnu funkce vybrané pro nalezení minima
        self.rbtn_blind = QRadioButton("Slepý algoritmus")
        self.rbtn_blind.setChecked(True)
        self.rbtn_climber = QRadioButton("Horolezecký algoritmus")
        self.rbtn_tabu = QRadioButton("Tabu algoritmus")
        self.lyt_methods = QVBoxLayout()
        self.lyt_methods.addWidget(self.rbtn_blind)
        self.lyt_methods.addWidget(self.rbtn_climber)
        self.lyt_methods.addWidget(self.rbtn_tabu)

        self.setLayout(self.lyt_methods)
        self.setFixedHeight(150)
        self.rbtn_blind.toggled.connect(self.parent().evtn_rbt_blind_toggled)
        self.rbtn_climber.toggled.connect(self.parent().evtn_rbt_climber_toggled)
        self.rbtn_tabu.toggled.connect(self.parent().evtn_rbt_tabu_toggled)