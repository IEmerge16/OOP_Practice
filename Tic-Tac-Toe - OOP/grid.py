class Grid:
    def __init__(self):
        self.cell = {}
        for cell_number in range(1, 10):
            self.cell[cell_number] = "_"
        self.status = 0
        self.is_full = False

    def __repr__(self):
        return f"""
        {self.cell[1]} {self.cell[2]} {self.cell[3]}
        {self.cell[4]} {self.cell[5]} {self.cell[6]}
        {self.cell[7]} {self.cell[8]} {self.cell[9]}
        """

    def print_guide(self):
        print(f"""
        1 2 3
        4 5 6
        7 8 9
        """)

    def reset_grid(self):
        self.status = 0
        for cell_number in range(1, 10):
            self.cell[cell_number] = "_"

    def update_cell(self, cell_number, mark):
        self.cell[cell_number] = mark
    
    def check_if_full(self):
        self.is_full = True
        for cell in range(1, 10):
            if self.cell[cell] == "_":
                self.is_full = False

    def check_rows(self):
        for row in range(1, 8, 3):
            if (self.cell[row] == self.cell[row + 1] == self.cell[row + 2]) and self.cell[row] != "_":
                if self.cell[row] == "X":
                    self.status = 1
                else:
                    self.status = 2

    def check_columns(self):
        for col in range(1, 4):
            if (self.cell[col] == self.cell[col + 3] == self.cell[col + 6]) and self.cell[col] != "_":
                if self.cell[col] == "X":
                    self.status = 1
                else:
                    self.status = 2
    
    def check_diagonals(self):
        if (self.cell[1] == self.cell[5] == self.cell[9]) and self.cell[1] != "_":
            if self.cell[1] == "X":
                self.status = 1
            else:
                self.status = 2
        if (self.cell[3] == self.cell[5] == self.cell[7]) and self.cell[3] != "_":
            if self.cell[3] == "X":
                self.status = 1
            else:
                self.status = 2

    def print_grid(self):
        print(self)