t = int(input())

case = 0
while t:
	case += 1
	t -= 1
	n = int(input())
	print('Case #', case, ':', sep='', end = ' ')
	if n == 0:
		print('INSOMNIA')
		continue
	temp = n
	c = 2
	d = set()
	while len(d) != 10:
		#print(temp, d)
		s = str(temp)
		oldlen = len(d)
		for i in s:
			d.add(i)
		newlen = len(d)
		temp = n*c
		c += 1
	print(temp-n)