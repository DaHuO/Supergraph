def solve(L):
	N = len(L)
	count = 0
	for i in range(N-1):
		if (L[i] != L[i+1]):
			count += 1
	if L[-1] == '-':
		count += 1
	return count

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	L = raw_input() # read a list of integers, 2 in this case
	print "Case #{}: {}".format(i, solve(L))
