from PyQt5.QtWidgets import *

class ComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        # comboboxy pro nastavení zobrazované funkce
        self.addItem("Paraboloid", {"fun": "X ** 2 + Y ** 2", "popis": "Základní funkce"})
        self.addItem("Rastrigin", {"fun": "(X**2 - 10 * np.cos(1.1 * np.pi * X)) +(Y**2 - 10 * np.cos(1.1 * np.pi * Y)) + 20", "popis": "Tato funkce skutečně prověří schopnosti algoritmu"})
        self.addItem("Funkce 3",
                               {"fun": "np.sin(np.sqrt(X ** 2 + Y ** 2))", "popis": "Středně obtížná funkce"})

        # odeslání signálu při změně checkboxu
        self.currentIndexChanged.connect(self.parent().evt_combo_box_changed)
