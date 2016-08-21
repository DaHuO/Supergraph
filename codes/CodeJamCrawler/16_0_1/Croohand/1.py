t = int(input())
for test in range(t):
	print('Case #%s: ' % (test + 1), end = '')
	n = int(input())
	if n == 0:
		print('INSOMNIA')
	else:
		cur = str(n)
		used = {i for i in cur}
		while len(used) < 10:
			cur = str(int(cur) + n)
			for i in cur: 
				used.add(i)
		print(cur)