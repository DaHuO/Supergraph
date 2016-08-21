import sys


def get_digits(n):
	digits = set()

	while (n != 0):
		digits.add(n % 10)
		n /= 10

	return digits


input = open(sys.argv[1], 'r')

t = input.readline()
lines = input.readlines()

for line_index in range(len(lines)):
	if (lines[line_index][-1] == '\n'):
		lines[line_index] = lines[line_index][:-1]

	n = int(lines[line_index])

	if (n == 0):
		result = 'INSOMNIA'
	else:
		x = n
		digits_seen = set()

		while (True):
			digits_seen |= get_digits(x)
			if (len(digits_seen) >= 10):
				break
			else:
				x += n

		result = str(x)

	print('Case #' + str(line_index + 1) + ': ' + result)


input.close()
