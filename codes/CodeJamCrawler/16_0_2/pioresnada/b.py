def f():
	n = input().replace('-','1').replace('+','0')
	c = 0
	while int(n):
		m = n[0]
		if m == '0':
			p = n.find('1')
			if p == -1: p = len(n)
			n = n.replace('0', '1', p)
		if m == '1':
			p = n.find('0')
			if p == -1: p = len(n)
			n = n.replace('1', '0', p)
		c = c + 1
	return c

for i in range(int(input())): print("Case #{0}: {1}".format(i+1, f()))
