def solve(N):
	if (N==0):
		return "INSOMNIA"
	notseen=map(str, range(10))
	K = 1
	while (len(notseen)):
		for i in notseen[::-1]:
			if i in str(N*K):
				notseen.remove(i)
		K+=1
	return N*(K-1)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())  # read a list of integers, 2 in this case
	print "Case #{}: {}".format(i, solve(n))
	# check out .format's specification for more formatting options
