def parse(number: int) -> set:
	return set(str(number))


def run(number: int):
	digits = set()
	value = number
	counter = 0

	while True:
		if value == 0:
			return "INSOMNIA"

		if len(digits) == 10:
			break

		counter += 1
		value = number * counter

		digits = digits.union(parse(value))

	return value


if __name__ == '__main__':
	for a in range(0, int(input())):
		number = int(input())
		result = run(number)

		print('Case #{}: {}'.format(a + 1, result))
