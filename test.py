# Import package
from src.cli_table import Table, align_data_left, align_data_center, align_data_right

# Create some data
data = [
	['First Name', 'Last Name', 'Grade'],
	['Roy', 'Trenneman', 5],
	['Maurice', 'Moss', 1],
	['Jen', 'Barber', 6],
	['Douglas', 'Reynholm', 9],
	['Richmond', 'Avenal', 7],
]

# Create the table
table = Table(
	data,
	alignment=[align_data_left, align_data_left, align_data_right],
	header_alignment=align_data_center,
	header=True,
)

# Sort by specific rows
table.sort_by('Grade')

# Freeze the table
table.freeze()

# Print the table
print(table)