import sys


def get_letter_counts(s):
	letter_counts = {}
	for c in s:
		if (c not in letter_counts):
			letter_counts[c] = 0
		letter_counts[c] += 1

	return letter_counts


digit_letter_counts = {
	0 : {'Z': 1, 'E': 1, 'R': 1, 'O': 1},
	1 : {'O': 1, 'N': 1, 'E': 1},
	2 : {'T': 1, 'W': 1, 'O': 1},
	3 : {'T': 1, 'H': 1, 'R': 1, 'E': 2},
	4 : {'F': 1, 'O': 1, 'U': 1, 'R': 1},
	5 : {'F': 1, 'I': 1, 'V': 1, 'E': 1},
	6 : {'S': 1, 'I': 1, 'X': 1},
	7 : {'S': 1, 'E': 2, 'V': 1, 'N': 1},
	8 : {'E': 1, 'I': 1, 'G': 1, 'H': 1, 'T': 1},
	9 : {'N': 2, 'I': 1, 'E': 1}
}


def sufficient_counts(dict1, dict2):
	for key in dict1:
		if (key not in dict2):
			return False
		elif (dict2[key] < dict1[key]):
			return False

	return True


def subtract_counts(dict1, dict2):
	new_counts = dict2.copy()
	for key in dict1:
		new_counts[key] = dict2[key] - dict1[key]

	return new_counts


def get_phone_number(remaining_letter_counts, curr_phone_number, phone_number):
	if (all(value == 0 for value in remaining_letter_counts.values())):
		phone_number[0] = curr_phone_number
	else:
		for digit in range(10):
			curr_digit_letter_counts = digit_letter_counts[digit]
			if (sufficient_counts(curr_digit_letter_counts, remaining_letter_counts)):
				new_counts = subtract_counts(curr_digit_letter_counts, remaining_letter_counts)
				get_phone_number(new_counts, str(digit) + curr_phone_number, phone_number)


input = open(sys.argv[1], 'r')

input.readline()
lines = input.readlines()

for line_index in range(len(lines)):
	if (lines[line_index][-1] == '\n'):
		lines[line_index] = lines[line_index][:-1]
	s = lines[line_index]

	s_letter_counts = get_letter_counts(s)

	phone_number = [None]
	get_phone_number(s_letter_counts, '', phone_number)

	print('Case #' + str(line_index + 1) + ': ' + phone_number[0])


input.close()
