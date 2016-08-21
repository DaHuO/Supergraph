def solve(K, C):
	ret = []
	for i in range(K):
		pos = i
		for j in range(C-1):
			pos = pos*K + i
		ret.append(pos+1)
	return ret

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	k, c, j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	print "Case #{}:".format(i),
	for i in solve(k, c):
		print i,
	print
