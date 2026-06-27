# 1. Name:
#      Nathan Yochim
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program prompts the user for a start date and an end date, checks
#      that both dates are valid, and then computes the number of days between
#      them.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was organizing the validation so that each part of the
#      date was checked in the correct order. The day depends on the month and
#      year, so I had to make sure the program re-prompts the right value when a
#      user enters something invalid. I also had to be careful with leap years
#      so February would allow 29 days only when it should.
# 5. How long did it take for you to complete the assignment?
#      2.5 hours

BASE_YEAR = 1753


def is_leap_year(year):
	assert isinstance(year, int), "Year must be an integer."

	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True

	return False


def days_in_month(year, month):
	assert isinstance(year, int), "Year must be an integer."
	assert isinstance(month, int), "Month must be an integer."
	assert 1 <= month <= 12, "Month must be between 1 and 12."

	days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	if month == 2 and is_leap_year(year):
		return 29

	return days_per_month[month]


def days_before_year(year):
	assert isinstance(year, int), "Year must be an integer."
	assert year >= BASE_YEAR, f"Year must be {BASE_YEAR} or later."

	total_days = 0

	for current_year in range(BASE_YEAR, year):
		if is_leap_year(current_year):
			total_days += 366
		else:
			total_days += 365

	return total_days


def date_to_days(year, month, day):
	assert isinstance(year, int), "Year must be an integer."
	assert isinstance(month, int), "Month must be an integer."
	assert isinstance(day, int), "Day must be an integer."
	assert year >= BASE_YEAR, f"Year must be {BASE_YEAR} or later."
	assert 1 <= month <= 12, "Month must be between 1 and 12."
	assert 1 <= day <= days_in_month(year, month), "Day is out of range for the given month."

	total_days = days_before_year(year)

	for current_month in range(1, month):
		total_days += days_in_month(year, current_month)

	total_days += day - 1

	return total_days


def days_between(start_year, start_month, start_day, end_year, end_month, end_day):
	start_days = date_to_days(start_year, start_month, start_day)
	end_days = date_to_days(end_year, end_month, end_day)

	if end_days < start_days:
		raise ValueError("End date must not be before start date.")

	return end_days - start_days


def prompt_for_integer(prompt, error_message):
	while True:
		value_text = input(prompt)

		try:
			value = int(value_text)
		except ValueError:
			print(error_message)
			continue

		return value


def prompt_for_year(prompt):
	while True:
		year = prompt_for_integer(prompt, "Please enter a whole number for the year.")

		if year < BASE_YEAR:
			print(f"The year must be {BASE_YEAR} or later.")
			continue

		return year


def prompt_for_month(prompt):
	while True:
		month = prompt_for_integer(prompt, "Please enter a whole number for the month.")

		if month < 1 or month > 12:
			print("The month must be between 1 and 12.")
			continue

		return month


def prompt_for_day(prompt, year, month):
	while True:
		day = prompt_for_integer(prompt, "Please enter a whole number for the day.")

		max_day = days_in_month(year, month)
		if day < 1 or day > max_day:
			if month == 2:
				print(f"February {year} has only {max_day} days.")
			else:
				print(f"That month has only {max_day} days.")
			continue

		return day


def get_date(label):
	year = prompt_for_year(f"{label} year: ")
	month = prompt_for_month(f"{label} month: ")
	day = prompt_for_day(f"{label} day: ", year, month)

	return year, month, day


def main():
	start_year, start_month, start_day = get_date("Start")
	end_year, end_month, end_day = get_date("End")

	while True:
		try:
			number_of_days = days_between(
				start_year, start_month, start_day,
				end_year, end_month, end_day)
		except ValueError as error:
			print(error)
			end_year, end_month, end_day = get_date("End")
			continue

		break

	print()
	print(f"There are {number_of_days} days")


if __name__ == "__main__":
	main()
