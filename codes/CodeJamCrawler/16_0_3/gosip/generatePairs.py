from math import sqrt

data = []
pairs = []

def makePairs():
	l = len(data)
	for i in range(l):
		for j in range(i+1,l):
			tryAddPair(i, j)

def tryAddPair(i, j):
	one = data[i]
	two = data[j]
	commonDivisors = []
	for k in range(9):
		cd = intersect(one[1][k], two[1][k])
		if len(cd) == 0: 
			return False
		commonDivisors.append(cd)
	pairs.append( ([i,j], commonDivisors) )
	return True
	

def intersect(l1, l2):
	inter = []
	for x in l1:
		if x in l2:
			inter.append(x)
	return inter

def generateData(st, numIter):
	for _ in range(numIter):
		datum = testForJamcoin(st)
		if len(datum) > 0: 
			data.append( ("".join([str(x) for x in st]), datum ) )
		st = increment(st)

def increment(st):
	l = len(st) - 2
	while st[l] == '1':
		st[l] = '0'
		l -= 1
	st[l] = '1'
	return st

def testForJamcoin(s):
	datum = []
	for i in range(2,11):
		n = countBase(s, i)
		divs = divisors(n)
		if len(divs) == 0: 
			return []
		else:
			datum.append(divs)
	return datum

def countBase(s, base):
	n = 0
	i = 0
	exp = 1
	while i < len(s):
		if s[i] == '1':
			n += exp
		exp *= base
		i += 1		
	return n

def divisors(n):
	upperBound = n // 2
	i = 2
	divisors = []
	while i < upperBound:
		if n % i == 0: 
			add = True
			for d in divisors:
				if i % d == 0:
					add = False
					break
			if (add): 
				divisors.append(i)
		i += 1
	return divisors

def main():
	generateData(list('10000001'), 64)
	makePairs()
	pairsFile = open('pairs.dat', 'w')
	for pair in pairs:
		i,j = pair[0]
		divisors = " ".join(str(x[0]) for x in pair[1])
		print(data[i][0] + " " + data[j][0] + " " + divisors, file=pairsFile)
	pairsFile.close()

if __name__ == '__main__':
	main()