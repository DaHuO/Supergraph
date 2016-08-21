import itertools
import math
def convertToBases(strInput):
	output = [0] * 9 # output is list of integers 
		# where each integer represents the input string in base i + 2
	for base in range(2,11):
		for i in range(0, len(strInput)):
			output[base-2] += int(strInput[i]) * base**(len(strInput)-i-1) 
	return output

def findDivisors(listInput):
	output = [0] * 9
	for i in range(0,len(listInput)):
		# print listInput
		for j in range(2,500): # int(math.sqrt(listInput[i]))
			if listInput[i] % j == 0:
				output[i] = j

				break
	return output

numTests = int(raw_input())  # read a line with a single integer
inputStr = raw_input().split(" ")
N = int(inputStr[0])
J = int(inputStr[1])

combinations = [('1' + "".join(seq) + '1') for seq in itertools.product("01", repeat=N-2)]
print "Case #1:"

for i in range(1, J+1):
	# finding ith sequence that satisfies conditions
	for seq in combinations:
		baseRep = convertToBases(seq)
		# print seq
		# print baseRep
		divisors = findDivisors(baseRep)
		if all(divisors):
			print "{} {}".format(str(seq), " ".join([str(d) for d in divisors]))
			combinations.remove(seq)
			break
# print combinations
	# print "Case #{}: {}".format(i, orignumber*(counter-1))