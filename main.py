from board import Board

with open("tests/evil") as f:
    lines = f.readlines()
    board = [[int(i) for i in l.strip()] for l in lines[1:]]

b = Board(board)
b.print_grid()
b.solve()
b.print_grid()