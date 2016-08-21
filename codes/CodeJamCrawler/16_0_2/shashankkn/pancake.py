def calc(i):
	x = list(i)
	if len(x) == 1:
		if x[0] == '-':
			return 1
		else:
			return 0
	else:
		a = x[0]
		c = 0;
		for b in x[1:]:
			if a != b:
				c=c+1
				a = b
		if x[-1] == '-':
			c = c+1
		return c
			
		

t = int(raw_input())
for i in xrange(1,t+1):
	print("Case #{}: {}").format(i,calc(raw_input()))
	
