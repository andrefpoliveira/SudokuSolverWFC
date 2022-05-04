class Square:
    def __init__(self, row, col, value = 0, eigenstates = None):
        self.row = row
        self.col = col
        self.value = value
        
        self.eigenstates = [True for _ in range(9)] if eigenstates == None else eigenstates
        self.total_eigenstates = sum(self.eigenstates)

    def choose_eigenstate(self, eigenstate = 0):
        self.value = self.eigenstates.index(True) + 1 if eigenstate == 0 else eigenstate
        self.remove_eigenstate(self.value)
        return self.value

    def remove_eigenstate(self, eigenstate):
        if self.eigenstates[eigenstate-1]:
            self.eigenstates[eigenstate-1] = False
            self.total_eigenstates -= 1

    def __str__(self):
        return f"{self.value if self.value != -1 else ' '}"

    def __repr__(self):
        return str(self)

    def copy(self):
        return Square(self.row, self.col, self.value, self.eigenstates.copy())