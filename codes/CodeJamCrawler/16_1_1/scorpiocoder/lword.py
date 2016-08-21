t=int(raw_input())
for i in range(t):
	s = raw_input()
	x = ""
	x = s[0]

	for y in s[1:len(s)]:
		if y >= x[0]:
			x = y + x
		else:
			x = x + y
	
	print "Case #"+str(i+1)+": "+x

		
