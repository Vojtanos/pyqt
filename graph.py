from PyQt5.QtWidgets import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import seaborn as sns

class Graph(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # comboboxy pro nastavení zobrazované funkce
        self.fig = plt.figure()
        self.axes = plt.axes(projection="3d")
        self.canvas = FigureCanvas(self.fig)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

        self.X = np.arange(-10, 10, 0.5)
        self.Y = np.arange(-10, 10, 0.5)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        X = self.X
        Y = self.Y
        Z = eval(self.parent().state.selected_function)
        self.axes.clear()
        self.axes.plot_wireframe(X, Y, Z, alpha=0.7)
        self.canvas.draw()
