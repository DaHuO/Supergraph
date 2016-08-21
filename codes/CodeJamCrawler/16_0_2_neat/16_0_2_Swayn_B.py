import copy
test = int(raw_input())
q = []
for i in range(test):
	q.append(raw_input())
a = []
for i in range(test):
	b = list(q[i])
	c = copy.copy(b)
	aa = 0
	while ('-' in c) :			
		c.reverse()
		aa+=1
		l = len(c)-1-c.index('-')
		c.reverse()
		tmp = []	
		for j in range(l+1):	
			t = c[j]			
			if t == '-':
				c[j] = '+'
			else :
				c[j] = '-'		
	a.append(aa)

for i in range(test):
	print "Case #"+str(i+1)+": "+str(a[i])

