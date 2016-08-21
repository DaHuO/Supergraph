def all_true(xs):
 	res = True
 	for v in xs.values():
 		res = res and v
 	return res

def sleeping_number(n):
	if (n == 0):
		return "INSOMNIA"
	digits_seen = {}
	for i in xrange(0, 10):
		digits_seen[str(i)] = False
	for c in str(n):
			digits_seen[c] = True	
	m = n
	while not all_true(digits_seen):
		m += n
		for c in str(m):
			digits_seen[c] = True			
	return m
		
'''for n in xrange(0, 1000000):
	print sleeping_number(n) '''


inf = open("a.in", 'r')
outf = open("a.out", 'w')

t = int(inf.readline())

for k in xrange(0, t):
	n = long(inf.readline())		
	outf.write("Case #" + str(k + 1) + ": ")	
	outf.write(str(sleeping_number(n)) + "\n")
outf.close()

