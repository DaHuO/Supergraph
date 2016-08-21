def solve(n, ks):
	if n == 0:
		print "Case #%d: INSOMNIA" % ks
	else:
		k = 1
		num = []
		while len(num) < 10:
			s = str(n*k)
			for c in s:
				if c not in num:
					num.append(c)
			k += 1
		print "Case #%d: %d" % (ks, n*(k-1) )

t = input()
for ks in range(1,t+1):
	n = input()
	solve(n, ks)