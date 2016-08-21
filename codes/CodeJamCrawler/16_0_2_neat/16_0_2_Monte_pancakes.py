#revenge of the pancakes

num = int(raw_input())

for i in range(1, num+1):
	flips = 0
	s = raw_input()
	while True:
		if '-' not in s:
			print "Case #{0}: {1}".format(i, flips)
			break
		if '+' not in s:
			print "Case #{0}: {1}".format(i,flips+1)
			break
		flips += 1
		c = s[0]
		count = 0
		for l in s:
			if l != c:
				break
			else:
				count += 1
		
		if c == '-':
			s =  '+'*count + s[count:]
		else:
			s = '-'*count + s[count:]

	
