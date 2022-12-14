
from math import floor

def align_data_center(data: str, space: int, data_width: int, spacer=' ') -> str:
	space_left = space - data_width

	if space_left % 2 == 0:
		left_pad = space_left / 2
		right_pad = left_pad
	else:
		left_pad = floor(space_left / 2)
		right_pad = left_pad + 1

	return f'{spacer * int(left_pad)}{data}{spacer * int(right_pad)}'

def align_data_left(data: str, space: int, data_width: int, spacer=' ') -> str:
	space_left = space - data_width

	return f'{data}{spacer * int(space_left)}'

def align_data_right(data: str, space: int, data_width: int, spacer=' ') -> str:
	space_left = space - data_width

	return f'{spacer * int(space_left)}{data}'
