def flip(s):
	l = len(s)
	c = 0;
	
	for i in range (0, l-1):
		if s[i] == '-' and s[i+1] == '+':
			c = c+2
			
	if s[l-1] == '-':
			c = c+2
	
	if s[0] == '-':
		c = c-1

	return c;

n = int(input())
for i in range (0, n):
	l = str(input())
	p = flip(l)
	print("Case #%d: %d" % (i+1, p))
	
