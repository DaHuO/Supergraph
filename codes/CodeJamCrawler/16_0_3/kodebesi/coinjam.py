import sys

def divisor(N):
	for a in range(2, int(round(N**0.5))+1):
		if N%a == 0:
			return a
	return -1
	
inputFile = sys.argv[1]
f = open(inputFile, 'r')
content = f.readlines()
NJ = content[1].split(' ')
N = int(NJ[0])
J = int(NJ[1])
print "Case #1:"
count = 0
for s in range(0, 2**(N-2)):
	sbin = "{0:b}".format(s)
	tz = N - 2 - len(sbin)
	candidate = '1' + ('0'*tz) + sbin + '1'
	divisors = []
	for b in range(2, 11):
		val = int(candidate, b)
		div = divisor(val)
		if div < 0:
			break
		divisors.append(div)
	if len(divisors) == 9:
		result = candidate + ' '
		for d in divisors:
			result = result + str(d) + ' '
		print result.strip()
		count = count + 1
	if count == J:
		break