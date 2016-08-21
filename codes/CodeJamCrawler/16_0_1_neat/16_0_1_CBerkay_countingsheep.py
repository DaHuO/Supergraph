def cs(N):
	if N == 0:
		return 'INSOMNIA'
	else:
		d = {}
		i = 1
		t = N
		while True:
			for c in str(t):
				d[c] = 1
			if len(d) == 10:
				return t
			i += 1
			t = N * i

if __name__ == '__main__':
	f = open('in.txt', 'r')
	for i, line in enumerate(f.read().split('\n')):
		if line and i!=0:
			ans = cs(int(line))
			print 'Case #%s: %s' % (i, ans)
	f.close()