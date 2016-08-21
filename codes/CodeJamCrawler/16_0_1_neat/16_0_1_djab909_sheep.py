# Python Sheep Problem
# Code Jam Round 1


#Inputs: T (num inputs), N (number to start with)

def hasSeenAllDigits(digits):
	for d in digits:
		if d == False: 
			return False
	return True

def countSheep(N):
	if N == 0:
		return "INSOMNIA"
	digitsSeen = [False] * 10	
	val = 0
	while hasSeenAllDigits(digitsSeen) == False:
		val += N
		digits = val
		while digits:
			digit = digits%10
			digitsSeen[digit] = True
			digits //= 10
	return str(val)

T = int(raw_input())
for i in range(0,T):
	N = int(raw_input())
	print "Case #{0}: {1}".format(i+1,countSheep(N))
