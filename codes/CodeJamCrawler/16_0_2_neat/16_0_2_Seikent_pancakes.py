#pancakes

def min_mov(pancakes_input):
	c = 0
	p = pancakes_input
	#print p,' ',
	l = []
	last_c = ''
	while c < len(p):
		if last_c != p[c]:
			l.append(p[c])
			last_c = p[c]
		c += 1
	p = ''.join(l)
	#print p
	if p == '-':
		return 1
	if p == '+':
		return 0
	cuenta = 0
	c = 0
	if p[0] == '-':
		cuenta += 1
		c += 2
	else:
		c = 1
	while c < len(p):
		cuenta += 2
		c += 2
	return cuenta

#print min_mov('--+-')
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	pancakes_input = raw_input()  
	m = min_mov(pancakes_input)
	print "Case #{}: {}".format(i, m)