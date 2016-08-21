
from google import reader, writer

FULL_HOUSE = set('0123456789')


def digits(number):
	return set(str(number))


def is_enough(known_digits):
	return known_digits == FULL_HOUSE


def is_insomnia(number):
	return number == 0


def main(number):
	known_digits = set()
	current_number = 0
	while not is_enough(known_digits):
		current_number += number
		known_digits.update(digits(current_number))

	return current_number


if __name__ == '__main__':
	input = reader()
	header = next(input)
	test_number = int(header.strip())
	case = 0
	with writer() as output:
		while case < test_number:
			case += 1
			test = next(input)
			test = int(test.strip())
			if is_insomnia(test):
				output.write('Case #%d: INSOMNIA\n' % case)
				continue

			result = main(test)
			output.write('Case #%d: %s\n' % (case, result))
