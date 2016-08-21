
from math import pow
from math import sqrt
import itertools

def isPrime(k):
	# if k is prime, return a divisor
	# else return -1
	if (k%2 == 0):
		return 2
	start = 3
	end = sqrt(k)+1
	while 1:
		# print start
		if start > end+1:
			break
		if (k%start == 0):
			return start
		start = start + 2
	# for x in range(2, k):
	# 	if (k%x == 0):
	# 		return x
	return -1

def findJamcoins(length, howmany):
	multipliers = baseMultipliers(length)

	allcoins = ["".join(seq) for seq in itertools.product("01", repeat=length)]

	for x in range(len(allcoins)):
		if howmany == 0:
			break
		current = allcoins[x]
		if (current[0] == '1' and current[len(current)-1] == '1'):
			# print current
			# is current a jamcoins in all bases?
			interpretations = []
			for i in range(9):
				number = 0
				baselist = multipliers[i]
				# print baselist
				for j in range(len(baselist)):
					tomult = baselist[j]
					currentstr = str(current)
					number = int(currentstr[j])*tomult + number
					# number = number + tomult*(int((str(current))[j]))
				interpretations.append(number)

			divisors = []
			toPrint = [current]
			for number in interpretations:
				divisor = isPrime(number)
				divisors.append(divisor)
				if divisor == -1:
					break
			if -1 in divisors:
				# print 'notprime'
				continue
			else:
				howmany = howmany - 1
				print str(current) + ' ' + str(divisors[0]) + ' ' + str(divisors[1]) + ' ' + str(divisors[2]) + ' ' + str(divisors[3]) + ' ' + str(divisors[4]) + ' ' + str(divisors[5]) + ' ' + str(divisors[6]) + ' ' + str(divisors[7]) + ' ' + str(divisors[8])
				# print current
				# print interpretations

		# if any number in interpretations is prime, current is not a jamcoin


def baseMultipliers(n):
	# gives base multipliers of bases 2..10 for a number of n digits
	toReturn = []

	for base in range(2, 11):
		multipliers = []
		for x in range(n):
			multipliers.append(int(pow(base, x)))
		multipliers.reverse()
		toReturn.append(multipliers)

	return toReturn

t = int(raw_input())

for i in xrange(1, t + 1):
	n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	# string = str(raw_input())

	# print baseMultipliers(3)

	# result = findFlips(string)
	print "Case #{}:".format(i)
	findJamcoins(n, m)
	# findJamcoins(16, 50)

