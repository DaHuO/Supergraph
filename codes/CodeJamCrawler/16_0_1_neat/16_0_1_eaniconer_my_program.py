m = int(input())

for i in range(m):
	t = int(input())
	if t == 0:
		print('Case #%d: INSOMNIA'%(i+1))
	else:	
		s = set()
		n = t
		while True:
			for el in str(n):
				s.add(el)
			#print(s)
			if len(s) == 10:
				break
			n += t
			
		print('Case #%d: %d'%(i+1, n))


