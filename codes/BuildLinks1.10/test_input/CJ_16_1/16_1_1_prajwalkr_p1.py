t = input()
for _ in range(t):
	a = raw_input()
	d = []
	res = []
	for x in a:
		if not len(res):
			res.append(x)
		elif x < res[0]:
			res.append(x)
		else:
			res = [x] + res
	print ''.join(res)
