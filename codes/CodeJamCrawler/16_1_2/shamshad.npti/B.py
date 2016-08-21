t = int(raw_input())

for c in range(1, t + 1):
	n = int(raw_input())
	rows = [0 for i in range(2501)]
	for i in range(2 * n - 1):
		s = map(int, raw_input().split())
		for e in s:
			rows[e]+=1;
	out = []
	for i in range(2501):
		if rows[i] % 2 == 0: continue;
		out.append(str(i))
	print 'Case #%d: %s' % (c, ' '.join(out))


