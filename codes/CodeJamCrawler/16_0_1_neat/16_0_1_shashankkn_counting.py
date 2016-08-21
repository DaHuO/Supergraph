def calc(i):
	a = [0,1,2,3,4,5,6,7,8,9]
	c = 1
	if i == 0:
		return "INSOMNIA"
	else:
		while len(a) > 0:
			b = i*c
			for x in (map(int,str(b))):
				if x in a:
					a.remove(x)
			c = c+1
		return b

t = int(raw_input())
for i in xrange(1,t+1):
	print("Case #{}: {}").format(i,calc(int(raw_input())))
	
