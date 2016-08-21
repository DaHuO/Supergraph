import math
PrimeList = []
PRIME_LIMIT = 999999

def solveC(n,j):
	res  = []

	num = 2**(n-1) - 1
	while(len(res)<j):
		num = num + 2
		b = toBinary(num)
		if(len(b) > n ):
			print("no sol found")
			break
		decList = [int(num)]+[toDecimal(b,i) for i in range(3,11)]
		factorsList = getFactors(decList) 
		if (1 not in factorsList) :
			resStr = b + " " +" ".join([str(f) for f in factorsList])
			res.append(resStr)

	return res

def getFactors(decList):
	global PrimeList
	res = [1 for i in range(2,11)]
	for i in range(9):
		d = decList[i]
		factor = 0
		lim = math.sqrt(d)
		for p in PrimeList:
			if p > lim :
				break
			elif (d%p == 0): 
				factor = p 
				break
		if (factor == 0):
			break
		else:
			res[i] = factor
	return res

def toDecimal( s, base):
	d = 0
	if (base == 10) :
		d = int(s)
	else:
		p =1
		for c in s[::-1]:
			d = d + int(c)*p 
			p = p * base 
	return d

def toBinary(d):
	return bin(d)[2:]

from itertools import *


def getPrimes(n):
    r = n // 2
    plist = list(islice(repeat(True), r + 1))
    plist[0] = False

    lim = int((n**0.5) / 2 + 1)

    for i in range(1, lim + 1):
        p = 2 * i + 1

        if plist[i]:
            sp = 2 * i * (i + 1)
            while(sp <= r):
                plist[sp] = False
                sp = sp + p

    primes = [2] + [(2 * i + 1) for i in range(r) if plist[i]]
    return primes

if __name__ == "__main__":
	ip_fname = "C-large.in"
	# ip_fname = "C-ex.in"
	# ip_fname = "C-small-attempt1.in"
	op_fname = "C-large.out"
	# op_fname = "C-ex.out"
	# op_fname = "C-small-attempt1.out"
	ip = open(ip_fname, 'r')
	op = open(op_fname , 'w')

	PrimeList = getPrimes(PRIME_LIMIT)

	t = int(ip.readline())
	for tc in range(1,t+1):
		ip_line = ip.readline()
		n,j = map(int,ip_line.split(" "))
		op.write("Case #"+str(tc)+":\n")
		for op_line in solveC(n,j) :
			op.write(op_line+"\n")

	ip.close()
	op.close()
