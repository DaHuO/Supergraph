import sys


def reverse_and_flip(s):
	new_s = ''

	for c in s[::-1]:
		if (c == '+'):
			new_s += '-'
		else:
			new_s += '+'

	return new_s


input = open(sys.argv[1], 'r')

t = input.readline()
lines = input.readlines()

for line_index in range(len(lines)):
	if (lines[line_index][-1] == '\n'):
		lines[line_index] = lines[line_index][:-1]

	s = lines[line_index]

	reverse_and_flips_count = 0

	while (not all(c == '+' for c in s)):
		if (s[0] == '+'):
			last_plus_prefix_index = 0
			while (s[last_plus_prefix_index] == '+'):
				last_plus_prefix_index += 1

			s = reverse_and_flip(s[:last_plus_prefix_index]) + s[last_plus_prefix_index:]

		else:
			last_invalid_index = len(s) - 1
			while (s[last_invalid_index] == '+'):
				last_invalid_index -= 1

			s = reverse_and_flip(s[:last_invalid_index + 1]) + s[last_invalid_index + 1:]

		reverse_and_flips_count += 1

	result = str(reverse_and_flips_count)

	print('Case #' + str(line_index + 1) + ': ' + result)


input.close()
