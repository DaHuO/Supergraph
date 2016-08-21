import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]


# Process each test case
case = 0
for line in lines:
	case += 1

	# Default result
	result = "INSOMNIA"

	# Initialize digit list (each index corresponds to a digit 0-9)
	digits_seen = [0] * 10

	# Get starting number from current input line
	starting_number = int(line)

	# Try up to 100 multiples before declaring insomnia
	for multiple in range(1, 200):
		current_number = starting_number * multiple

		# Read the result as a string
		result_as_string = str(current_number)

		# For each number in the string, increment associated index in digits_seen
		for index in range (0, len(result_as_string)):
			digits_seen[int(result_as_string[index])] += 1

		# Check if all digits have been seen
		if not 0 in digits_seen:
			result = str(current_number)
			break


	# Output
	print("Case #" + str(case) + ": " + result)