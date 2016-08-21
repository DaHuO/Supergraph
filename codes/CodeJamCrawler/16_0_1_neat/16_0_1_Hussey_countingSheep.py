user_input = raw_input("Enter:")
cases = int(user_input)
outArr = []

for i in range(cases):
	num = int( raw_input())
	seen = [False for i in range(10)]
	i = 1
	snum = -1
	while False in seen and num != 0:
		snum = num * i
		for c in str(snum):
			nc = int(c)
			seen[nc] = True
		i += 1
	outArr.append(snum)


with open('output.txt', 'wb') as f:
	for l,out in enumerate(outArr):
		if out == -1:
			f.write( "Case #%d: INSOMNIA\n" % (l+1) )
		else:
			f.write( "Case #%d: %d\n" % (l+1,out) )