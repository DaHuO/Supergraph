f = open("a.in")
d = map(int, f.read().strip().split("\n")[1:])
f.close()

o = open("a.out", "w")
for i in xrange(len(d)):
	a = set()
	n = int(d[i])
	for j in xrange(1, 1000001):
		k = n * j
		for e in str(k): a.add(e)
		if len(a) == 10: break
	if len(a) == 10:
		s = str(k)
	else:
		s = "INSOMNIA"
	ln = "Case #%d: %s" % (i + 1, s)
	print ln
	o.write(ln + "\n")
o.close()
	

