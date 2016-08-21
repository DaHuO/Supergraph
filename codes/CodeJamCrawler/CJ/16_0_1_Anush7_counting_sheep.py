t = input()
r = ['0','1','2','3','4','5','6','7','8','9']
for i in range(1,t+1):
	s = []
	n = input()
	c = 1
	if n > 0:
		while True:
			val = c * n
			for v in str(val):
				if v not in s:
					s.append(v)
					
			if set(r) == set(s):
				print "Case #"+str(i)+": "+str(val)
				break
			
			c += 1
	else:
		print "Case #"+str(i)+": INSOMNIA"
			
	t -= 1
