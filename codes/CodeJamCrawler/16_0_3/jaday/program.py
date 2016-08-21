import math

def InterpretBase(s, r):
	base10 = 0
	for x in range(0, len(s)):
		if(s[x] == '1'):
			base10 += r**(len(s) - x - 1)
	return base10

def FindDivisor(n):
	for x in range(2, int(math.sqrt(n)) + 1):
		if(n % x == 0):
			return x
	return -1
	
def Next(s):
	val = int(s, 2)
	val += 2
	return str(bin(val))[2:]

f = open('C:/Users/Jeremy/Desktop/Code/3/input.txt', 'r')
numCases = int(f.readline())
for x in range(0,numCases):
	line = f.readline().split()
	n = int(line[0])
	j = int(line[1])
	results = []
	jamPerm = "1"
	jamPerm += "0" * (n - 2)
	jamPerm += "1"
	numFound = 0
	while(numFound < j):
		print jamPerm
		isJam = True
		divisors = [0] * 9
		for y in range(2, 11):
			num = InterpretBase(jamPerm, y)
			div = FindDivisor(num)
			if(div == -1):
				isJam = False
				break
			else:
				divisors[y-2] = div
		if(isJam):
			print "That worked."
			results.append((jamPerm, divisors))
			numFound += 1
		jamPerm = Next(jamPerm)
	f2 = open('C:/Users/Jeremy/Desktop/Code/3/output.txt', 'w')
	f2.write("Case #1:\n")
	for y in range(0,len(results)):
		s = results[y][0]
		for z in range(0, len(results[y][1])):
			s += " "
			s += str(results[y][1][z])
		f2.write(s + "\n")
		
	