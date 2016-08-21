import collections

def split_numebr(N):
	while N:
		digit = N % 10
		N /= 10
		yield digit


def count_output(N):
	"""Get an integer, generate the output string
	"""
	number_count = {
		1: False,
		2: False,
		3: False,
		4: False,
		5: False,
		6: False,
		7: False,
		8: False,
		9: False,
		0: False,
	}
	for i in range(1, 20000000):
		for digit in split_numebr(i * N):
			number_count[digit] = True
			if all(number_count.values()):
				return i * N
	return 'INSOMNIA'


if __name__ == '__main__':
	with open('A-large.in', 'r'
	) as input, open('A.large.out', 'w') as output:
		T = int(input.readline())
		for i in xrange(T):
			N = int(input.readline())
			output.write(
				'Case #{case_number}: {output}\n'.format(
					case_number=i + 1,
					output=count_output(N),
				)
			)
