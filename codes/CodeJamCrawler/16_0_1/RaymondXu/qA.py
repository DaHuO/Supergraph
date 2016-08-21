from sets import Set


def sheep(n):
	if n == 0:
		return 'INSOMNIA'
	i = 1
	curr = n
	seen = Set()
	while len(seen) < 10:
		for digit in str(curr):
			if digit not in seen:
				seen.add(digit)
		i += 1
		curr = i * n

	return (i - 1) * n


def main():
	r = open('input_file.txt', 'r')
	w = open('output_file.txt', 'w')

	t = int(r.readline()) # read a line with a single integer
	print t
	for i in xrange(1, t + 1):
		n = int(r.readline().strip())
		w.write('Case #{}: {}\n'.format(i, sheep(n)))


main()