import itertools

def problem_c(N, J):
	middles = itertools.product(*([['0', '1']] * ((N - 2) // 2)))
	for _ in range(J):
		middle = next(middles)
		coinjam = '1' + ''.join(reversed(middle)) + ''.join(middle) + '1'
		text = coinjam
		for b in range(2, 11):
			n = int(coinjam, b)
			for i in range(2, n):
				if not n % i:
					text += ' ' + str(i)
					break
		yield text
	

def write_output():
	with open('output.txt', 'w') as output_file:
		output_file.write('Case #1:\n')
		for x in problem_c(32, 500):
			output_file.write('{:s}\n'.format(x))

write_output()