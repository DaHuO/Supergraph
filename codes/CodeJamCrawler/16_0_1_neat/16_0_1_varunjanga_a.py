def f(n):
	a = "0000000000"
	a = list(a)
	i = 0
	while True:
		if ''.join(a) == "1111111111":
			return i*n
		i+=1
		for c in str(i*n):
			a[int(c)-int('0')] = '1'

def inp():
	return int(raw_input())
x=inp()
for a in xrange(x):
	n = inp()
	if n == 0: print "Case #"+str(a+1)+": INSOMNIA"
	else: print "Case #"+str(a+1)+": "+str(f(n))