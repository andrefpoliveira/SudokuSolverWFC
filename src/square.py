from __future__ import annotations
from colorama import Fore

class Square:
	def __init__(self, row: int, col: int, value = 0, eigenstates = None, defined = False) -> Square:
		self.row = row
		self.col = col
		self.value = value
		self.defined = defined
	
		self.eigenstates = eigenstates or [True for _ in range(9)]
		self.total_eigenstates = sum(self.eigenstates)


	def board_defined(self, value: int) -> None:
		self.value = value
		self.defined = True


	def select_eigenstate(self, eigenstate: int = 0) -> int:
		"""
		Select a eigenstate for the current square.
		If no eigenstate is provided, select the first available one.

		Args:
			eigenstate (int, optional): The eigenstate to select. Defaults to 0.

		Returns:
			int: The eigenstate selected.
		"""
		self.value = self.eigenstates.index(True) + 1 if eigenstate == 0 else eigenstate
		self.remove_eigenstate(self.value)
		return self.value

	
	def remove_eigenstate(self, eigenstate: int) -> None:
		"""
		Removes a eigenstate from the square.

		Args:
			eigenstate (int): The eigenstate to remove.
		"""
		if self.eigenstates[eigenstate-1]:
			self.eigenstates[eigenstate-1] = False
			self.total_eigenstates -= 1


	def __str__(self) -> str:
		"""
		Returns the string representation of the square.

		Returns:
			str: The string representation of the square.
		"""
		return (Fore.WHITE if self.defined else Fore.MAGENTA) + f"{self.value if self.value != 0 else '.'}" + Fore.RESET


	def __repr__(self) -> str:
		"""
		Returns the string representation of the square.

		Returns:
			str: The string representation of the square.
		"""
		return str(self)


	def copy(self) -> Square:
		"""
		Returns a copy of the square.

		Returns:
			Square: The copy of the square.
		"""
		return Square(self.row, self.col, self.value, self.eigenstates.copy(), self.defined)