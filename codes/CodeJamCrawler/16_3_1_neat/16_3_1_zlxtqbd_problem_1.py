for t in range(int(raw_input())):
	N = int(raw_input())
	numbers = map(int, raw_input().split())

	result = []
	while any(x > 0 for x in numbers):
		m = max(numbers)
		i = numbers.index(m)
		result.append(i)
		numbers[i] -= 1
		if sum(numbers) == 2 and len(result) % 2 == 1:
			result.append(26)

	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '']

	result_letters = [letters[a] for a in result]

	new_result = []

	length = len(result_letters)
	if len(result_letters) % 2 == 1:
		length -= 1

	for i in range(0, length, 2):
		new_result.append(result_letters[i] + result_letters[i+1])

	if len(result_letters) % 2 == 1:
		new_result.append(result_letters[-1])

	print "Case #{}: {}".format(t+1, str(new_result).replace(",", "").replace("'", "")[1:-1])