def solve(stack):
	last = stack[0]
	c = 0
	for p in stack:
		if(p != last):
			last = p
			c+=1
	if(last == '-'):
		c+=1
	return c


inp = int(input())
for i in range(inp):	
	print("Case #%d:" % (i+1), solve(input())) 
