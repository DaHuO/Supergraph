def run(pancakes: list) -> int:
	def is_ready(pancakes: list) -> bool:
		for symbol in pancakes:
			if symbol == '-':
				return False
		return True

	def is_blank(pancakes: list) -> bool:
		for symbol in pancakes:
			if symbol == '+':
				return False
		return True

	def can_full_flip(pancakes: list) -> bool:
		return pancakes[0] == '-' or (pancakes[0] == '+' and pancakes[-1] != '-')

	def normalize(pancakes: list) -> list:
		for symbol in pancakes[::-1]:
			if symbol == '+':
				pancakes.pop()
				continue
			break
		return pancakes

	def flip(pancakes: list) -> list:
		if can_full_flip(pancakes):
			for index, symbol in enumerate(pancakes[::-1]):
				pancakes[index] = '-' if symbol == '+' else '+'
		else:
			for index, symbol in enumerate(pancakes[::-1]):
				if symbol == '+':
					pancakes[0:-index] = flip(pancakes[0:-index])
					break

		return pancakes

	count = 0
	pancakes = normalize(pancakes)

	while not is_ready(pancakes):
		pancakes = normalize(flip(pancakes))
		count += 1

	return count


if __name__ == '__main__':
	for a in range(0, int(input())):
		number = list(input())
		result = run(number)

		print('Case #{}: {}'.format(a + 1, result))
