

from types import FunctionType
from typing import Any
from .aligners import align_data_center

class Cell:
	def __init__(self, data: Any) -> None:
		self.__data = data
		self.__aligner = align_data_center
		self.__conditional_formatter = None

	def get(self) -> Any:
		return self.__data

	def get_as_str(self) -> str:
		return str(self.__data)

	def get_as_display_str(self) -> str:
		if self.__conditional_formatter is None:
			return self.get_as_str()

		return self.__conditional_formatter(self.__data)

	def get_width(self) -> int:
		return len(self.get_as_str())

	def set_conditional_formatter(self, formatter: FunctionType) -> None:
		self.__conditional_formatter = formatter

	def set_aligner(self, aligner: FunctionType) -> None:
		self.__aligner = aligner

	def get_aligner(self) -> FunctionType:
		return self.__aligner

