# Console-Table
Displaying Tables in the console

## How To Use
```python
# Import package
from cli_table import Table, align_data_left, align_data_center, align_data_right

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
	alignment=align_data_left,
	header_alignment=align_data_center,
	header=True,
)

# Sort by specific rows
table.sort_by('Grade')

# Freeze the table
table.freeze()

# Print the table
print(table)
```

Output:
```
| First Name | Last Name | Grade |
| Maurice    | Moss      | 1     |
| Roy        | Trenneman | 5     |
| Jen        | Barber    | 6     |
| Richmond   | Avenal    | 7     |
| Douglas    | Reynholm  | 9     |
```

## Arguments

### Table()
Creates a table object

| Argument            | Type             | Default Value | Description |
| ------------------- | ---------------- | ------------- |------------ |
| `data`              | `list[list[Any]]` |  | 2D array containing the data to be used |
| `margin=`           | `int` | `1` | Margin around cells, (how many spaces before and after data) |
| `alignment=`        | `align_data_left` \| `align_data_center` \| `align_data_right` | `align_data_center` | How to align data |
| `header_alignment=` | `align_data_left` \| `align_data_center` \| `align_data_right` | `align_data_center` | How to align headers |
| `header=`           | `bool` | `False` | Does the data contain a header (0th row is the header) |
| `add_top=`          | `bool` | `False` | Add a top border around the table |
| `add_bottom=`       | `bool` | `False` | Add a bottom border around the table |
| `use_color=`        | `bool` | `False` | Use `colorama` colors for the table |
| `header_color_bg=`  | `str` | `colorama.Back.RESET` | Header Background Color |
| `header_color_fg=`  | `str` | `colorama.Fore.LIGHTBLUE_EX` | Header Foreground Color |
| `odd_color_bg=`     | `str` | `colorama.Back.RESET` | Odd Numbered Cells Background Color |
| `odd_color_fg=`     | `str` | `colorama.Fore.BLUE` | Odd Numbered Cells Foreground Color |
| `even_color_bg=`    | `str` | `colorama.Back.RESET` | Even Numbered Cells Background Color |
| `even_color_fg=`    | `str` | `colorama.Fore.CYAN` | Even Numbered Cells Foreground Color |

### Table().is_frozen()
Checks if the table needs to be frozen before printing


### Table().sort_by()
Sorts the table by the values of a column

| Argument            | Type             | Default Value | Description |
| ------------------- | ---------------- | ------------- |------------ |
| `column`            | `str` \| `int` |  | Which column index(int) or name(str) to sort by |
| `key=`              | `None` \| `Callable` | `None` | Sorting key, takes the entire row, should return a sortable value, bu default, returns the entire cell |
| `reverse=`          | `bool` | `False` | Reverses the sorting algorithm, asc or desc |


### Table().update_data()
Changes the data that the table has

| Argument            | Type             | Default Value | Description |
| ------------------- | ---------------- | ------------- |------------ |
| `data`           | `list[list[Any]]` |  | New data to be used |


### Table().freeze()
Compiles the given data into a string for quick displaying


### Table().display() | print(Table())
Prints the table

