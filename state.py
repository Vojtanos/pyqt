class State():
    def __init__(self):
        super().__init__()
        self.selected_function = "X ** 2 + Y ** 2"
        self.selected_algorithm = "bind_search"
        self.stop_when_cb_changed = False

        # nastavení parametrů pro vyhledávací algoritmy
        self.width = 7
        self.number_of_search = 10
        self.mutate_koef = 5
        self.max_tabu = int(self.width / 2)