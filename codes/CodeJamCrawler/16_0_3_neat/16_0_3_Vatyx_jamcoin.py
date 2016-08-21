import itertools
f = open("C-large.in", 'r')
fo = open("output.txt","w")

f.readline()
txt = f.readline().split()
n = int(txt[0])
j = int(txt[1])

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def base_to_10(num, base):
	if base == 10:
		return int(num)
	total = 0
	for n in xrange(0, len(num)):
		total += int(num[-(n+1)]) * (base ** n)
	return total

# benchmarked on an old single-core system with 2GB RAM.

from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(10000) + 1, 2))

    return True

def getdivsor(num):
	#for x in mrange(2, int(num**0.5+ 1), 1):
	for x in mrange(2, int(10000), 1):
		if num%x == 0:
			return x

fo.write('Case #1:\n')
#strings = ["".join(seq) for seq in itertools.product("01", repeat=n-2)]
print "Oh I got here"
foundstrings = []

for s in itertools.product("01", repeat=n-2):
	if len(foundstrings) == j:
		break
	s = "".join(s)
	s = '1' + s + '1'
	bases = [base_to_10(s, x) for x in xrange(2, 11)]

	#print "Created bases"
	addIt = True
	#print s
	for b in bases:
		#print "I'm checking", b
		if is_prime(b):
			addIt = False
			break
	
	if addIt:
		print s
		foundstrings.append(s)
		fs = s
		fo.write(fs)
		bases = [base_to_10(fs, x) for x in xrange(2, 11)]
		for b in bases:
			fo.write(" " + str(getdivsor(b)))
		fo.write('\n')
	#print "Ok next"
# print foundstrings
# bases = [base_to_10(foundstrings[0], x) for x in xrange(2, 11)]
# print bases
# for b in bases:
# 	print getdivsor(b)

# for fs in foundstrings:
# 	fo.write(fs)
# 	bases = [base_to_10(fs, x) for x in xrange(2, 11)]
# 	for b in bases:
# 		fo.write(" " + str(getdivsor(b)))
# 	fo.write('\n')


#print [getdivsor(x) for x in bases]
# s = foundstrings[0]
# bases = [base_to_10(s, x) for x in xrange(2, 11)]
# divsors = [getdivsor(x) for x in bases]
# print divsors