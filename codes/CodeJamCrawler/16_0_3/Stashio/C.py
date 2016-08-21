import re
import numpy

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

NUM_PRIMES_FOR_CHECK = 10000
primes = set(primesfrom2to(NUM_PRIMES_FOR_CHECK))

def getStartingBase10Value(numBits):
	return (2 ** (numBits - 1)) + 1

def getEndingBase10Value(numBits):
	return (2 ** numBits) - 1
	
def tryGetLowestDivisor(N):
	global primes
	for p in primes:
		if N % p == 0:
			return p
			
	return -1
	
def convertBaseAToBaseB(N, A, B):
	ans = 0
	d = 1
	while N > 0:
		R = N % B
		ans += R*d
		d *= A
		N //= B
		
	return ans
		

fr = open("input.in", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1]
	
while curTest < numTests:
	N, J = map(int, getLine().strip().split())
	
	curVal = getStartingBase10Value(N)
	endVal = getEndingBase10Value(N)
	
	found = 0
	
	fw.write("Case #%d:\n" % (curTest+1))
	
	while (found < J) and (curVal <= endVal):
		base2Val = convertBaseAToBaseB(curVal, 10, 2)
		divisors = []
		failed = False
		for base in range(2, 11):
			baseNum = convertBaseAToBaseB(base2Val, base, 10)
			d = tryGetLowestDivisor(baseNum)
			if d == -1:
				failed = True
				break
			else:
				divisors.append(str(d))
				
		if not failed:
			found += 1
			fw.write("%d %s\n" % (base2Val, " ".join(divisors)))
	
		curVal += 2
		
	curTest += 1
					
fr.close()
fw.close()