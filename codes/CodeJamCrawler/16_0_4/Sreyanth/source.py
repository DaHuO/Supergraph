# your code goes here

t = int(raw_input())

for i in range(t):
	a, b, c = raw_input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	
	d = ""
	for j in range(a):
		d += str(j+1)
		d += " "
	d.strip()
	print "Case #%d: %s" % (i+1, d)