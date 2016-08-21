def f(n, ary):
	n = str(n)
	for i in n:
		k = int(i)
		if not ary[k]:
			ary[k] += 1

for t in xrange(input()):
	n = input()
	if n == 0:
		print "Case #%d"%(t+1) + ": " + "INSOMNIA"
	else:
		ary = [0]*10
		f(n, ary)
		i = 2
		k = 0
		while len(set(ary)) != 1:
			k = n*i
			f(k, ary)
			i += 1
		print "Case #%d"%(t+1) + ": " + str(k)