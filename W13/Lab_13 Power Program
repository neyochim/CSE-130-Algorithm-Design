# 1. Name:
#      Nathan Yochim
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program reads a JSON file containing power measurements, asks
#      the user for a sub-array size, and then computes the highest average
#      power for any consecutive window of that size.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was making the input validation strict enough to
#      match the assignment requirements without making the program awkward to
#      use. I had to check that the JSON file existed, that it contained an
#      "array" key first, and that every value in the array was really an
#      integer. I also had to be careful that the sliding-window logic stayed
#      efficient while still being easy to understand.
# 5. How long did it take for you to complete the assignment?
#      3 hours

import json


def load_power_values(filename):
	assert isinstance(filename, str), "Filename must be a string."
	assert filename.strip(), "Filename cannot be empty."

	try:
		with open(filename, "r", encoding="utf-8-sig") as input_file:
			power_data = json.load(input_file)
	except FileNotFoundError:
		print(f'Error: The file "{filename}" was not found.')
		return None
	except json.JSONDecodeError:
		print("Error: The file is not valid JSON.")
		return None
	except OSError as error:
		print(f"Error: Could not read the file. {error}")
		return None

	if not isinstance(power_data, dict):
		print('Error: The JSON file must contain an object with an "array" key.')
		return None

	keys = list(power_data.keys())
	if not keys or keys[0] != "array":
		print('Error: The first key in the JSON file must be "array".')
		return None

	power_values = power_data["array"]
	if not isinstance(power_values, list):
		print('Error: The value for "array" must be a list of integers.')
		return None

	if not power_values:
		print("Error: The power array cannot be empty.")
		return None

	for value in power_values:
		if type(value) is not int:
			print("Error: Every value in the power array must be an integer.")
			return None

	assert len(power_values) > 0, "The power list should not be empty here."

	return power_values


def prompt_for_window_size(max_size):
	assert isinstance(max_size, int), "The maximum size must be an integer."
	assert max_size > 0, "The maximum size must be positive."

	window_text = input("Enter the size of the sub-array: ")

	try:
		window_size = int(window_text)
	except ValueError:
		print("Error: The sub-array size must be a whole number.")
		return None

	if window_size <= 0:
		print("Error: The sub-array size must be greater than zero.")
		return None

	if window_size > max_size:
		print("Error: The sub-array size cannot be larger than the number of measurements.")
		return None

	assert 0 < window_size <= max_size, "Window size should be valid before returning."

	return window_size


def find_best_average(power_values, window_size):
	assert isinstance(power_values, list), "Power values must be stored in a list."
	assert all(type(value) is int for value in power_values), "Power values must all be integers."
	assert isinstance(window_size, int), "Window size must be an integer."
	assert 0 < window_size <= len(power_values), "Window size must fit inside the list."

	current_sum = 0
	for index in range(window_size):
		current_sum += power_values[index]

	best_sum = current_sum
	best_start_index = 0

	for index in range(window_size, len(power_values)):
		current_sum = current_sum - power_values[index - window_size] + power_values[index]

		if current_sum > best_sum:
			best_sum = current_sum
			best_start_index = index - window_size + 1

	best_average = best_sum / window_size

	assert best_average >= 0, "Average power should not be negative for this assignment."
	assert 0 <= best_start_index <= len(power_values) - window_size, "Best start index must be valid."

	return best_average, best_start_index


def main():
	filename = input("Enter the name of the power data file: ")
	power_values = load_power_values(filename)
	if power_values is None:
		return

	window_size = prompt_for_window_size(len(power_values))
	if window_size is None:
		return

	best_average, best_start_index = find_best_average(power_values, window_size)

	print(f"The highest average power is {best_average:.2f}.")
	print(f"It starts at index {best_start_index}.")


if __name__ == "__main__":
	main()
