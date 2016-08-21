def pick(n):
	t = [0,1,2,3,4,5,6,7,8,9]
	c = 0
	
	while True :
		if n == n*2:
			return -1
		else:
			c = c + 1
			s = str(c * n)
			#print(s)
			for l in s:
				if int(l) in t:
					t.remove(int(l))
					
			if len(t) == 0:
				return c*n


n = int(input())
l = []


for i in range (0, n):
	l.append(int(input()))
	
for i in range (0, n):
	p = pick(l[i])
	if p != -1:
		print("Case #%d: %d" % (i+1, p))
	else:
		print("Case #%d: %s" % (i+1, "INSOMNIA"))

	
