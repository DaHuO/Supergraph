import gmpy2
import math

def factor(n):
    for i in xrange(2, min(int(math.sqrt(n)) + 1, 100000)):
        if n % i == 0:
            return i
    return None

N = 32
J = 500

print "Case #1:"
for i in xrange(int('0b1'+'0'*(N-2), 2), int('0b1'+'1'*(N-2), 2)+1):
	if J == 0:
		break
	binStr = bin(i)[2:]+'1'
#	print 'Checking: ' + binStr

	noPrime = True
	factors = []
	for base in xrange(2,10+1):
#		print 'Prime checking'
		is_prime = gmpy2.is_prime(int(binStr,base))
		noPrime = not(is_prime) and noPrime
		if is_prime:
#			print 'Prime %i found on base %i' % (int(binStr,base), base)
			break
		else:
			numFactor = factor(int(binStr,base))
			if numFactor:
				factors.append(numFactor)
			else:
				noPrime = False
				break

	if noPrime:
		print binStr  + " " + " ".join(map(str, factors))
		J -= 1
