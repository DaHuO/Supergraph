def f(n):
	if n == 0:
		return "INSOMNIA"
	a = 1
	b = n
	d = {}
	while not ('0' in d and '1' in d and '2' in d and '3' in d and '4' in d and '5' in d and '6' in d and '7' in d and '8' in d and '9' in d):
		for i in str(b):
			d[i] = None
		b = n*(a+1)
		a += 1
	return (a-1)*n

x = raw_input()
for i in range(int(x)):
	a = raw_input()
	print "Case #%s: %s" % (i+1, f(int(a)))