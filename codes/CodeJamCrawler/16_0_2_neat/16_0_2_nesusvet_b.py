
from google import reader, writer


def flip(stack):
	return map(lambda p: '+' if p == '-' else '-', stack[::-1])


def maneuver(stack, i):
	sub = stack[:i + 1]
	return flip(sub) + stack


def main(stack):
	state = stack[0]
	changes = 0
	for char in stack:
		if char != state:
			changes += 1
			state = char

	if char == '-':
		changes += 1

	return changes


if __name__ == '__main__':
	input = reader()
	header = next(input)
	test_number = int(header.strip())
	case = 0
	with writer() as output:
		while case < test_number:
			case += 1
			test = next(input)
			result = main(test.strip())
			output.write('Case #%d: %s\n' % (case, result))
