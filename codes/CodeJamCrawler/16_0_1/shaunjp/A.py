def getans(a):
	if a == 0:
		return "INSOMNIA"
	c = set()
	for i in str(a):
		c.add(i);
	b = a
	while len(c) != 10:
		b += a
		for i in str(b):
			c.add(i);
	return b 

a = int(raw_input())

for i in range (1, a + 1):
	b = int(raw_input())
	ans = getans(b)
	print "Case #" + str(i) + ": " + str(ans)
