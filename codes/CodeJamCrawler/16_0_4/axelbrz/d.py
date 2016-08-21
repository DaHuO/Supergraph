from Queue import Queue

f = open("d.in")
d = f.read().strip().split("\n")[1:]
f.close()

o = open("d.out", "w")
for i in xrange(len(d)):
	input = d[i]
	k, c, s = map(int, input.split(" "))
	ln = k**c
	s = ln
	#print ln, k, ln/k
	ln = "Case #%d: %s" % (i + 1, " ".join(map(str, [1+j*(ln/k) for j in xrange(k)])))
	print ln
	o.write(ln + "\n")
o.close()
