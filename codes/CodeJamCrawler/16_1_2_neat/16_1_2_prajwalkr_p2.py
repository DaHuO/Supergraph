t = input()
for case in range(t):
	n = input()
	d = dict()
	a = []
	for _ in range(2*n - 1):
		a += map(int,raw_input().split())
	for x in a:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	res = []
	for key in d:
		if d[key]%2:
			res.append(str(key))
	res = sorted(res)
	print "Case #{}: {}".format(case + 1,' '.join(res))
