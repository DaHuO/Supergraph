# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
map = {}
for i in xrange(1, t + 1):
	map = {}
	n = int(raw_input()) # read a list of integers, 2 in this case
	if n == 0:
		print "Case #{}: INSOMNIA".format(i)
		continue
	for j in xrange(1, 1000):
		counted_number = n*j
		n_str = list(str(counted_number))
		for digit in n_str:
			map[digit] = digit
		if len(map)==10:
			print "Case #{}: {}".format(i, counted_number)
			break
	if not len(map)==10:
		print "Case #{}: INSOMNIA".format(i)
