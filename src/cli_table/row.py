

from typing import Any
import colorama

from .cell import Cell


class Row:
	def __init__(self, data: list[Any]) -> None:
		self.__data = [Cell(i) for i in data]

	def get_width(self) -> int:
		return len(self.__data)

	def get_at(self, index: int) -> Any:
		return self.__data[index]

	def get_all(self) -> list[Cell]:
		return self.__data

