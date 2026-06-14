# 1. Name:
#      Nathan Yochim
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program reads a JSON file containing an array of names, sorts the
#      names with selection sort, and prints the sorted list.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was matching the design from Lab 07 with the program
#      requirements in Lab 08. I had to make sure the selection sort logic was
#      done manually instead of using Python's built-in sort, and I also had to
#      keep the output format exact so it matched the example in the lab.
# 5. How long did it take for you to complete the assignment?
#      2 hours

import json
from pathlib import Path


def read_values_from_file(file_name):
	# Read the list of values from a JSON file.
	file_path = Path(__file__).parent / file_name
	with open(file_path, "r", encoding="utf-8-sig") as input_file:
		data = json.load(input_file)

	assert isinstance(data, dict), "The JSON file must contain an object."
	assert "array" in data, "The JSON file must contain an 'array' key."

	assert isinstance(data["array"], list), "The 'array' value must be a list."
	return data["array"]


def selection_sort(values):
	# Sort a list in ascending order using selection sort.
	for end_index in range(len(values) - 1, 0, -1):
		largest_index = 0

		for scan_index in range(1, end_index + 1):
			if values[scan_index] > values[largest_index]:
				largest_index = scan_index

		temp = values[end_index]
		values[end_index] = values[largest_index]
		values[largest_index] = temp


def display_values(file_name, values):
	# Display the sorted values exactly as the assignment example shows.
	print(f"The values in {file_name} are:")

	for value in values:
		print(f"\t{value}")


def main():
	# Run the sort program.
	file_name = input("What is the name of the file? ")
	values = read_values_from_file(file_name)

	selection_sort(values)
	display_values(file_name, values)


if __name__ == "__main__":
	main()
