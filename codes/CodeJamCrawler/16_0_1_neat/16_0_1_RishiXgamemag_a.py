testcase = int(raw_input())
def solve(a):
	n = []
	s = []
	i=1
	if a == 0:
		return "INSOMNIA"
	else :
		while len(s) != 10:
			n =[int(j) for j in str(i * a)]
			i += 1
			for num in n:
					if num in s:
						pass
					else :
						s.append(num)
		return (''.join(map(str,n)))			
for testNr in xrange(1, testcase+1):
		x = int(raw_input())
		print("Case #%i: %s" % (testNr, solve(x)))