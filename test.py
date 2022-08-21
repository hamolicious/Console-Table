
from secrets import choice
from src.cli_table import Table, align_data_left, align_data_center, align_data_right
from random import randint
from string import ascii_letters

width = randint(2, 6)
height = randint(5, 20)

heading = [[''.join([choice(ascii_letters) for _ in range(3, 10)]) for _ in range(width)]]
data = [[randint(0, 9999) for _ in range(width)] for _ in range(height)]

table = Table(
	heading + data,
	alignment=align_data_right,
	header_alignment=align_data_center,
	header=True,
)

table.sort_by(heading[0][0])

table.freeze()
print(table)



