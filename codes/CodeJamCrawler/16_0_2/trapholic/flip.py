def switch(char):
	if char == '-':
		return '+'
	return '-'


def flip_n(n, input_str):
	a = input_str[:n]
	b = input_str[n:]
	return ''.join([c for c in [switch(d) for d in a[::-1]] + list(b)])


def longest_prefix(input_str):
	start = input_str[0]
	pos = True
	if start == '-':
		pos = False

	count = 1
	for i in range(1,len(input_str)):
		if input_str[i] == start:
			count += 1
		else:
			break
	return count


def all_plus(input_str):
	for c in input_str:
		if c == '-':
			return 0
	return 1


def all_minus(input_str):
	for c in input_str:
		if c == '+':
			return 0
	return 1


def compute(input_str):
	if all_plus(input_str):
		return 0
	if all_minus(input_str):
		return 1
	
	return compute(flip_n(longest_prefix(input_str), input_str)) + 1


with open('B-large.in') as f:
	content = f.readlines()
	num_of_test = int(content[0])

	with open('output.txt', 'wb') as o:
		for i in range(num_of_test):
			result = compute(content[i+1])
			result_str = 'Case #' + str(i+1) + ': ' + str(result)
			o.write(result_str)
			if i < num_of_test-1:
				o.write('\n')
