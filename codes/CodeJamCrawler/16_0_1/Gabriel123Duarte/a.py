
def solve(n):
	cont = 1
	original = n
	total = [False] * 10
	while sum(total) < 10:
		n = original * cont
		cont = cont + 1
		s = str(n)
		size = len(s)
		for i in xrange(0, size):
			total[int(s[i]) - 1] = True
		#print str(cont)
		#print str(n) + " - "  + str(sum(total))
		#print str(n) +  " - " + str(cont)
	return n

caso = 1
t = input()
for T in xrange(1, t + 1):
	n = input()
	if n == 0:
		print "Case #" + str(T) + ": INSOMNIA"
	else:
		print "Case #" + str(T) + ": " + str(solve(n))	
#print total


