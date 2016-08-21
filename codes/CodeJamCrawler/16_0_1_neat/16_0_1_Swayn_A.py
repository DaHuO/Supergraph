test = int(raw_input())
q = []
for i in range(test):
	q.append(int(raw_input()))
a = []
for i in range(test):
	b = q[i]
	if b == 0 :
		a.append('INSOMNIA')
		continue
	aa = set(map(long,str(b)))
	j = 1;
	while True :
		c = b*(j+1)	
		aa = set().union(aa,map(long,str(c)))
		if len(aa) == 10 :
			a.append(c)
			break
		j+=1
for i in range(test):
	print "Case #"+str(i+1)+": "+str(a[i])

