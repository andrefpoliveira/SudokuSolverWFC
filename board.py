from square import Square

class Board:
    def __init__(self, initial_values):
        self.grid = [[Square(row, col) for col in range(9)] for row in range(9)]

        for row in range(9):
            for col in range(9):
                if initial_values[row][col] != 0:
                    self.grid[row][col].value = initial_values[row][col]
                    self.propagation(row, col, initial_values[row][col], True)

        self.actions = []

    def propagation(self, row, col, eigenstate, init = True):
        # Remove eigenstate from row
        for i, sq in enumerate(self.grid[row]):
            if i == col: continue
            else: sq.remove_eigenstate(eigenstate)

        # Remove eigenstate from column
        for i in range(9):
            if i == row: continue
            else: self.grid[i][col].remove_eigenstate(eigenstate)

        # Remove eigenstate from square
        for i in range(3 * (row//3), 3 * (row//3) + 3):
            for j in range(3 * (col//3), 3 * (col//3) + 3):
                self.grid[i][j].remove_eigenstate(eigenstate)

    def backtrack(self):
        if not self.actions: return False
        action, grid = self.actions.pop()
        row, col, eigenstate = action

        self.grid = grid
        self.grid[row][col].value = 0
        self.grid[row][col].remove_eigenstate(eigenstate)

        return True

    def solve(self):
        while True:
            squares = [item for sublist in self.grid for item in sublist]
            squares.sort(key = lambda x: (x.value, x.total_eigenstates))
            sq = squares[0]

            if sq.value != 0:
                print("Finished!")
                break
        
            if sq.value == 0 and sq.total_eigenstates == 0:
                if not self.backtrack():
                    print("Failed!")
                    return
                continue
        
            eigenstate = sq.choose_eigenstate()
            self.actions.append(((sq.row, sq.col, eigenstate), self.copy_grid()))
            self.propagation(sq.row, sq.col, eigenstate)

    def copy_grid(self):
        return [[ self.grid[row][col].copy() for col in range(9)] for row in range(9)]

    def print_grid(self):
        for i in self.grid:
            print(i)
        print()
