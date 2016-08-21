def solve(n):
	s = set(list(str(n)))
	c = 2
	while(len(s) < 10):
		n2 = n*c
		
		if(n == n2):
			return "INSOMNIA"
		for d in str(n2):
			s.add(d)
		if(len(s) == 10):
			return n2
		c+=1
	return c
inp = int(input())
for i in range(inp):	
	print("Case #%d:" % (i+1), solve(int(input()))) 
