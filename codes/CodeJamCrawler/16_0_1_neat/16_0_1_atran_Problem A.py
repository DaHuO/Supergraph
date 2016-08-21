t = int(raw_input())

def printResult(number, text):
	print "Case #{}: {}".format(number, text)

for i in xrange(1, t + 1):
	n = int(raw_input())

	if n == 0:
		printResult(i, "INSOMNIA")
	else:
		memo = [False] * 10
		j = 1
		while(1):
		 	digits = [int(digit) for digit in str(n * j)]

		 	for digit in digits:
		 		memo[digit] =  True

		 	if False not in memo:
		 		printResult(i, n * j)
		 		break

		 	j = j + 1

	

