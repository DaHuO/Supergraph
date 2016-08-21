

f = file("B-large.in")
o = file("sol.out", "w")
cnt = int(f.readline())

for i in xrange(cnt):
	curr = f.readline().rstrip()
	p = " "
	cnt = 0
	for j in curr:
		if (p != j):
			print p + " != " + j

			cnt += 1
		p = j
	print "curr[:-1]: " + curr[-1]
	if (curr[-1] == "+"):
		cnt -= 1
	print "Case #" + str(i+1) + ": " + str(cnt) + "\n"
	o.write("Case #" + str(i+1) + ": " + str(cnt) + "\n")
