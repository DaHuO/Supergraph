
def solve(N, li):
	d = {}
	for l in li:
		for i in l:
			d[i] = 0
	for l in li:
		for i in l:
			d[i] += 1
	out = []
	for num in d:
		if d[num] % 2 == 1:
			out.append(num)
	if len(out) != N:
		print ERROR
	return ' '.join([str(x) for x in sorted(out)])

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange(t):
		N = int(raw_input())
		li = []
		for n in xrange(2*N-1):
			li.append([int(x) for x in raw_input().split(' ')])
		print "Case #{}: {}".format(i + 1, solve(N, li))
