import time

#loads prime numbers from a file containing one number per line
def loadPrimes(filename):
	file = open(filename)
	primes = []
	for line in file:
		primes += [int(line)]
	file.close()
	return primes

# get number represented by string in the given base
def convertToBase(string, base):
	res = 0
	for i in range(0, len(string)):
		res += int(string[len(string) -1 -i]) * base**i
	return res

# get next available string
def getNextString(string):
	requiredLength = len(string) - 2
	nextString = str(bin(convertToBase(string[1:-1], 2)+1))
	nextString = nextString[2:len(nextString)] 
	padding = (requiredLength - len(nextString)) * "0"
	return "1" + padding + nextString + "1"

# try to divide this number with specified number of primes, if none work, give up 
# and return -1
def findFactor(num, limit, primes):
	for i in range(0, limit):
		if (num != primes[i]) and (num % primes[i] == 0) :
			return primes[i]
	return -1

N = 32
J = 500
MAX_ATTEMPTS = 10000
FACTOR_ATTEMPT_LIMIT = 100

t1 = time.time()
primes = loadPrimes("primes")
print "Loaded primes in %d sec" % (time.time() - t1)

string = "1" + "0"*(N - 2) + "1"
solutions = {}

t1 = time.time()

for attempt in range(0, MAX_ATTEMPTS):
	if len(solutions) >= J:
		break
	solution = {}
	found = True
	for base in range(2, 11):
		value = convertToBase(string, base)
		factor = findFactor(value, MAX_ATTEMPTS, primes)
		if factor != -1:
			solution[base] = factor
		else:
			found = False
			break
	if (found):
		solutions[string] = solution
	string = getNextString(string)

#print solutions
if len(solutions) < J:
	print "FAILURE. Found only %d solutions" % len(solutions)
else: 
	print "SUCCESS!"

print "time taken: %d sec" % (time.time() - t1)

output = open("output", "w")
output.write("Case #1:\n")
for solution in solutions:
	line = solution + " "
	for base in range(2, 11):
		line += str(solutions[solution][base]) + " "
	line += "\n"
	output.write(line)
output.close()
