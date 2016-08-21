#!/usr/bin/python

import sys

def calculate_last_number(number):
	original_number = int(number)
	if (int(number) == 0):
		return 'INSOMNIA'
	else:
		digits_left = ['0','1','2','3','4','5','6','7','8','9']
		counter = 1
		while digits_left:
			digits_left = eliminate_numbers(number,digits_left)
			if digits_left:
				number = str(original_number*(counter+1))
				counter = counter + 1
			else:
				return number


# current_number - int - number currently analyzing
# digits_left - list - the list of digits left to find
def eliminate_numbers(current_number, digits_left):
	for digit in current_number:
		if (digit in digits_left):
			digits_left.remove(digit)
	return digits_left


file_name = sys.argv[1]
fp = open(file_name)
# All lines of file in list
contents = fp.read().splitlines()
# Only want values after first digit
test_cases = contents[1:]
# print test_cases

for index, value in enumerate(test_cases):
	print 'Case #' + str(index+1) + ': ' + calculate_last_number(value)




