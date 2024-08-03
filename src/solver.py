from __future__ import annotations
import os
import time

from src.square import Square

class Solver:
	"""
	Solver class that will solve the sudoku puzzle using the WFC (Wave Function Collapse) algorithm.
	"""
	def __init__(self) -> Solver:
		self.board = None

		# Stats
		self.actions = []
		self.backtracks = 0

	def load(self, filename: str) -> None:
		"""
		Loads the sudoku puzzle from a file.

		Args:
			filename (str): The file to load the puzzle from.
		"""
		# Check if the file exists
		if not os.path.exists(filename):
			raise FileNotFoundError(f"File {filename} not found.")

		# Load the grid
		with open(filename) as f:
			grid = [[int(v) for v in l.strip()] for l in f.readlines()]

		# Create the board
		self.board = [[Square(row, col) for col in range(9)] for row in range(9)]
		for row in range(9):
			for col in range(9):
				if grid[row][col] != 0:
					self.board[row][col].board_defined(grid[row][col])
					self.propagate(row, col, grid[row][col])


	def propagate(self, row: int, col: int, eigenstate: int) -> None:
		"""
		Updates the eigenstates of all the squares affected by chosing the value for another square.

		Args:
			row (int): The row of the square.
			col (int): The column of the square.
			eigenstate (int): The eigenstate to remove from the affected
		"""
		# Remove eigenstate from row
		for i, sq in enumerate(self.board[row]):
			if i == col: continue
			else: sq.remove_eigenstate(eigenstate)

        # Remove eigenstate from column
		for i in range(9):
			if i == row: continue
			else: self.board[i][col].remove_eigenstate(eigenstate)

        # Remove eigenstate from square
		for i in range(3 * (row//3), 3 * (row//3) + 3):
			for j in range(3 * (col//3), 3 * (col//3) + 3):
				self.board[i][j].remove_eigenstate(eigenstate)


	def backtrack(self) -> bool:
		"""
		Backtracks the last action taken.

		Returns:
			bool: True if the backtracking was successful, False otherwise.
		"""
		if not self.actions:
			return False

		self.backtracks += 1

		action, board = self.actions.pop()
		row, col, eigenstate = action

		self.board = board
		self.board[row][col].value = 0
		self.board[row][col].remove_eigenstate(eigenstate)

		return True


	def copy_board(self) -> list[list[Square]]:
		"""
		Returns a copy of the board.

		Returns:
			list[list[Square]]: A copy of the board.
		"""
		return [[sq.copy() for sq in row] for row in self.board]

	
	def solve(self, filename: str, metric_time = False, metric_backtracks = False) -> None:
		self.load(filename)

		start = time.time()

		while True:
			squares = [item for sublist in self.board for item in sublist]
			squares.sort(key = lambda x: (x.value, x.total_eigenstates))
			sq = squares[0]

			if sq.value != 0:
				break
        
			if sq.value == 0 and sq.total_eigenstates == 0:
				if not self.backtrack():
					print("This sudoku is not solvable! Please confirm the input.")
					return
				continue
        
			eigenstate = sq.select_eigenstate()
			self.actions.append(((sq.row, sq.col, eigenstate), self.copy_board()))
			self.propagate(sq.row, sq.col, eigenstate)

		end = time.time()

		print(self)

		if metric_time:
			print(f"Solve time: {end - start:.4f}s")

		if metric_backtracks:
			print(f"Backtracks: {self.backtracks}")


	def __str__(self) -> str:
		"""
		Returns the string representation of the board.

		Returns:
			str: The string representation of the board.
		"""
		return '\n'.join(
			[' '.join(str(sq) for sq in row[:3]) + ' | ' +\
			 ' '.join(str(sq) for sq in row[3:6]) + ' | ' +\
			 ' '.join(str(sq) for sq in row[6:]) +\
				('\n' + '-'*21 if i in [2, 5] else '')
			 	for i, row in enumerate(self.board)
			])


	def __repr__(self) -> str:
		"""
		Returns the string representation of the board.

		Returns:
			str: The string representation of the board.
		"""
		return str(self)