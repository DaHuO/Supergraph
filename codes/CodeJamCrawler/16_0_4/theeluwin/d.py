def solve(s):
	K, C, S = [int(ss) for ss in s.split(' ')]
	a = K**(C-1)
	r = []
	for k in range(K):
		r.append(1 + a * k)
	return ' '.join([str(rr) for rr in r])


if __name__ == '__main__':
	infile = open('d.in')
	outfile = open('d.out', 'w')
	indata = infile.read().split('\n')
	T = int(indata[0])
	for t in range(1, T + 1):
		r = solve(indata[t])
		outfile.write("Case #{}: {}\n".format(t, r))
