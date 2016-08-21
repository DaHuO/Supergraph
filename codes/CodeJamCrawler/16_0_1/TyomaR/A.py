for test in range(1, int(input()) + 1):
	n = int(input())
	cur = 0
	if n == 0: 
		cur = "INSOMNIA"
	else:
		unused = set([str(i) for i in range(10)])
		while len(unused):
			cur += n
			s = str(cur)
			used = set()
			for i in unused:
				if i in s:
					used.add(i)
			unused -= used
	print("Case #%s: %s" % (test, cur))
