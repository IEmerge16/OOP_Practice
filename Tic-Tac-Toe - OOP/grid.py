class Grid:
    def __init__(self):
        self.cell = {cell_number : "_" for cell_number in range(1, 10)}
        self.status = None
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
        for cell_number in range(1, 10):
            self.cell[cell_number] = "_"
        self.status = None
        self.is_full = False

    def update_cell(self, cell_number, mark):
        self.cell[cell_number] = mark
    
    def check_if_full(self):
        self.is_full = "_" not in self.cell.values()

    def check_rows(self):
        for row in (1, 4, 7):
            if self.cell[row] == self.cell[row + 1] == self.cell[row + 2] and self.cell[row] != "_":
                self.status = self.cell[row]

    def check_columns(self):
        for col in (1, 2, 3):
            if self.cell[col] == self.cell[col + 3] == self.cell[col + 6] and self.cell[col] != "_":
                self.status = self.cell[col]
    
    def check_diagonals(self):
        for diff in (2, 4):
            if self.cell[5 - diff] == self.cell[5] == self.cell[5 + diff] and self.cell[5] != "_":
                self.status = self.cell[5]

    def print_grid(self):
        print(self)