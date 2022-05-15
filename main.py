import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtTest
from PyQt5.QtCore import *


from funkce.blind_search import BindAlg
from funkce.climber_search import ClimberAlg
from funkce.tabu_search import TabuAlg

from setting_widgets import  SettingWidgets
from combo_box import ComboBox
from radio_buttons import RadioButtons
from start_button import StartButton
from graph import Graph
from new_best import NewBest
from state import State
from input import Input
from range_input import RangeInput
from tutorial import Tutorial

from threading import *

import numpy as np

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.state = State()
        #nastavení okna
        self.setWindowTitle("FunctionSolver")
        self.resize(1000,600)
        self.setWindowIcon(QIcon("images/icon_start.png"))

        self.combo_box = ComboBox(self)
        self.radio_buttons = RadioButtons(self)
        self.setting_widgets = SettingWidgets(self)
        self.start_button = StartButton(self)
        self.graph = Graph(self)
        self.new_best = NewBest(self)
        self.input = Input(self)
        self.range_input = RangeInput(self)
        self.tutorial = Tutorial(self)

        #vnější layout a levý panel s nástroji pro nastavení
        self.outer_layout = QHBoxLayout()
        self.left_panel_widget = QWidget()
        self.left_panel = QVBoxLayout()
        self.left_panel_widget.setMaximumWidth(300);
        self.left_panel_widget.setMinimumWidth(220);
        self.left_panel_widget.setLayout(self.left_panel)
        self.outer_layout.addWidget(self.left_panel_widget)

        #přidání combo boxu do levého layoutu
        self.left_panel.addWidget(self.combo_box)
        self.left_panel.addWidget(self.input)
        # přidání tlačítek do levého layoutu
        self.left_panel.addWidget(self.radio_buttons)
        # přidání widgetů pro nastavení do levého layoutu
        self.left_panel.addWidget(self.setting_widgets)
        self.left_panel.addWidget(self.new_best)
        self.left_panel.addStretch()
        # přidání progress baru
        self.prg = QProgressBar()
        self.left_panel.addWidget(self.prg)
        # přidání start buttonu
        self.left_panel.addWidget(self.start_button)
        # přidání grafu
        self.right_panel = QVBoxLayout()
        self.inner_right = QHBoxLayout()
        self.inner_right.addWidget(self.range_input)
        self.inner_right.addWidget(self.tutorial, alignment=Qt.AlignRight)
        self.right_panel.addLayout(self.inner_right)
        self.right_panel.addWidget(self.graph)
        self.outer_layout.addLayout(self.right_panel)

        #vložení layoutu do hlavního okna
        self.setLayout(self.outer_layout)

        #nastavení stylesheetu
        #dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        #self.setStyleSheet(dark_stylesheet)

    # slot změní a vykreslí vybranou funkci
    def evt_range_clicked(self):
        try:
            x = int(self.range_input.line_x.text())
            y = int(self.range_input.line_y.text())
            #nastavení šířky vyhledávání v grafu
            maximum = max(x, y)
            width = 1
            while(2 ** width / 10 < maximum):
                width = width + 1;
            #width = width + 1;
            self.state.width = width
            #----------------------------
            self.graph.X = np.arange(-x, x, 0.5)
            self.graph.Y = np.arange(-y, y, 0.5)
            self.graph.X, self.graph.Y = np.meshgrid(self.graph.X, self.graph.Y)
            self.draw_function()
        except:
            QMessageBox.critical(self, "chyba","Zadejne číslo")

    def evt_tutorial_clicked(self):
        QMessageBox.information(self, "tutoriál", "Tvar vkládání vlastních funkcí:\n \n X ** 2            ==    X na druhou \n np.sin(Y)     ==     sinus(Y) \n np.cos(Y)    ==     cos(Y) \n np.pi             ==      pi \n np.log(Y)     ==      log(Y) \n X ** 1/2         ==       odmocnina")

    def evt_input_enter(self):
        self.state.selected_function = self.input.line.text()
        try:
            X = 1
            Y = 1
            eval(self.state.selected_function)
            self.draw_function()
        except:
            QMessageBox.critical(self, "chyba","chybně zadaná funkce")
            self.state.selected_function = "X ** 2 + Y ** 2"

    def evt_combo_box_changed(self, idx):
        data = self.combo_box.itemData(idx)
        QMessageBox.information(self, "ComboBox", "{}".format(data["popis"]))
        self.state.selected_function = data["fun"]
        print(self.state.selected_function)
        self.state.stop_when_cb_changed = True
        self.draw_function()

    def evt_sld_search(self, number):
        self.setting_widgets.l1.setText("Počet vyhledávání: " + str(number * 5))
        self.state.number_of_search = number * 5

    def evt_sld_mutate(self, number):
        self.setting_widgets.l2.setText("Mutační koeficient: " + str(number))
        self.state.mutate_koef = number

    def evt_sld_tabu(self, number):
        self.setting_widgets.l3.setText("Velikost tabu listu: " + str(number))
        self.state.max_tabu = number

    def evt_btn_start(self):
        try:
            lambda X, Y: eval(self.state.selected_function)
        except:
            QMessageBox.information(self, "chyba","chybně zadaná funkce")
            self.state.selected_function = "X ** 2 + Y ** 2"

        self.draw_function()  # aby nezůstali staré body
        function = lambda X, Y: eval(self.state.selected_function)
        params_of_fn = 2
        number_of_search = self.state.number_of_search
        width = self.state.width
        mutate_koef = self.state.mutate_koef
        number_of_childs = self.state.number_of_search
        max_tabu = self.state.max_tabu

        if self.state.selected_algorithm == "bind_search":
            bindAlg = BindAlg(function)
            array_of_points = bindAlg.run(number_of_search, width, params_of_fn)
            self.draw_climber(array_of_points)
            self.draw_blind(array_of_points)

        if self.state.selected_algorithm == "climber_search":
            climber = ClimberAlg(function, params_of_fn)
            array_of_points = climber.run(number_of_search, width, mutate_koef, number_of_childs)
            self.draw_climber(array_of_points)

        if self.state.selected_algorithm == "tabu_search":
            tsearcher = TabuAlg(function, params_of_fn)
            array_of_points = tsearcher.run(number_of_search, width, max_tabu)
            self.draw_tabu(array_of_points)

        print(self.state.selected_function)

    def evtn_rbt_blind_toggled(self, chk):
        if chk:
            self.state.selected_algorithm = "bind_search"
            self.setting_widgets.sld_mutate.hide()
            self.setting_widgets.sld_tabu.hide()
            self.setting_widgets.l2.hide()
            self.setting_widgets.l3.hide()

    def evtn_rbt_climber_toggled(self, chk):
        if chk:
            self.state.selected_algorithm = "climber_search"
            self.setting_widgets.sld_mutate.show()
            self.setting_widgets.sld_tabu.hide()
            self.setting_widgets.l2.show()
            self.setting_widgets.l3.hide()

    def evtn_rbt_tabu_toggled(self, chk):
        if chk:
            self.state.selected_algorithm = "tabu_search"
            self.setting_widgets.sld_mutate.hide()
            self.setting_widgets.sld_tabu.show()
            self.setting_widgets.l2.hide()
            self.setting_widgets.l3.show()

    def draw_function(self):
        X = self.graph.X
        Y = self.graph.Y
        Z = eval(self.state.selected_function)
        self.graph.axes.clear()
        self.graph.axes.plot_wireframe(X, Y, Z, alpha=0.7)
        self.graph.canvas.draw()

    def draw_blind(self, array_of_points):
        p = False
        prog_step = 1 / len(array_of_points)
        self.state.stop_when_cb_changed = False
        self.new_best.set_null()
        for point in array_of_points:
            if point[3] and p:
                p.set_color('red')
            color = "green" if point[3] else "red"
            if point[3]:
                p = self.graph.axes.scatter(point[1], point[2], point[0], color=color)
                self.new_best.set_point(point)
            else:
                self.graph.axes.scatter(point[1], point[2], point[0], color=color)

            self.graph.canvas.draw()
            self.prg.setValue(int(prog_step * 101))
            prog_step = prog_step + 1 / len(array_of_points)
            QtTest.QTest.qWait(500)
            if self.state.stop_when_cb_changed:
                break
        self.prg.setValue(0)

    def draw_climber(self, array_of_points):
        points = []
        prog_step = 1 / len(array_of_points)
        self.state.stop_when_cb_changed = False
        self.new_best.set_null()
        for point in array_of_points:
            color = "green" if point[3] else "red"
            p = self.graph.axes.scatter(point[1], point[2], point[0], color=color)
            self.graph.canvas.draw()
            self.prg.setValue(int(prog_step * 101))
            prog_step = prog_step + 1 / len(array_of_points)
            QtTest.QTest.qWait(50)
            if point[3]:
                self.new_best.set_point(point)
                for point in points:
                    point.remove()
                QtTest.QTest.qWait(1000)
                points = []
            else:
                points.append(p)
            if self.state.stop_when_cb_changed:
                break
        self.prg.setValue(0)

    def draw_tabu(self, array_of_points):
        points = []
        colors = ["green", "red", "orange"]
        self.state.stop_when_cb_changed = False
        prog_step = 1 / len(array_of_points)
        self.new_best.set_null()
        for point in array_of_points:
            color = colors[point[3]]
            p = self.graph.axes.scatter(point[1], point[2], point[0], color=color)
            self.graph.canvas.draw()
            self.prg.setValue(int(prog_step * 101))
            prog_step = prog_step + 1 / len(array_of_points)
            QtTest.QTest.qWait(50)
            if point[3] == 0:
                self.new_best.set_point(point)
                for point in points:
                    point.remove()
                QtTest.QTest.qWait(1000)
                points = []
            else:
                points.append(p)
            if self.state.stop_when_cb_changed:
                break

        self.prg.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg_main = DlgMain()
    dlg_main.show()
    sys.exit(app.exec_())

