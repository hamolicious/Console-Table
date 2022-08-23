# Import package
from src.cli_table import Table, align_data_left, align_data_center, align_data_right
import colorama

# Create some data
data = [
	['First Name', 'Last Name', 'Grade'],
	['Roy', 'Trenneman', 5],
	['Maurice', 'Moss', 1],
	['Jen', 'Barber', 6],
	['Douglas', 'Reynholm', 9],
	['Richmond', 'Avenal', 0],
]

# Create the table
table = Table(
	data,
	alignment=[align_data_left, align_data_left, align_data_right],
	header_alignment=align_data_center,
	header=True,
	use_color=True
)

def red_if_zero(data: float|int) -> str:
	if data == 0:
		return f'{colorama.Fore.RED}{data}{colorama.Fore.RESET}'
	return str(data)

# Sort by specific rows
table.sort_by('Grade')
table.set_conditional_formatter_for('Grade', red_if_zero)

# Freeze the table
table.freeze()

# Print the table
print(table)