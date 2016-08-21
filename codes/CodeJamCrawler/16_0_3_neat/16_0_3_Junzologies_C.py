coins = []

# Test Dataset
"""
for x in xrange(2**5,2**6):
	s = "{0:b}".format(x)
	if s[-1] != "0":
		coins.append(s)
"""	
# Small Dataset
"""
for x in xrange(2**15,2**16):
	s = "{0:b}".format(x)
	if s[-1] != "0":
		coins.append(s)
"""
# Large Dataset

for x in xrange(2**31,2**32):
	s = "{0:b}".format(x)
	if s[-1] != "0":
		coins.append(s)

raw_input()
N,J = raw_input().split()
J = int(J)
noJams = 0

print "Case #1:"

for coin in coins:
	divisors = []
	x, cont = 2, True
	
	while x <= 10 and cont: # Interpret in 9 bases, 2 - 10
		cont = False
		
		n = int(coin,x) # Interpreted as base x
		
		for i in xrange(2, int(n ** 0.5)+1):
			if n % i == 0:
				divisors.append(i) # Append divisor
				cont = True
				x += 1
				break
	
	if len(divisors) == 9:
		noJams += 1
		print coin, " ".join(map(str,divisors))
	
	if noJams >= J:
		break