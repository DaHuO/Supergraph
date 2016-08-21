t = input()
for i in xrange(t):
	n = input()
	a = map(int,raw_input().split())
	b = []
	for j in xrange(n):
		b.append([a[j],j])

	s= ''
	while True:
		b.sort(key=lambda x: x[0],reverse=True)
		
		if  b[0][0] +2 <= b[1][0]:
			b[0][0] -= 2
			s = s+chr(b[0][1]+65)
			s = s+chr(b[0][1]+65)
			s = s+' '
		elif b[0][0]!= 1 and b[1][0]!= 1:
			b[0][0] -= 1
			b[1][0] -= 1
			s = s+chr(b[0][1]+65)
			s = s+chr(b[1][1]+65)
			s = s+' '
		else:
			while(n>0):
				if b[n-1][0] == 0:
					b.pop()
					n = n - 1
				else:
					break
			if len(b)% 2 == 0:
				if b[0][0] == 2:
					b[0][0] -= 1
					s = s+chr(b[0][1]+65)
					s = s+' '
				elif len(b) == 2:
					b[0][0] -= 1
					b[1][0] -= 1
					s = s+chr(b[0][1]+65)
					s = s+chr(b[1][1]+65)
					s = s+' '
					break
				else:
					b[0][0] -= 1
					b[1][0] -= 1
					s = s+chr(b[0][1]+65)
					s = s+chr(b[1][1]+65)
					s = s+' '
			else:
				if b[0][0] == 2:
					b[0][0] -= 2
					s = s+chr(b[0][1]+65)
					s = s+chr(b[0][1]+65)
					s = s+' '
				else:
					b[0][0] -= 1
					s = s+chr(b[0][1]+65)
					s = s+' '	

	print "Case #%d: %s" % (i+1,s)										
					
			
