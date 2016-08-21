f = open("input", "r")
o = open("output", "w")
T = int(f.readline())
[n, limit] = [int(each) for each in f.readline().split(" ")]

x = 2**n
sieve_limit = 1000000
sieve = [0] * sieve_limit
numbers = []

def convert(num, base):
	val = 0
	power = 0
	for each in num[::-1]:
		val += int(each)*(base**power)
		power += 1
	return val

def sieve_calc(upper_bound):
        i = 2
        while i < sieve_limit:
                if sieve[i] == 1:
                        i += 1
                        continue
                numbers.append(i)
                for j in range(i, sieve_limit, i):
                        sieve[j] = 1
                i += 1

def printDivisor(val):
	global numbers
	for each in numbers:
		if val % each == 0:
			return each

def isPrime(val):
	#if val >= len(sieve):
	#	return True
	#return (True if sieve[val] == 0 else False)
	for each in numbers:
		if each >= val:
			break
		if val % each == 0:
			return False
	return True

sieve_calc(2**16)
print "done calculating primes"

count = 0
o.write("Case #1:\n")
i = 2**(n-1)
while i < 2**n:
#for i in range(2**(n-1) + 1, 2**n):
	i += 1

	bin_value = bin(i)[2:]
	print bin_value
	if bin_value[0] == '0' or bin_value[-1] == '0':
		continue
	word = ""
	for j in range(2, 11):
		val = convert(bin_value, j)
		if isPrime(val):
			break
		else:
			word += " " + str(printDivisor(val))
	else:
		line = bin(i)[2:] + word
		o.write(str(line) + "\n")

		count += 1
		if count == limit:
			break

o.close()
f.close()
