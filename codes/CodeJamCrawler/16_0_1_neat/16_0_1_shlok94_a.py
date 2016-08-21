T = int(raw_input())
for i in range(T):
	a = raw_input()
	b = set()
	if int(a) == 0:
		print "Case #%s: INSOMNIA" %str(i+1)
	else:
		d=2
		c = a
		while 1:
			for j in c:
				b.add(j)
			if len(b) == 10:
				print "Case #"+ str(i+1) + ": " + c	
				break
			else:
				c = str(d * int(a))
				d = d + 1
