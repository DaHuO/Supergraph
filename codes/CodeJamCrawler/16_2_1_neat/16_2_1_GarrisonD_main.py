from copy import deepcopy

numbers = {
	0: 'ZERO',
	1: 'ONE',
	2: 'TWO',
	3: 'THREE',
	4: 'FOUR',
	5: 'FIVE',
	6: 'SIX',
	7: 'SEVEN',
	8: 'EIGHT',
	9: 'NINE'
}


def run(data: str):
	digits = list()

	for digit, string in numbers.items():
		if (digit not in digits) and all([symbol in data for symbol in string]):
			digits.append(digit)

			temp = str(deepcopy(data))

			for symbol in string:
				temp = temp.replace(symbol, '', 1)

			if len(temp) == 0:
				return [str(digit)]

			value = run(temp)

			if value:
				return [str(digit)] + value


if __name__ == '__main__':
	count = int(input())

	for a in range(count):
		string = input()
		result = sorted(run(string))
		print('Case #{}: {}'.format(a + 1, ''.join(result)))
